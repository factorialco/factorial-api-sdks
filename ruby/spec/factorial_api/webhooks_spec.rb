# frozen_string_literal: true

# Handwritten specs for the generated webhook catalog (webhooks.rb). They
# lock the invariants the generator promises, so a regeneration that breaks
# the catalog shape fails here instead of in a user's webhook receiver.

require 'spec_helper'

RSpec.describe 'F webhook catalog' do
  it 'exposes a consistent, non-trivial catalog' do
    expect(F::Api::WEBHOOK_CATALOG.size).to be > 100
    expect(F::Api::WEBHOOK_SUBSCRIPTION_TYPES.size).to eq(F::Api::WEBHOOK_CATALOG.size)
    expect(F::Api::WEBHOOK_PAYLOAD_TYPES.size).to eq(F::Api::WEBHOOK_CATALOG.size)
    expect(F::Api::WEBHOOK_SUBSCRIPTION_TYPES).to eq(F::Api::WEBHOOK_SUBSCRIPTION_TYPES.uniq)
  end

  it 'uses namespace/resource/event subscription types' do
    expect(F::Api::WEBHOOK_SUBSCRIPTION_TYPES)
      .to all(match(%r{\A[a-z0-9_]+/[a-z0-9_]+/[a-z0-9_]+\z}))
  end

  it 'maps every subscription type to a generated model class' do
    F::Api::WEBHOOK_PAYLOAD_TYPES.each_value do |klass|
      expect(klass).to be_a(Class)
      expect(klass.name).to start_with('F::Api::')
    end
  end

  it 'defines one alias constant per event, pointing at its payload class' do
    F::Api::WEBHOOK_PAYLOAD_TYPES.each do |subscription_type, payload_class|
      alias_const = "#{subscription_type.split('/').map do |segment|
        segment.split('_').map(&:capitalize).join
      end.join}Webhook"

      expect(F::Api.const_defined?(alias_const)).to be(true), "missing alias #{alias_const}"
      expect(F::Api.const_get(alias_const)).to equal(payload_class)
    end
  end

  it 'fills in every catalog entry field' do
    entry = F::Api::WEBHOOK_CATALOG.first

    expect(entry.subscription_type).not_to be_empty
    expect(entry.namespace).not_to be_empty
    expect(entry.resource).not_to be_empty
    expect(entry.event).not_to be_empty
    expect(entry.payload_schema).not_to be_empty
  end

  it 'builds a payload object from a delivered body' do
    payload_class = F::Api::WEBHOOK_PAYLOAD_TYPES.fetch('ats/application/create')
    payload = payload_class.build_from_hash('id' => '7', 'ats_job_posting_id' => '3')

    expect(payload).to be_a(F::Api::AtsApplicationCreateWebhook)
    expect(payload.id).to eq('7')
  end
end
