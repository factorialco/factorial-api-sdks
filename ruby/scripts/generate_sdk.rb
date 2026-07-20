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
  docs
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
spec = ARGV[0] || Dir.glob("oas-*.yaml").grep_v(/normalized/).max
abort("ERROR: no oas-*.yaml found") unless spec && File.exist?(spec)

date_str = spec[/\d{4}-\d{2}-\d{2}/] or abort("ERROR: #{spec} has no YYYY-MM-DD date")
year, month, day = date_str.split("-").map { |part| Integer(part, 10) }

step "Spec: #{spec} (date #{year}.#{month}.#{day})"

# --- 2. Compute the gem version: MAJOR.MINOR.YEAR.MONTH.DAY.BUILD ---
config = YAML.load_file(CONFIG_FILE)
major_minor = config.fetch("additionalProperties").fetch("sdkMajorMinor")

previous_version = File.exist?(VERSION_FILE) ? File.read(VERSION_FILE)[/VERSION\s*=\s*['"]([^'"]+)['"]/, 1] : nil
previous_date = previous_version&.split(".")&.values_at(2, 3, 4)&.join(".")

build = (previous_date == "#{year}.#{month}.#{day}") ? Integer(previous_version.split(".").last) + 1 : 0

version = "#{major_minor}.#{year}.#{month}.#{day}.#{build}"
step "Gem version: #{version} (build #{build.zero? ? 'first for this date' : "increment from #{previous_version}"})"

# --- 3. Normalize operationIds ---
step "Normalizing spec"
FileUtils.rm_f(Dir.glob("*.normalized.yaml"))
run!("ruby", "scripts/normalize_spec.rb", spec)
normalized = spec.sub(/\.yaml\z/, ".normalized.yaml")

# --- 4. Update the generator config ---
step "Updating #{CONFIG_FILE}"
config["inputSpec"] = normalized
config["additionalProperties"]["gemVersion"] = version
File.write(CONFIG_FILE, config.to_yaml)

# --- 5. Clean up previously generated code ---
step "Cleaning previous generated code"
FileUtils.rm_rf(GENERATED_PATHS)

# --- 6. Generate ---
step "Generating SDK"
run!("openapi-generator", "generate", "-c", CONFIG_FILE)

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

step "Done. Review the diff with git; run gem build when ready to package."