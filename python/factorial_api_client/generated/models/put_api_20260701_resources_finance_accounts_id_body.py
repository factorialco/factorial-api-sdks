from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20260701_resources_finance_accounts_id_body_type import (
    PutApi20260701ResourcesFinanceAccountsIdBodyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260701ResourcesFinanceAccountsIdBody")


@_attrs_define
class PutApi20260701ResourcesFinanceAccountsIdBody:
    id: str
    """ Unique identifier in factorial for the ledger account """
    name: str | Unset = UNSET
    """ Name of the ledger account """
    number: str | Unset = UNSET
    """ Number of the ledger account """
    type_: PutApi20260701ResourcesFinanceAccountsIdBodyType | Unset = UNSET
    """ Type of the ledger account """
    currency: str | Unset = UNSET
    """ Currency of the ledger account """
    legal_entity_id: str | Unset = UNSET
    """ Legal entity ID of the ledger account """
    external_id: str | Unset = UNSET
    """ Id of the ledger account on the external system """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        number = self.number

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value if self.type_ is not None else None

        currency = self.currency

        legal_entity_id = self.legal_entity_id

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if type_ is not UNSET:
            field_dict["type"] = type_
        if currency is not UNSET:
            field_dict["currency"] = currency
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        number = d.pop("number", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PutApi20260701ResourcesFinanceAccountsIdBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PutApi20260701ResourcesFinanceAccountsIdBodyType(_type_) if _type_ is not None else None

        currency = d.pop("currency", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        external_id = d.pop("external_id", UNSET)

        put_api_20260701_resources_finance_accounts_id_body = cls(
            id=id,
            name=name,
            number=number,
            type_=type_,
            currency=currency,
            legal_entity_id=legal_entity_id,
            external_id=external_id,
        )

        put_api_20260701_resources_finance_accounts_id_body.additional_properties = d
        return put_api_20260701_resources_finance_accounts_id_body

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
