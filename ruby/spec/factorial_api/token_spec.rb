# frozen_string_literal: true

# Handwritten specs for F::Api::Token. The JWTs are built by hand (base64url
# segments joined with dots, fake signature) so every claim set — and every
# malformed variant — is fully controlled by the example that uses it.

require 'spec_helper'
require_relative '../support/jwt_fixtures'

RSpec.describe F::Api::Token do
  include JwtFixtures

  describe '#claims' do
    it 'decodes the payload of a well-formed JWT, string-keyed' do
      token = described_class.new(build_jwt('cid' => '42', 'staff' => true))

      expect(token.claims).to eq('cid' => '42', 'staff' => true)
      expect(token.jwt?).to be(true)
    end

    it 'decodes payloads of every base64 padding length' do
      %w[a ab abc].each do |value|
        token = described_class.new(build_jwt('v' => value))

        expect(token.claims).to eq('v' => value)
      end
    end

    it 'decodes the base64url alphabet (-_ instead of +/)' do
      # eyJ4IjoiPz8_PiJ9 is base64url for {"x":"???>"} and contains a `_`
      # that plain base64 decoding would reject.
      token = described_class.new("#{encode_segment(alg: 'none')}.eyJ4IjoiPz8_PiJ9.sig")

      expect(token.claims).to eq('x' => '???>')
    end

    it 'is empty for an opaque (non-JWT) credential' do
      token = described_class.new('opaque-credential')

      expect(token.claims).to eq({})
      expect(token.jwt?).to be(false)
    end

    it 'is empty for nil' do
      token = described_class.new(nil)

      expect(token.raw).to eq('')
      expect(token.claims).to eq({})
    end

    it 'is empty when the segment count is not three' do
      two = "#{encode_segment(alg: 'none')}.#{encode_segment(exp: 1)}"

      expect(described_class.new(two).claims).to eq({})
      expect(described_class.new("#{two}.sig.extra").claims).to eq({})
    end

    it 'is empty when the payload is not decodable JSON' do
      expect(described_class.new('head.!!!not-base64!!!.sig').claims).to eq({})
      expect(described_class.new('head.bm90LWpzb24.sig').claims).to eq({}) # "not-json"
    end

    it 'is empty when the payload is JSON but not an object' do
      expect(described_class.new('head.WzFd.sig').claims).to eq({}) # [1]
    end

    it 'is frozen, like the token itself' do
      token = described_class.new(build_jwt('cid' => '42'))

      expect(token).to be_frozen
      expect(token.claims).to be_frozen
    end
  end

  describe '#expires_at' do
    it 'returns the exp claim as a UTC Time' do
      token = described_class.new(build_jwt('exp' => 1_767_225_600))

      expect(token.expires_at).to eq(Time.at(1_767_225_600).utc)
      expect(token.expires_at.utc?).to be(true)
    end

    it 'is nil when exp is absent, non-numeric, or the token is opaque' do
      expect(described_class.new(build_jwt('cid' => '42')).expires_at).to be_nil
      expect(described_class.new(build_jwt('exp' => 'soon')).expires_at).to be_nil
      expect(described_class.new('opaque').expires_at).to be_nil
    end
  end

  describe '#expired?' do
    let(:now) { Time.at(1_000_000) }

    it 'is true from the exp instant onwards' do
      expect(described_class.new(build_jwt('exp' => now.to_i - 1)).expired?(now: now)).to be(true)
      expect(described_class.new(build_jwt('exp' => now.to_i)).expired?(now: now)).to be(true)
    end

    it 'is false before exp' do
      expect(described_class.new(build_jwt('exp' => now.to_i + 1)).expired?(now: now)).to be(false)
    end

    it 'is false without a readable expiry (the API stays the authority)' do
      expect(described_class.new(build_jwt('cid' => '42')).expired?(now: now)).to be(false)
      expect(described_class.new('opaque').expired?(now: now)).to be(false)
    end
  end

  describe '#expiring_soon?' do
    let(:now) { Time.at(1_000_000) }

    it 'is true when exp falls within the margin' do
      token = described_class.new(build_jwt('exp' => now.to_i + 100))

      expect(token.expiring_soon?(margin: 100, now: now)).to be(true)
      expect(token.expiring_soon?(margin: 99, now: now)).to be(false)
    end

    it 'defaults to a 60-second margin' do
      expect(described_class.new(build_jwt('exp' => now.to_i + 59)).expiring_soon?(now: now)).to be(true)
      expect(described_class.new(build_jwt('exp' => now.to_i + 61)).expiring_soon?(now: now)).to be(false)
    end

    it 'is false without a readable expiry' do
      expect(described_class.new('opaque').expiring_soon?(now: now)).to be(false)
    end
  end

  describe '#[]' do
    it 'reads a claim by string or symbol' do
      token = described_class.new(build_jwt('cid' => '42'))

      expect(token['cid']).to eq('42')
      expect(token[:cid]).to eq('42')
      expect(token[:missing]).to be_nil
    end
  end

  describe '#to_s / #inspect' do
    it 'round-trips the raw credential through to_s' do
      jwt = build_jwt('cid' => '42')

      expect(described_class.new(jwt).to_s).to eq(jwt)
      expect(described_class.new(jwt).raw).to eq(jwt)
    end

    it 'keeps the raw credential out of inspect' do
      jwt = build_jwt('cid' => '42')
      token = described_class.new(jwt)

      expect(token.inspect).to include('"cid"=>"42"').or include('"cid" => "42"')
      expect(token.inspect).not_to include(jwt)
    end
  end
end
