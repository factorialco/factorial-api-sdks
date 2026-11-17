from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_20270101_resources_compensations_payroll_results_bulk_create_body_results_item_items_item import (
        PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBodyResultsItemItemsItem,
    )


T = TypeVar(
    "T", bound="PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBodyResultsItem"
)


@_attrs_define
class PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBodyResultsItem:
    employee_id: str
    """ Employee id, refers to employees/employees endpoint. Must be part of the payroll run. """
    items: list[
        PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBodyResultsItemItemsItem
    ]
    """ One entry per payroll concept """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20270101_resources_compensations_payroll_results_bulk_create_body_results_item_items_item import (
            PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBodyResultsItemItemsItem,
        )

        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = PostApi20270101ResourcesCompensationsPayrollResultsBulkCreateBodyResultsItemItemsItem.from_dict(
                items_item_data
            )

            items.append(items_item)

        post_api_20270101_resources_compensations_payroll_results_bulk_create_body_results_item = (
            cls(
                employee_id=employee_id,
                items=items,
            )
        )

        post_api_20270101_resources_compensations_payroll_results_bulk_create_body_results_item.additional_properties = d
        return (
            post_api_20270101_resources_compensations_payroll_results_bulk_create_body_results_item
        )

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
