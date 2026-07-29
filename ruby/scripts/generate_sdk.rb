#!/usr/bin/env ruby
# frozen_string_literal: true

# Regenerates the Ruby SDK from an OpenAPI spec.
#
# The spec is fetched, never committed (same contract as the TS/Python SDKs):
#   ruby scripts/generate_sdk.rb                        # latest spec
#   ruby scripts/generate_sdk.rb --version=2026-10-01   # a dated API version
#   ruby scripts/generate_sdk.rb path/to/oas.yaml       # a local file (offline dev)
#   OPENAPI_SPEC_URL=https://api.local.factorial.dev/oas/ ruby scripts/generate_sdk.rb
#
# Plus --bump=major|minor|patch and --beta (see DEVELOPMENT.md).

require 'fileutils'
require 'net/http'
require 'uri'
require 'yaml'

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

# Fetches a URL following up to 3 redirects; aborts on any non-2xx.
def http_get!(url, hops = 3)
  abort("ERROR: too many redirects fetching the spec (#{url})") if hops.zero?

  response = Net::HTTP.get_response(URI(url))
  return http_get!(response['location'], hops - 1) if response.is_a?(Net::HTTPRedirection)

  abort("ERROR: fetching spec failed: HTTP #{response.code} for #{url}") unless response.is_a?(Net::HTTPSuccess)

  response.body
end

# --- 1. Parse the flags ---
VALID_BUMPS = %w[major minor patch].freeze
# First semver version; major 2 targets API 2026-07-01 in version_map.json,
# matching the TypeScript and Python SDKs.
INITIAL_VERSION = '2.0.0'
SPEC_BASE_URL = 'https://api.factorialhr.com/oas/'

beta = !ARGV.delete('--beta').nil?
bump_arg = ARGV.grep(/\A--bump=/).first
bump = bump_arg&.split('=', 2)&.last
ARGV.delete(bump_arg) if bump_arg
if bump && !VALID_BUMPS.include?(bump)
  abort("ERROR: --bump must be one of #{VALID_BUMPS.join(', ')} (got #{bump.inspect})")
end

version_arg = ARGV.grep(/\A--version=/).first
requested_date = version_arg&.split('=', 2)&.last
ARGV.delete(version_arg) if version_arg
if requested_date && !requested_date.match?(/\A\d{4}-\d{2}-\d{2}\z/)
  abort("ERROR: --version must be a date like 2026-10-01 (got #{requested_date.inspect})")
end

# --- 2. Obtain the spec: a local file if given, otherwise fetch it ---
# Specs are never committed; downloads land in gitignored oas-<date>.yaml.
spec = ARGV[0]
if spec
  abort("ERROR: spec file not found: #{spec}") unless File.exist?(spec)
  spec_body = File.read(spec, encoding: 'UTF-8')
else
  spec_url = ENV.fetch('OPENAPI_SPEC_URL', nil)
  spec_url = nil if spec_url && spec_url.empty?
  spec_url ||= requested_date ? "#{SPEC_BASE_URL}?version=#{requested_date}" : SPEC_BASE_URL

  step "Fetching spec from #{spec_url}"
  spec_body = http_get!(spec_url)
end

date_str = YAML.unsafe_load(spec_body).dig('info', 'version').to_s
abort("ERROR: could not read info.version from the spec (got #{date_str.inspect})") unless
  date_str.match?(/\A\d{4}-\d{2}-\d{2}\z/)
if requested_date && requested_date != date_str
  abort("ERROR: requested API version #{requested_date} but the spec says #{date_str}")
end

unless spec
  spec = "oas-#{date_str}.yaml"
  File.write(spec, spec_body)
end

step "Spec: #{spec} (date #{date_str})#{' [beta]' if beta}"

# --- 3. Compute the gem version: MAJOR.MINOR.PATCH[.beta.N] ---
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

# --- 4. Normalize operationIds ---
step 'Normalizing spec'
FileUtils.rm_f(Dir.glob('*.normalized.yaml'))
run!('ruby', 'scripts/normalize_oas.rb', spec)
normalized = spec.sub(/\.yaml\z/, '.normalized.yaml')

# --- 5. Update the generator config ---
# Surgical line edits instead of a YAML round-trip, so comments survive.
step "Updating #{CONFIG_FILE}"
config_text = File.read(CONFIG_FILE)
config_text.sub!(/^inputSpec: .*/, "inputSpec: #{normalized}") or
  abort("ERROR: inputSpec line not found in #{CONFIG_FILE}")
config_text.sub!(/^(\s*)gemVersion: .*/, "\\1gemVersion: #{version}") or
  abort("ERROR: gemVersion line not found in #{CONFIG_FILE}")
File.write(CONFIG_FILE, config_text)

# --- 6. Clean up previously generated code ---
step 'Cleaning previous generated code'
FileUtils.rm_rf(GENERATED_PATHS)

# --- 7. Generate ---
step 'Generating SDK'
run!('openapi-generator', 'generate', '-c', CONFIG_FILE)

# --- 7.5. Patch generated models: nil-tolerant required-field setters ---
# The spec marks fields as required that the live API returns as null;
# without this patch, deserializing those responses raises ArgumentError.
step 'Patching generated models'
run!('ruby', 'scripts/patch_models.rb')

# --- 8. Re-attach the facade (idempotent) ---
step 'Re-attaching the F::Api facade'
File.open(ENTRYPOINT, 'a') { |f| f.puts(REQUIRE_LINE) } unless File.read(ENTRYPOINT).include?(REQUIRE_LINE)

# --- 9. Sanity check ---
step 'Verifying the gem loads'
# Quoted heredoc: the #{...} below is passed through literally, for the child
# ruby process to interpolate, not this script.
load_check = <<~'RUBY'
  require "factorial_api"
  abort("F::Api did not load") unless defined?(F::Api)
  puts "OK #{F::VERSION} - #{F::Api::API_CLASSES.size} APIs"
RUBY
run!('bundle', 'exec', 'ruby', '-e', load_check)

# --- 10. Verify the facade still works on the regenerated client ---
step 'Running facade specs'
run!('bundle', 'exec', 'rspec', 'spec/factorial_api')

step 'Done. Review the diff with git; run gem build when ready to package.'
