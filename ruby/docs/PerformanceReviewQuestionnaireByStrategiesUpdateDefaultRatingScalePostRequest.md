# F::PerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScalePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_process_id** | **String** | Review process ID |  |
| **default_rating_scale** | **Array&lt;Object&gt;** | ###### **What should each range object look like?**    - &#x60;value&#x60;: Range value (0 to 10)   - &#x60;text&#x60;: Range description |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScalePostRequest.new(
  performance_review_process_id: 1,
  default_rating_scale: [{&quot;value&quot;:1,&quot;text&quot;:&quot;Poor&quot;},{&quot;value&quot;:2,&quot;text&quot;:&quot;Inconsistent&quot;},{&quot;value&quot;:3,&quot;text&quot;:&quot;Meets expectations&quot;},{&quot;value&quot;:4,&quot;text&quot;:&quot;Exceeds expectations&quot;},{&quot;value&quot;:5,&quot;text&quot;:&quot;Exceptional&quot;}]
)
```

