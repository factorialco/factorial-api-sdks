from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_finance_cost_center_memberships_bulk_create_update_body_memberships_item import (
        PostApi20261001ResourcesFinanceCostCenterMembershipsBulkCreateUpdateBodyMembershipsItem,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesFinanceCostCenterMembershipsBulkCreateUpdateBody")


@_attrs_define
class PostApi20261001ResourcesFinanceCostCenterMembershipsBulkCreateUpdateBody:
    employee_id: str
    memberships: list[
        PostApi20261001ResourcesFinanceCostCenterMembershipsBulkCreateUpdateBodyMembershipsItem
    ]
    company_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        memberships = []
        for memberships_item_data in self.memberships:
            memberships_item = memberships_item_data.to_dict()
            memberships.append(memberships_item)

        company_id = self.company_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "memberships": memberships,
                "company_id": company_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_finance_cost_center_memberships_bulk_create_update_body_memberships_item import (
            PostApi20261001ResourcesFinanceCostCenterMembershipsBulkCreateUpdateBodyMembershipsItem,
        )

        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        memberships = []
        _memberships = d.pop("memberships")
        for memberships_item_data in _memberships:
            memberships_item = PostApi20261001ResourcesFinanceCostCenterMembershipsBulkCreateUpdateBodyMembershipsItem.from_dict(
                memberships_item_data
            )

            memberships.append(memberships_item)

        company_id = d.pop("company_id")

        post_api_20261001_resources_finance_cost_center_memberships_bulk_create_update_body = cls(
            employee_id=employee_id,
            memberships=memberships,
            company_id=company_id,
        )

        post_api_20261001_resources_finance_cost_center_memberships_bulk_create_update_body.additional_properties = d
        return post_api_20261001_resources_finance_cost_center_memberships_bulk_create_update_body

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
