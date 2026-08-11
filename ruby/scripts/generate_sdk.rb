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
# Plus --set-version=X.Y.Z to pin an exact version (used by the beta
# workflow); otherwise the version already in version.rb is kept —
# release-please owns bumps.

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
SPEC_BASE_URL = 'https://api.factorialhr.com/oas/'

set_version_arg = ARGV.grep(/\A--set-version=/).first
requested_version = set_version_arg&.split('=', 2)&.last
ARGV.delete(set_version_arg) if set_version_arg

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

step "Spec: #{spec} (date #{date_str})"

# --- 3. Resolve the gem version: release-please owns it ---
# Regenerating never bumps: the version already in version.rb (maintained by
# release-please from Conventional Commits) is reused, so there is nothing to
# revert afterwards. --set-version pins an exact version for the beta workflow.
version = requested_version ||
          File.read(VERSION_FILE, encoding: 'UTF-8')[/VERSION\s*=\s*['"]([^'"]+)['"]/, 1] ||
          abort("ERROR: could not read the current version from #{VERSION_FILE}")
step "Gem version: #{version}#{' (from --set-version)' if requested_version}"

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

# --- 7.6. Regenerate the typed webhook catalog (stage 3) ---
# Reads the RAW spec: the normalized one has the webhooks section stripped.
step 'Generating webhook catalog'
run!('ruby', 'scripts/generate_webhooks.rb', spec)

# --- 8. Re-attach the F require and the facade (idempotent) ---
step 'Re-attaching the F require and the facade'
content = File.read(ENTRYPOINT)
File.write(ENTRYPOINT, "require 'f'\n#{content}") unless content.match?(/^require 'f'$/)
File.open(ENTRYPOINT, 'a') { |f| f.puts(REQUIRE_LINE) } unless File.read(ENTRYPOINT).include?(REQUIRE_LINE)

# --- 8.5. Refresh the factorial-api-sdks skill reference tables ---
# Same anti-drift loop as release.ts / release.py. Runs after step 8: the
# tables' Ruby column is read from the loaded gem, which needs the facade
# re-attached to the regenerated entrypoint.
step 'Refreshing the skill reference'
run!('python3', '../scripts/generate_skill.py', spec)

# --- 9. Sanity check ---
step 'Verifying the gem loads'
# Quoted heredoc: the #{...} below is passed through literally, for the child
# ruby process to interpolate, not this script.
load_check = <<~'RUBY'
  require "factorial_api"
  abort("F::Api did not load") unless defined?(F::Api)
  extras = F.constants.sort - [:Api]
  abort("namespace polluted: F:: carries #{extras.inspect} besides :Api") unless extras.empty?
  puts "OK #{F::Api::VERSION} - #{F::Api::API_CLASSES.size} APIs"
RUBY
run!('bundle', 'exec', 'ruby', '-e', load_check)

# --- 10. Verify the facade still works on the regenerated client ---
step 'Running facade specs'
run!('bundle', 'exec', 'rspec', 'spec/factorial_api')

step 'Done. Review the diff with git; run gem build when ready to package.'
