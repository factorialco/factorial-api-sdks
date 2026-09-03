from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PostApi20261001ResourcesFinanceCostCenterMembershipsBulkCreateUpdateBodyMembershipsItem",
)


@_attrs_define
class PostApi20261001ResourcesFinanceCostCenterMembershipsBulkCreateUpdateBodyMembershipsItem:
    cost_center_id: str
    start_date: str
    percentage: float
    id: str | Unset = UNSET
    end_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_center_id = self.cost_center_id

        start_date = self.start_date

        percentage = self.percentage

        id = self.id

        end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cost_center_id": cost_center_id,
                "start_date": start_date,
                "percentage": percentage,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_center_id = d.pop("cost_center_id")

        start_date = d.pop("start_date")

        percentage = d.pop("percentage")

        id = d.pop("id", UNSET)

        end_date = d.pop("end_date", UNSET)

        post_api_20261001_resources_finance_cost_center_memberships_bulk_create_update_body_memberships_item = cls(
            cost_center_id=cost_center_id,
            start_date=start_date,
            percentage=percentage,
            id=id,
            end_date=end_date,
        )

        post_api_20261001_resources_finance_cost_center_memberships_bulk_create_update_body_memberships_item.additional_properties = d
        return post_api_20261001_resources_finance_cost_center_memberships_bulk_create_update_body_memberships_item

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
