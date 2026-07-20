# F::ContractsMaterializedTemplate

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Synthetic identifier for this materialized template, composed as {company_id}-{template_type}-{legal_entity_id}-{country_code}. Used as a stable cursor reference for pagination.  |  |
| **company_id** | **String** | Identifier of the company that owns this template. All templates are scoped to a company; use this to correlate templates across different levels (company, country, legal entity) for the same organization.  |  |
| **legal_entity_id** | **String** | Identifier of the legal entity this template has been materialized for. Present only when template_type is legal_entity. Legal entity templates represent the final merged view of fields applicable to employees hired under that legal entity, combining company-level defaults with country-specific and legal-entity-specific overrides.  | [optional] |
| **country_code** | **String** | ISO 3166-1 alpha-2 country code identifying the country this template applies to. Present for country and legal_entity template types. Determines which country-specific fields and options are included (e.g. fields required by Spanish or French labor law).  | [optional] |
| **template_type** | **String** | The level at which this template has been materialized. Templates follow a three-tier inheritance hierarchy: company (base defaults for the whole organization), country (overrides per country labor law), and legal_entity (final merged view per legal entity, combining all three levels). Use legal_entity when you need the definitive set of fields for a specific hiring context.  |  |
| **template** | **Array&lt;Object&gt;** | The ordered list of contract fields defined in this template after merging all inheritance levels and removing hidden fields. Each entry is a FragmentField describing a single configurable attribute of a contract (e.g. contract type, job title, salary). The list reflects the final effective set of fields an employee contract under this template will contain.  |  |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsMaterializedTemplate.new(
  id: 1-legal_entity-42-es,
  company_id: 1,
  legal_entity_id: 1,
  country_code: es,
  template_type: legal_entity,
  template: null
)
```

