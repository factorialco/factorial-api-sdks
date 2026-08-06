# frozen_string_literal: true

require 'json'

# Builds JWTs by hand — base64url segments joined with dots, fake signature —
# exactly like a real producer would, so every claim set (and every malformed
# variant) is fully controlled by the example that uses it.
module JwtFixtures
  # Encodes exactly like a real JWT producer: base64url alphabet, no padding.
  def encode_segment(hash)
    [JSON.generate(hash)].pack('m0').tr('+/', '-_').delete('=')
  end

  def build_jwt(claims)
    "#{encode_segment(alg: 'none')}.#{encode_segment(claims)}.fake-signature"
  end
end
