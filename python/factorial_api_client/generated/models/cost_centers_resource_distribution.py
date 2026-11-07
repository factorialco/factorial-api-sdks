from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CostCentersResourceDistribution")


@_attrs_define
class CostCentersResourceDistribution:
    resource_type: str
    """ Type of the record the row belongs to, as passed in the request """
    resource_id: str
    """ ID of the record the row belongs to. For an expense, this is its `expenses_expensable_id`. """
    cost_center_id: str
    """ ID of the cost center this share of the cost is charged to """
    percentage: float
    """ The cost center's share of the record's cost, as a fraction between 0 and 1, so 0.6 means 60%. The shares of
    a record normally add up to 1. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_type = self.resource_type

        resource_id = self.resource_id

        cost_center_id = self.cost_center_id

        percentage = self.percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_type": resource_type,
                "resource_id": resource_id,
                "cost_center_id": cost_center_id,
                "percentage": percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_type = d.pop("resource_type")

        resource_id = d.pop("resource_id")

        cost_center_id = d.pop("cost_center_id")

        percentage = d.pop("percentage")

        cost_centers_resource_distribution = cls(
            resource_type=resource_type,
            resource_id=resource_id,
            cost_center_id=cost_center_id,
            percentage=percentage,
        )

        cost_centers_resource_distribution.additional_properties = d
        return cost_centers_resource_distribution

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
