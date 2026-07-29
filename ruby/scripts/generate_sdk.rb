#!/usr/bin/env ruby
# frozen_string_literal: true

# Regenerates the Ruby SDK from an OpenAPI spec.
# Usage: ruby scripts/generate_sdk.rb [oas-YYYY-MM-DD.yaml]
# With no argument, uses the most recent oas-*.yaml in the root.

require 'fileutils'

ROOT = File.expand_path('..', __dir__)
Dir.chdir(ROOT)

GENERATED_PATHS = %w[
  lib/factorial_api/api
  lib/factorial_api/models
  spec/api
  spec/models
].freeze

REQUIRE_LINE  = "require 'factorial_api/api'"
ENTRYPOINT    = 'lib/factorial_api.rb'
VERSION_FILE  = 'lib/factorial_api/version.rb'
CONFIG_FILE   = 'openapi-ruby-client.yaml'

def step(msg) = puts("\n==> #{msg}")

def run!(*cmd)
  puts "    $ #{cmd.join(' ')}"
  system(*cmd) or abort("ERROR: command failed: #{cmd.join(' ')}")
end

# --- 1. Locate the spec and extract its date ---
VALID_BUMPS = %w[major minor patch].freeze
# First semver version; major 2 targets API 2026-07-01 in version_map.json,
# matching the TypeScript and Python SDKs.
INITIAL_VERSION = '2.0.0'

beta = !ARGV.delete('--beta').nil?
bump_arg = ARGV.grep(/\A--bump=/).first
bump = bump_arg&.split('=', 2)&.last
ARGV.delete(bump_arg) if bump_arg
if bump && !VALID_BUMPS.include?(bump)
  abort("ERROR: --bump must be one of #{VALID_BUMPS.join(', ')} (got #{bump.inspect})")
end

spec = ARGV[0] || Dir.glob('oas-*.yaml').grep_v(/normalized/).max
abort('ERROR: no oas-*.yaml found') unless spec && File.exist?(spec)

date_str = spec[/\d{4}-\d{2}-\d{2}/] or abort("ERROR: #{spec} has no YYYY-MM-DD date")

step "Spec: #{spec} (date #{date_str})#{' [beta]' if beta}"

# --- 2. Compute the gem version: MAJOR.MINOR.PATCH[.beta.N] ---
# Plain semver, same model as the TypeScript and Python SDKs: the major
# tracks the Factorial API version (mapped in the repo-root version_map.json,
# so a new dated API version is a major bump), minor = features and
# patch = fixes in the handwritten layer. Default bump is minor, matching
# the sibling release scripts. Interim only: once release-please owns the
# Ruby package, it takes over the version.
bump_explicit = !bump.nil?
bump ||= 'minor'

previous = File.exist?(VERSION_FILE) ? File.read(VERSION_FILE)[/VERSION\s*=\s*['"]([^'"]+)['"]/, 1] : nil
prev_base = previous&.sub(/\.beta\.\d+\z/, '')
prev_is_beta = !previous.nil? && previous != prev_base

base =
  if prev_base.nil? || prev_base.match?(/\A\d{8}\./)
    # First semver release, or migrating from the legacy date-first scheme.
    INITIAL_VERSION
  elsif prev_is_beta && !bump_explicit
    # Iterate the current beta, or promote it to a release: the base was
    # already bumped when the first beta of this line was cut.
    prev_base
  else
    major, minor, patch = prev_base.split('.').map { |part| Integer(part, 10) }
    case bump
    when 'major'
      major += 1
      minor = 0
      patch = 0
    when 'minor'
      minor += 1
      patch = 0
    when 'patch'
      patch += 1
    end
    "#{major}.#{minor}.#{patch}"
  end

version = base
if beta
  n = previous&.match(/\A#{Regexp.escape(base)}\.beta\.(\d+)\z/) { |m| Integer(m[1], 10) + 1 } || 1
  version = "#{base}.beta.#{n}"
end

bump_label = bump_explicit ? bump : "#{bump} by default"
step "Gem version: #{version} (bump: #{bump_label}#{", previous: #{previous}" if previous})"

# --- 3. Normalize operationIds ---
step 'Normalizing spec'
FileUtils.rm_f(Dir.glob('*.normalized.yaml'))
run!('ruby', 'scripts/normalize_oas.rb', spec)
normalized = spec.sub(/\.yaml\z/, '.normalized.yaml')

# --- 4. Update the generator config ---
# Surgical line edits instead of a YAML round-trip, so comments survive.
step "Updating #{CONFIG_FILE}"
config_text = File.read(CONFIG_FILE)
config_text.sub!(/^inputSpec: .*/, "inputSpec: #{normalized}") or
  abort("ERROR: inputSpec line not found in #{CONFIG_FILE}")
config_text.sub!(/^(\s*)gemVersion: .*/, "\\1gemVersion: #{version}") or
  abort("ERROR: gemVersion line not found in #{CONFIG_FILE}")
File.write(CONFIG_FILE, config_text)

# --- 5. Clean up previously generated code ---
step 'Cleaning previous generated code'
FileUtils.rm_rf(GENERATED_PATHS)

# --- 6. Generate ---
step 'Generating SDK'
run!('openapi-generator', 'generate', '-c', CONFIG_FILE)

# --- 6.5. Patch generated models: nil-tolerant required-field setters ---
# The spec marks fields as required that the live API returns as null;
# without this patch, deserializing those responses raises ArgumentError.
step 'Patching generated models'
run!('ruby', 'scripts/patch_models.rb')

# --- 7. Re-attach the facade (idempotent) ---
step 'Re-attaching the F::Api facade'
File.open(ENTRYPOINT, 'a') { |f| f.puts(REQUIRE_LINE) } unless File.read(ENTRYPOINT).include?(REQUIRE_LINE)

# --- 8. Sanity check ---
step 'Verifying the gem loads'
# Quoted heredoc: the #{...} below is passed through literally, for the child
# ruby process to interpolate — not this script.
load_check = <<~'RUBY'
  require "factorial_api"
  abort("F::Api did not load") unless defined?(F::Api)
  puts "OK #{F::VERSION} - #{F::Api::API_CLASSES.size} APIs"
RUBY
run!('bundle', 'exec', 'ruby', '-e', load_check)

# --- 9. Verify the facade still works on the regenerated client ---
step 'Running facade specs'
run!('bundle', 'exec', 'rspec', 'spec/factorial_api')

step 'Done. Review the diff with git; run gem build when ready to package.'
