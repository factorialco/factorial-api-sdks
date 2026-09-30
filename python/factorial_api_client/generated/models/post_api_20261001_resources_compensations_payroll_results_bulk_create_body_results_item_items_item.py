from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="PostApi20261001ResourcesCompensationsPayrollResultsBulkCreateBodyResultsItemItemsItem",
)


@_attrs_define
class PostApi20261001ResourcesCompensationsPayrollResultsBulkCreateBodyResultsItemItemsItem:
    payroll_concept_id: str
    """ Payroll concept id, refers to compensations/concepts endpoint. """
    amount: int
    """ Signed amount in the concept's minor unit (cents for money concepts) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payroll_concept_id = self.payroll_concept_id

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payroll_concept_id": payroll_concept_id,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payroll_concept_id = d.pop("payroll_concept_id")

        amount = d.pop("amount")

        post_api_20261001_resources_compensations_payroll_results_bulk_create_body_results_item_items_item = cls(
            payroll_concept_id=payroll_concept_id,
            amount=amount,
        )

        post_api_20261001_resources_compensations_payroll_results_bulk_create_body_results_item_items_item.additional_properties = d
        return post_api_20261001_resources_compensations_payroll_results_bulk_create_body_results_item_items_item

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
