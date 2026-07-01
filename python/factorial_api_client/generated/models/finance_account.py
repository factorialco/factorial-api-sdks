from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.finance_account_type import FinanceAccountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FinanceAccount")


@_attrs_define
class FinanceAccount:
    id: str
    """ Unique identifier in factorial for the ledger account """
    legal_entity_id: str
    """ Legal entity ID of the ledger account """
    number: str
    """ Number of the ledger account """
    disabled: bool
    """ Whether the ledger account is disabled """
    type_: FinanceAccountType
    """ Type of the ledger account """
    updated_at: str
    """ Last updated date of the ledger account """
    name: str | Unset = UNSET
    """ Name of the ledger account """
    external_id: str | Unset = UNSET
    """ Id of the ledger account on the external system """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        legal_entity_id = self.legal_entity_id

        number = self.number

        disabled = self.disabled

        type_ = self.type_.value

        updated_at = self.updated_at

        name = self.name

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "legal_entity_id": legal_entity_id,
                "number": number,
                "disabled": disabled,
                "type": type_,
                "updated_at": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        legal_entity_id = d.pop("legal_entity_id")

        number = d.pop("number")

        disabled = d.pop("disabled")

        type_ = FinanceAccountType(d.pop("type"))

        updated_at = d.pop("updated_at")

        name = d.pop("name", UNSET)

        external_id = d.pop("external_id", UNSET)

        finance_account = cls(
            id=id,
            legal_entity_id=legal_entity_id,
            number=number,
            disabled=disabled,
            type_=type_,
            updated_at=updated_at,
            name=name,
            external_id=external_id,
        )

        finance_account.additional_properties = d
        return finance_account

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
