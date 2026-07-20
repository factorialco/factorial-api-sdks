# F::PerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_process_id** | **String** | Review process ID |  |
| **strategy** | **String** | Reviewer strategy to update the questionnaire for |  |
| **questionnaire_content** | **Array&lt;Object&gt;** | List of grouped questions to be evaluated by the reviewer. ###### **What should each group object look like?**    - &#x60;uuid&#x60;: Unique identifier for the group   - &#x60;type&#x60;: Group type (&#x60;section&#x60; or &#x60;question&#x60;). If it&#39;s &#x60;section&#x60;, the questions will be grouped under a section with a given title   - &#x60;section_title&#x60;: Title of the section (optional)   - &#x60;questions&#x60;: List of questions  ###### **What should each question object look like?**    - &#x60;uuid&#x60;: Unique identifier for the question   - &#x60;mandatory&#x60;: Whether the question is mandatory or not   - &#x60;with_comment&#x60;: Whether the reviewer can add a comment or not   - &#x60;title&#x60;: Question   - &#x60;answer_type&#x60;: Answer type (&#x60;text&#x60;, &#x60;rating&#x60;, &#x60;number&#x60; or &#x60;multiple_choice&#x60;)   - &#x60;max_choices&#x60;: Maximum number of choices. If &#x60;1&#x60;, it&#39;ll be a single choice question   - &#x60;choice_options&#x60;: List of options for single and multiple choice questions |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyPostRequest.new(
  performance_review_process_id: 1,
  strategy: manager,
  questionnaire_content: [{&quot;uuid&quot;:&quot;b69c9b4d-0aa6-4ada-89d5-5fdcb04c1327&quot;,&quot;type&quot;:&quot;section&quot;,&quot;section_title&quot;:&quot;Performance&quot;,&quot;questions&quot;:[{&quot;uuid&quot;:&quot;a347a2fd-1a0a-4eee-b6c8-f74be63624fb&quot;,&quot;mandatory&quot;:true,&quot;with_comment&quot;:true,&quot;title&quot;:&quot;How would you rate the commitment of the employee?&quot;,&quot;answer_type&quot;:&quot;rating&quot;},{&quot;uuid&quot;:&quot;a922bd33-e9c8-4856-87c6-92eb895f4271&quot;,&quot;mandatory&quot;:true,&quot;with_comment&quot;:false,&quot;title&quot;:&quot;What are the strengths of the employee?&quot;,&quot;answer_type&quot;:&quot;text&quot;}]},{&quot;uuid&quot;:&quot;26f26623-043f-4110-a5cb-1fd54a69626f&quot;,&quot;type&quot;:&quot;question&quot;,&quot;questions&quot;:[{&quot;uuid&quot;:&quot;84ba99f3-4e4f-4917-a2af-6d0aa8c2e0f2&quot;,&quot;mandatory&quot;:true,&quot;with_comment&quot;:false,&quot;title&quot;:&quot;Do you think the employee is a team player?&quot;,&quot;answer_type&quot;:&quot;multiple_choice&quot;,&quot;max_choices&quot;:1,&quot;choice_options&quot;:[&quot;Yes&quot;,&quot;No&quot;]}]}]
)
```

