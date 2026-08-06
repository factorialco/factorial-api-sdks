# frozen_string_literal: true

# The F:: root namespace is shared by every Factorial gem: each gem claims
# exactly one constant under it and emits everything inside that one. This
# gem's claim is F::Api. These examples pin that contract for the WHOLE gem
# at once — generated code, handwritten layer, and anything a future change
# might add — so a regression fails the suite instead of colliding with
# another gem's constants at some customer's site.

require 'spec_helper'

RSpec.describe 'F:: namespace hygiene' do
  it 'claims exactly one constant on the shared F:: root' do
    expect(F.constants).to contain_exactly(:Api)
  end

  it 'adds no module methods to the shared F:: root' do
    expect(F.singleton_methods).to be_empty
  end
end
