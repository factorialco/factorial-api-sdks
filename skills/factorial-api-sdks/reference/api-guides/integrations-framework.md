<!-- Vendored from https://apidoc.factorialhr.com/docs/integrations-framework.md -->

# Integrations Framework

## 💡 Context

In Factorial, we have developed the first version of our **integrations framework**, allowing Factorial to sync data (employee compensation, expenses…) into external systems (payroll software, ERPs).

This functionality is exposed through our [public API](/reference), so that external partners and clients can integrate external software more easily and consistently.

<Callout icon="❗️" theme="error">
  The integrations framework is currently only avalable for official partners. Interested clients must contact their account manager
</Callout>

## ✨ Introduction

This framework enables external developers to sync data from Factorial to the different external softwares in an easy and transparent way for the user, providing the best experience to the user. A **summary** of the flow of how the framework would be:

1. Client **defines** all the data (compensations, expenses) in Factorial
2. Client **clicks** on ‘Sync to \[*external\_software\_name]*
3. Partner receives a **webhook** notification
4. Partner fetches **data to sync** from Factorial
5. Partner syncs it to the external software
6. Partner reports the **sync result** back to Factorial so the client can have **visibility of the result** of the sync

<Callout icon="❗️" theme="error">
  **Important**

  Please note that steps 3,4,5 and 6 are mandatory for the partner to be implemented. See [Async Integration Flow ](https://apidoc.factorialhr.com/docs/integrations-framework#-async-integration-flow)for more details.
</Callout>

## 🔧 Setup integration for the first time

To get started, the partner must to specify 2 things to Factorial team:

### **Data Fields**

From Factorial, we can send a set of fields when syncing each item to the external software. The partner must specify 2 things: which data they want to receive and which fields are mandatory for their integration:

### Compensations

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Format
      </th>

      <th>
        Do they want to have this data in our response? (Yes/No)
      </th>

      <th>
        Is it mandatory to sync to the payroll software (Yes/No)
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `employee_id`  (in Factorial)
      </td>

      <td>
        Integer
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        `employee_company_identifier` (in the payroll software)
      </td>

      <td>
        String
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        `legal_entity_id`
      </td>

      <td>
        Integer
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        `payroll_concept_id`
      </td>

      <td>
        Integer
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        `amount`
      </td>

      <td>
        Integer

        * cents for money
        * minutes for time
        * km for distance
        * units for unit
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        `units` (those are the available in Factorial, maybe a mapping needs to be done with the units of the payroll software)
      </td>

      <td>
        String: one of `distance`, `money`, `time`, `unit`
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        `effective_on` (the effective date is typically the last day of the payroll run)
      </td>

      <td>
        yyyy-mm-dd
      </td>

      <td />

      <td />
    </tr>
  </tbody>
</Table>

### Expenses

| Fields                      | Format                                                                                                                              | Do they want to have this data in our response? (Yes/No) | Is it mandatory to sync to the ERP software (Yes/No) |
| :-------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------- | :--------------------------------------------------- |
| `expense_id` (in Factorial) | Integer                                                                                                                             |                                                          |                                                      |
| `expense_type`              | String: one of expense, mileage, per\_diem                                                                                          |                                                          |                                                      |
| `group_id`                  | Integer                                                                                                                             |                                                          |                                                      |
| `company_id`                | Integer                                                                                                                             |                                                          |                                                      |
| `legal_entity_id`           | Integer                                                                                                                             |                                                          |                                                      |
| `employee_id`               | Integer                                                                                                                             |                                                          |                                                      |
| `total_amount`              | Integer (cents)                                                                                                                     |                                                          |                                                      |
| `currency`                  | String (currency code in ISO 4217 format)                                                                                           |                                                          |                                                      |
| `status`                    | String: one of pending, changes\_requested, approved, paid, rejected, reversed, draft, in\_payroll, sent\_to\_pay                   |                                                          |                                                      |
| `payment`                   | String: one of reimbursable, not\_reimbursable                                                                                      |                                                          |                                                      |
| `reimbursable_amount`       | Integer (cents)                                                                                                                     |                                                          |                                                      |
| `reimbursable_currency`     | String (currency code in ISO 4217 format)                                                                                           |                                                          |                                                      |
| `reimbursement_method`      | String: one of unknown, sepa\_transfer, payroll                                                                                     |                                                          |                                                      |
| `created_at`                | yyyy-mm-dd hh:mm                                                                                                                    |                                                          |                                                      |
| `effective_on`              | yyyy-mm-dd hh:mm                                                                                                                    |                                                          |                                                      |
| `review_request_at`         | yyyy-mm-dd hh:mm                                                                                                                    |                                                          |                                                      |
| `paid_at`                   | yyyy-mm-dd hh:mm                                                                                                                    |                                                          |                                                      |
| `status_updated_at`         | yyyy-mm-dd hh:mm                                                                                                                    |                                                          |                                                      |
| `updated_at`                | yyyy-mm-dd hh:mm                                                                                                                    |                                                          |                                                      |
| `description`               | String                                                                                                                              |                                                          |                                                      |
| `internal_reference`        | String                                                                                                                              |                                                          |                                                      |
| `creation_type`             | String: one of manual, automatic, travelperk                                                                                        |                                                          |                                                      |
| `merchant_name`             | String                                                                                                                              |                                                          |                                                      |
| `user_merchant`             | String                                                                                                                              |                                                          |                                                      |
| `merchant_tin`              | String                                                                                                                              |                                                          |                                                      |
| `category_id`               | Integer                                                                                                                             |                                                          |                                                      |
| `category_name`             | String                                                                                                                              |                                                          |                                                      |
| `subcategory_id`            | Integer                                                                                                                             |                                                          |                                                      |
| `subcategory_name`          | String                                                                                                                              |                                                          |                                                      |
| `ledger_account_id`         | Integer                                                                                                                             |                                                          |                                                      |
| `exchange_rate`             | Number                                                                                                                              |                                                          |                                                      |
| `taxes`                     | Array                                                                                                                               |                                                          |                                                      |
| `mileage`                   | Integer (units of distance)                                                                                                         |                                                          |                                                      |
| `units`                     | String: one of kilometres, miles                                                                                                    |                                                          |                                                      |
| `start_date`                | yyyy-mm-dd hh:m                                                                                                                     |                                                          |                                                      |
| `end_date`                  | yyyy-mm-dd hh:mm                                                                                                                    |                                                          |                                                      |
| `origin`                    | String                                                                                                                              |                                                          |                                                      |
| `destination`               | String                                                                                                                              |                                                          |                                                      |
| `round_trip`                | Boolean                                                                                                                             |                                                          |                                                      |
| `calculated_mileage`        | Integer (units of distance)                                                                                                         |                                                          |                                                      |
| `calculated_amount`         | Integer (units of money)                                                                                                            |                                                          |                                                      |
| `rate`                      | Integer                                                                                                                             |                                                          |                                                      |
| `cost_center_ids`           | Array of objects with cost\_center 'name', 'id' and 'percentage' associated                                                         |                                                          |                                                      |
| `budget_id`                 | Integer                                                                                                                             |                                                          |                                                      |
| `budget_name`               | String                                                                                                                              |                                                          |                                                      |
| `project_id`                | Integer                                                                                                                             |                                                          |                                                      |
| `project_name`              | String                                                                                                                              |                                                          |                                                      |
| `subproject_id`             | Integer                                                                                                                             |                                                          |                                                      |
| `subproject_name`           | String                                                                                                                              |                                                          |                                                      |
| `payment_method_name`       | String: one of cash, personal\_debit\_card, personal\_credit\_card, corporate\_debit\_card, corporate\_credit\_car, factorial\_card |                                                          |                                                      |
| `files_attached`            | Files                                                                                                                               |                                                          |                                                      |
| `document_number`           | Integer                                                                                                                             |                                                          |                                                      |
| `document_type`             | String: one of invoice, receipt, other                                                                                              |                                                          |                                                      |

### **Webhook URL**

* URLs where Factorial will send the webhook must be provided. One for production and another for the test environment
* This URL will be used for all companies using the integration.

### **Integration UUI**

* Factorial will provide the Partner with an `integration_uuid` That represents your integration across Factorial environments and is the shared integration identifier between both systems. You will need it in the following steps.

<Callout icon="📘" theme="info">
  Integration UUID is the same across Factorial's [Environments: production and demo](https://apidoc.factorialhr.com/docs/production-and-demo)
</Callout>

## 🔧 Setup integration for a new client

When a new client starts using the integration for the first time, some configuration may be required on the partner's side.

### 1. Set up data mappings

#### Compensations

* The partner can list the Payroll Concepts for a company by calling the following endpoint: [Read Compensation Concepts](/reference/compensations-concept)

**`GET {baseUrl}/api/{version}/resources/compensations/concepts`**

* It is important that the partner filters by
  * *categories*:
    * earnings\_fixed\_salary
    * earnings\_variable
    * earnings\_benefits\_in\_kind
    * earnings\_others
    * deductions
  * *with\_active\_status*: true

* Once the partner has the list of Payroll Concepts, they can ask the client to map them with the payroll concepts codes of their payroll software account.

#### Expenses

TBD

### 2. Notify Factorial about the new installation & set up

Once the setup is finished on the partner's side and the integration is ready to be used, it must be enabled in Factorial for that specific client (company) by calling the following endpoint:

[Create an Installation](/reference/post_api-2026-04-01-resources-marketplace-installations) Factorial Creates an Installation​

```http
 POST {baseUrl}/api/{version}/resources/marketplace/installations 
 
{
  "integration_uuid": string,  // your integration identifier
  "company_id": integer
}
```

## 🔄 Async Integration Flow

<Callout icon="❗️" theme="error">
  **Important**

  Please note all described steps are mandatory for the partner to be implemented.
</Callout>

### 1. Receive Webhook Notification

When a sync is triggered by the user in Factorial, Partners’ webhook will receive a `POST` request with the following payload:

```json
{
  "sync_run_id": integer,
  "integration_uuid": string,  // your integration identifier
  "company_id": integer
}
```

<Callout icon="❗️" theme="error">
  **Important**

  * Partners’ endpoint must respond with HTTP `200 OK` to confirm receipt.
  * The partner should process the sync **asynchronously**.
  * Partner **should not** return errors in this response — errors must be handled and reported separately in Step 4.
  * If a webhook notification fails, Factorial will send an email to the partner and **retry the notification up to 5 times within 15 minutes**. If all retries fail, the user will be notified that the sync was unsuccessful.
</Callout>

### 2. Fetch Sync Data

To retrieve the data items to sync, call the following endpoint:

[Reads all Syncable items](https://apidoc.factorialhr.com/reference/get_api-2026-04-01-resources-integrations-syncable-items)

**`GET {baseUrl}/api/{version}/resources/integrations/syncable_items?sync_run_id={n}`**

using the `sync_run_id` value received in the webhook payload.

The response will contain **a paginated list of all the data entries to sync**. You must use [Pagination](https://apidoc.factorialhr.com/docs/pagination) to get the full set of items.

**Example with Compensation data**

```json
{ 
  "data": [
    {
      "syncable_sync_run_id": 1,
      "syncable_type": "compensations/compensation",
      "sync_payload": {
        "employee_id": 8,
        "payroll_concept_id": 16,
        "amount": 50,
        "unit": "units",
        "effective_on": "2025-08-31",
        "employee_company_identifier": "23537657",
        "legal_entity_id": 5
      }
    },
    {
      "syncable_sync_run_id": 2,
      "syncable_type": "compensations/compensation",
      "sync_payload": {
        "employee_id": 6,
        "payroll_concept_id": 20,
        "amount": 5198, // Amount in cents (5198 -> 51.98)
        "unit": "money",
        "effective_on": "2025-08-31",
        "employee_company_identifier": "23456787",
        "legal_entity_id": 3
      }
    }
  ],
  "meta": {
    "has_next_page": true,
    "has_previous_page": false,
    "start_cursor": "MQ==",
    "end_cursor": "MTAw",
    "total": 869,
    "limit": 100
  }
}
```

![](https://files.readme.io/9a705c70ee0a066f34c0f7986ef1da480d60066ef612fb2959fc101c5806c2c4-image.png)

### 3. Process Sync Data

When processing the data, the partner is responsible for:

* **Performing the delta**:
  * The client may trigger the sync multiple times for the same period and company, potentially with different filters. These are **not concurrent**, but your system must ensure **idempotency** or manage updates accordingly.
* **Pushing data to the external system**:
  * Create or update items (compensations, expenses) in the external payroll provider based on the sync data.

<Callout icon="❗️" theme="error">
  Please clarify with Factorial how updates should be managed:

  *Should we overwrite previous values defined directly in the external system, or should a merge be done? (This depends on which system is the source of truth.)*
</Callout>

***

### 4. Report Sync Status

Once sync items are processed, the Partner needs to report the final status of each `syncable_sync_run` received in the step 2 back to Factorial by calling:

[Updates a Syncable sync run](https://apidoc.factorialhr.com/reference/put_api-2025-10-01-resources-integrations-syncable-sync-runs-id)

```
PUT {baseUrl}/api/{version}/resources/integrations/syncable_sync_runs/{id}

{
  "status": "success"| "failed" | "invalid",
  "error_messages": {
    "sycn_api_error": string,
    "sync_validation_error": string
      ...
    }
}
```

* Use `success` when the item was synced correctly to the external software.
* Use `failed` if something went wrong and the item was not synced.
* Use `invalid` if the data is structurally incorrect or missing required fields.
  * Example: Factorial sends you a compensation with a `payroll_concept_id` that you don’t have mapped with any code of the payroll software

<Callout icon="❗️" theme="error">
  One hour after the user starts the sync process, any items without a reported status will be marked as 'failed,' and the sync\_run will be updated to its corresponding final state.
</Callout>
