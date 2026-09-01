from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.performance_employee_score_scale_scale_item import (
        PerformanceEmployeeScoreScaleScaleItem,
    )


T = TypeVar("T", bound="PerformanceEmployeeScoreScale")


@_attrs_define
class PerformanceEmployeeScoreScale:
    id: str
    """ Employee score scale ID """
    scale: list[PerformanceEmployeeScoreScaleScaleItem]
    """ Scale to be used when scoring the employee performance """
    is_default: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        scale = []
        for scale_item_data in self.scale:
            scale_item = scale_item_data.to_dict()
            scale.append(scale_item)

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "scale": scale,
                "is_default": is_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_employee_score_scale_scale_item import (
            PerformanceEmployeeScoreScaleScaleItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        scale = []
        _scale = d.pop("scale")
        for scale_item_data in _scale:
            scale_item = PerformanceEmployeeScoreScaleScaleItem.from_dict(scale_item_data)

            scale.append(scale_item)

        is_default = d.pop("is_default")

        performance_employee_score_scale = cls(
            id=id,
            scale=scale,
            is_default=is_default,
        )

        performance_employee_score_scale.additional_properties = d
        return performance_employee_score_scale

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
