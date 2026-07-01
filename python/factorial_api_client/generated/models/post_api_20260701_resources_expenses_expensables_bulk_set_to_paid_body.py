from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20260701ResourcesExpensesExpensablesBulkSetToPaidBody")


@_attrs_define
class PostApi20260701ResourcesExpensesExpensablesBulkSetToPaidBody:
    ids: list[str]
    """ The IDs of the expensables to set to paid """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))

        post_api_20260701_resources_expenses_expensables_bulk_set_to_paid_body = cls(
            ids=ids,
        )

        post_api_20260701_resources_expenses_expensables_bulk_set_to_paid_body.additional_properties = d
        return post_api_20260701_resources_expenses_expensables_bulk_set_to_paid_body

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
