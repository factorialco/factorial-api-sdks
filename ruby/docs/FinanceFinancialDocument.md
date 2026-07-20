# F::FinanceFinancialDocument

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Factorial unique identifier. |  |
| **net_amount_cents** | **Integer** | Net amount in cents. | [optional] |
| **total_amount_cents** | **Integer** | Total amount in cents. | [optional] |
| **document_number** | **String** | Document number. | [optional] |
| **currency** | **String** | Document currency. | [optional] |
| **status** | **String** | Current status. |  |
| **due_date** | **String** | Due date. | [optional] |
| **document_date** | **String** | Document date. | [optional] |
| **legal_entity_id** | **String** | Factorial unique identifier for the legal entity of the financial document. | [optional] |
| **vendor_id** | **String** | Factorial unique identifier for the vendor of the financial document. | [optional] |
| **file** | **Object** | File attached. | [optional] |
| **updated_at** | **String** | Updation date. |  |
| **taxes** | **Array&lt;Object&gt;** | Taxes. |  |
| **fully_reconciled_at** | **String** | Date when was fully reconciled. | [optional] |
| **recorded_at** | **String** | Date when was recorded. | [optional] |
| **duplicate_financial_document_id** | **String** | Factorial unique identifier for the duplicate financial document. | [optional] |
| **validated_at** | **String** | Date when was validated. | [optional] |
| **validated_by_id** | **String** | Factorial unique identifier for the user who validated the financial document. | [optional] |
| **document_type** | **String** | Type of the financial document. Using \&quot;invoice\&quot; as default. |  |
| **parent_financial_document_id** | **String** | Factorial unique identifier for the parent financial document of the financial document. | [optional] |
| **taxes_total_amount_cents** | **Integer** | Taxes total amount in cents. | [optional] |
| **issuer_name** | **String** | Name of the entity issuing the financial document. | [optional] |
| **issuer_address_line_1** | **String** | First line of the issuer&#39;s address. | [optional] |
| **issuer_address_line_2** | **String** | Second line of the issuer&#39;s address. | [optional] |
| **issuer_city** | **String** | City of the issuer&#39;s address. | [optional] |
| **issuer_postal_code** | **String** | Postal code of the issuer&#39;s address. | [optional] |
| **issuer_state** | **String** | State or province of the issuer&#39;s address. | [optional] |
| **issuer_country_code** | **String** | Country code of the issuer&#39;s address. | [optional] |
| **issuer_tax_id** | **String** | Tax identification number of the issuer. | [optional] |
| **recipient_name** | **String** | Name of the entity receiving the financial document. | [optional] |
| **recipient_address_line_1** | **String** | First line of the recipient&#39;s address. | [optional] |
| **recipient_address_line_2** | **String** | Second line of the recipient&#39;s address. | [optional] |
| **recipient_city** | **String** | City of the recipient&#39;s address. | [optional] |
| **recipient_postal_code** | **String** | Postal code of the recipient&#39;s address. | [optional] |
| **recipient_state** | **String** | State or province of the recipient&#39;s address. | [optional] |
| **recipient_country_code** | **String** | Country code of the recipient&#39;s address. | [optional] |
| **recipient_tax_id** | **String** | Tax identification number of the recipient. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceFinancialDocument.new(
  id: 135,
  net_amount_cents: 10000,
  total_amount_cents: 11210,
  document_number: INV-135,
  currency: USD,
  status: review,
  due_date: 2020-01-01,
  document_date: 2020-01-01,
  legal_entity_id: 13,
  vendor_id: 33,
  file: {id&#x3D;1, filename&#x3D;invoice.pdf, url&#x3D;https://factorial.com/invoice.pdf, size&#x3D;1024, content_type&#x3D;application/pdf, created_at&#x3D;2020-01-01T00:00:00.000Z},
  updated_at: 2020-01-01T00:00:00.000Z,
  taxes: [{amount_cents&#x3D;1210, base_amount_cents&#x3D;10000, percentage&#x3D;0.21, type&#x3D;vat, tax_rates&#x3D;[{percentage&#x3D;21.0}]}],
  fully_reconciled_at: 2020-01-01T00:00:00.000Z,
  recorded_at: 2020-01-01T00:00:00.000Z,
  duplicate_financial_document_id: null,
  validated_at: 2020-01-01T00:00:00.000Z,
  validated_by_id: 31,
  document_type: invoice,
  parent_financial_document_id: 135,
  taxes_total_amount_cents: 1210,
  issuer_name: Acme Corporation,
  issuer_address_line_1: 123 Main Street,
  issuer_address_line_2: Suite 100,
  issuer_city: San Francisco,
  issuer_postal_code: 94105,
  issuer_state: California,
  issuer_country_code: US,
  issuer_tax_id: US123456789,
  recipient_name: XYZ Company,
  recipient_address_line_1: 456 Market Street,
  recipient_address_line_2: Floor 5,
  recipient_city: New York,
  recipient_postal_code: 10001,
  recipient_state: New York,
  recipient_country_code: es,
  recipient_tax_id: B66854530
)
```

