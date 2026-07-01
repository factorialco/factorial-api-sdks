from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinanceBudgetOption")


@_attrs_define
class FinanceBudgetOption:
    id: str
    """ Unique identifier for the budget option """
    name: str
    """ Name of the budget option """
    currency: str
    """ Currency of the budget option """
    legal_entity_id: str
    """ Legal entity ID of the budget option """
    description: str | Unset = UNSET
    """ Description of the budget option """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        currency = self.currency

        legal_entity_id = self.legal_entity_id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "currency": currency,
                "legal_entity_id": legal_entity_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        currency = d.pop("currency")

        legal_entity_id = d.pop("legal_entity_id")

        description = d.pop("description", UNSET)

        finance_budget_option = cls(
            id=id,
            name=name,
            currency=currency,
            legal_entity_id=legal_entity_id,
            description=description,
        )

        finance_budget_option.additional_properties = d
        return finance_budget_option

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
