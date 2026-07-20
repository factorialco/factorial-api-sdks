# F::ApiPublicCredential

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **company_id** | **String** | company id for all kind of accesses |  |
| **id** | **String** | id of the credential prefixed by the type of credential |  |
| **email** | **String** | Only for Access Oauth token | [optional] |
| **login_email** | **String** | Only for Access Oauth token | [optional] |
| **full_name** | **String** |  | [optional] |
| **first_name** | **String** | Only for Access Oauth token | [optional] |
| **last_name** | **String** | Only for Access Oauth token | [optional] |
| **employee_id** | **String** | Id for hte employee related. Only for Access Oauth token |  |
| **role** | **String** | Employee role in the Company. Only for Access Oauth token | [optional] |
| **gdpr_tos** | **Boolean** | Only for Company Oauth or API key | [optional] |
| **legal_name** | **String** | Only for Company Oauth or API key | [optional] |
| **locale** | **String** | Only for Company Oauth or API key | [optional] |
| **logo** | **String** | Only for Company Oauth or API key | [optional] |
| **name** | **String** | Only for Company Oauth or API key | [optional] |
| **onboarded_on** | **String** | Only for Company Oauth or API key | [optional] |
| **subscription_plan** | **String** | Only for Company Oauth or API key | [optional] |
| **tin** | **String** | Only for Company Oauth or API key | [optional] |
| **to_be_deleted** | **String** | Only for Company Oauth or API key | [optional] |
| **tos** | **Boolean** | Only for Company Oauth or API key | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ApiPublicCredential.new(
  company_id: 1,
  id: access-1,
  email: test@factorial.co,
  login_email: test@factorial.co,
  full_name: null,
  first_name: Hellen,
  last_name: Smith,
  employee_id: 1,
  role: Smith,
  gdpr_tos: false,
  legal_name: Company legal name,
  locale: Company locale,
  logo: Thumbnail companylogo url,
  name: Company name,
  onboarded_on: Factorial onboarding date,
  subscription_plan: Company subscription plan,
  tin: Company tax identification number,
  to_be_deleted: Company deletion date,
  tos: false
)
```

