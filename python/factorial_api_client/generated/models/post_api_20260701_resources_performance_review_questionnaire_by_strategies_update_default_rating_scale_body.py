from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="PostApi20260701ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScaleBody",
)


@_attrs_define
class PostApi20260701ResourcesPerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScaleBody:
    performance_review_process_id: str
    """ Review process ID """
    default_rating_scale: list[Any]
    """ ###### **What should each range object look like?**

      - `value`: Range value (0 to 10)
      - `text`: Range description """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        performance_review_process_id = self.performance_review_process_id

        default_rating_scale = self.default_rating_scale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "performance_review_process_id": performance_review_process_id,
                "default_rating_scale": default_rating_scale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        performance_review_process_id = d.pop("performance_review_process_id")

        default_rating_scale = cast(list[Any], d.pop("default_rating_scale"))

        post_api_20260701_resources_performance_review_questionnaire_by_strategies_update_default_rating_scale_body = cls(
            performance_review_process_id=performance_review_process_id,
            default_rating_scale=default_rating_scale,
        )

        post_api_20260701_resources_performance_review_questionnaire_by_strategies_update_default_rating_scale_body.additional_properties = d
        return post_api_20260701_resources_performance_review_questionnaire_by_strategies_update_default_rating_scale_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
