#!/usr/bin/env ruby
# frozen_string_literal: true

# Regenerates the Ruby SDK from an OpenAPI spec.
# Usage: ruby scripts/generate_sdk.rb [oas-YYYY-MM-DD.yaml]
# With no argument, uses the most recent oas-*.yaml in the root.

require "yaml"
require "fileutils"

ROOT = File.expand_path("..", __dir__)
Dir.chdir(ROOT)

GENERATED_PATHS = %w[
  lib/factorial_api/api
  lib/factorial_api/models
  spec/api
  spec/models
].freeze

REQUIRE_LINE  = "require 'factorial_api/api'"
ENTRYPOINT    = "lib/factorial_api.rb"
VERSION_FILE  = "lib/factorial_api/version.rb"
CONFIG_FILE   = "openapi-ruby-client.yaml"

def step(msg) = puts("\n==> #{msg}")

def run!(*cmd)
  puts "    $ #{cmd.join(' ')}"
  system(*cmd) or abort("ERROR: command failed: #{cmd.join(' ')}")
end

# --- 1. Locate the spec and extract its date ---
VALID_BUMPS = %w[feature fix none].freeze

beta = !ARGV.delete("--beta").nil?
bump = ARGV.grep(/\A--bump=/).first&.then { |arg| ARGV.delete(arg); arg.split("=", 2).last }
if bump && !VALID_BUMPS.include?(bump)
  abort("ERROR: --bump must be one of #{VALID_BUMPS.join(', ')} (got #{bump.inspect})")
end

spec = ARGV[0] || Dir.glob("oas-*.yaml").grep_v(/normalized/).max
abort("ERROR: no oas-*.yaml found") unless spec && File.exist?(spec)

date_str = spec[/\d{4}-\d{2}-\d{2}/] or abort("ERROR: #{spec} has no YYYY-MM-DD date")
spec_date = date_str.delete("-") # "2026-07-01" -> "20260701"

step "Spec: #{spec} (date #{date_str})#{beta ? ' [beta]' : ''}"

# --- 2. Compute the gem version: YYYYMMDD.X.Y[.beta.N] ---
# The API date is the leading segment and the only breaking boundary; X.Y
# versions the handwritten layer (features.fixes) and MUST stay backwards
# compatible within the same date line. `~> YYYYMMDD` therefore pins users
# to an API version while receiving every compatible update.
config = YAML.load_file(CONFIG_FILE)
facade = config.fetch("additionalProperties").fetch("sdkMajorMinor")
facade_x, facade_y = facade.split(".").map { |part| Integer(part, 10) }

previous = File.exist?(VERSION_FILE) ? File.read(VERSION_FILE)[/VERSION\s*=\s*['"]([^'"]+)['"]/, 1] : nil
prev_date, prev_x, prev_y = previous&.split(".")&.values_at(0, 1, 2)
prev_is_beta = previous&.include?(".beta.") || false
same_line = prev_date == spec_date && prev_x == facade_x.to_s

# Without an explicit --bump, regenerating the same line is a rebuild (a fix
# release), while a new API date starts at the X.Y configured in the YAML.
# Releasing after a beta of the same line keeps the base version, since the
# beta already sorts below it.
bump ||= (same_line && !prev_is_beta ? "fix" : "none")

case bump
when "feature"
  facade_x += 1
  facade_y = 0
when "fix"
  facade_y = [facade_y, same_line && prev_y ? Integer(prev_y, 10) + 1 : facade_y].max
end

version = "#{spec_date}.#{facade_x}.#{facade_y}"

if beta
  n = previous&.match(/\A#{Regexp.escape(version)}\.beta\.(\d+)\z/) { |m| Integer(m[1], 10) + 1 } || 1
  version = "#{version}.beta.#{n}"
end

step "Gem version: #{version} (bump: #{bump}#{previous ? ", previous: #{previous}" : ''})"

# --- 3. Normalize operationIds ---
step "Normalizing spec"
FileUtils.rm_f(Dir.glob("*.normalized.yaml"))
run!("ruby", "scripts/normalize_oas.rb", spec)
normalized = spec.sub(/\.yaml\z/, ".normalized.yaml")

# --- 4. Update the generator config ---
# Surgical line edits instead of a YAML round-trip, so comments survive.
step "Updating #{CONFIG_FILE}"
config_text = File.read(CONFIG_FILE)
config_text.sub!(/^inputSpec: .*/, "inputSpec: #{normalized}") or
  abort("ERROR: inputSpec line not found in #{CONFIG_FILE}")
config_text.sub!(/^(\s*)gemVersion: .*/, "\\1gemVersion: #{version}") or
  abort("ERROR: gemVersion line not found in #{CONFIG_FILE}")
# Persist the bumped facade version, so the next run starts from it.
config_text.sub!(/^(\s*)sdkMajorMinor: .*/, "\\1sdkMajorMinor: '#{facade_x}.#{facade_y}'") or
  abort("ERROR: sdkMajorMinor line not found in #{CONFIG_FILE}")
File.write(CONFIG_FILE, config_text)

# --- 5. Clean up previously generated code ---
step "Cleaning previous generated code"
FileUtils.rm_rf(GENERATED_PATHS)

# --- 6. Generate ---
step "Generating SDK"
run!("openapi-generator", "generate", "-c", CONFIG_FILE)

# --- 6.5. Patch generated models: nil-tolerant required-field setters ---
# The spec marks fields as required that the live API returns as null;
# without this patch, deserializing those responses raises ArgumentError.
step "Patching generated models"
run!("ruby", "scripts/patch_models.rb")

# --- 7. Re-attach the facade (idempotent) ---
step "Re-attaching the F::Api facade"
unless File.read(ENTRYPOINT).include?(REQUIRE_LINE)
  File.open(ENTRYPOINT, "a") { |f| f.puts(REQUIRE_LINE) }
end

# --- 8. Sanity check ---
step "Verifying the gem loads"
run!("bundle", "exec", "ruby", "-e",
     'require "factorial_api"; ' \
     'abort("F::Api did not load") unless defined?(F::Api); ' \
     'puts "OK #{F::VERSION} - #{F::Api::API_CLASSES.size} APIs"')

# --- 9. Verify the facade still works on the regenerated client ---
step "Running facade specs"
run!("bundle", "exec", "rspec", "spec/factorial_api")

step "Done. Review the diff with git; run gem build when ready to package."
