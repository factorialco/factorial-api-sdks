from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.finance_ledger_account_resource_balance_type import (
    FinanceLedgerAccountResourceBalanceType,
)
from ..models.finance_ledger_account_resource_resource_type import (
    FinanceLedgerAccountResourceResourceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FinanceLedgerAccountResource")


@_attrs_define
class FinanceLedgerAccountResource:
    id: str
    """ Factorial unique identifier. """
    resource_type: FinanceLedgerAccountResourceResourceType
    """ Ledger account resource type. """
    resource_id: str
    """ Factorial unique identifier of the resource associated to the ledger account resource. """
    account_id: str
    """ Factorial Ledger Account identifier. """
    updated_at: str
    """ Last time the resource was updated. """
    balance_type: FinanceLedgerAccountResourceBalanceType | Unset = UNSET
    """ Ledger account balance type. """
    external_id: str | Unset = UNSET
    """ External identifier. """
    legal_entity_id: str | Unset = UNSET
    """ Factorial unique identifier of the Legal entity. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resource_type = self.resource_type.value

        resource_id = self.resource_id

        account_id = self.account_id

        updated_at = self.updated_at

        balance_type: str | Unset = UNSET
        if not isinstance(self.balance_type, Unset):
            balance_type = self.balance_type.value if self.balance_type is not None else None

        external_id = self.external_id

        legal_entity_id = self.legal_entity_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "resource_type": resource_type,
                "resource_id": resource_id,
                "account_id": account_id,
                "updated_at": updated_at,
            }
        )
        if balance_type is not UNSET:
            field_dict["balance_type"] = balance_type
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        resource_type = FinanceLedgerAccountResourceResourceType(d.pop("resource_type"))

        resource_id = d.pop("resource_id")

        account_id = d.pop("account_id")

        updated_at = d.pop("updated_at")

        _balance_type = d.pop("balance_type", UNSET)
        balance_type: FinanceLedgerAccountResourceBalanceType | Unset
        if isinstance(_balance_type, Unset):
            balance_type = UNSET
        else:
            balance_type = FinanceLedgerAccountResourceBalanceType(_balance_type) if _balance_type is not None else None

        external_id = d.pop("external_id", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        finance_ledger_account_resource = cls(
            id=id,
            resource_type=resource_type,
            resource_id=resource_id,
            account_id=account_id,
            updated_at=updated_at,
            balance_type=balance_type,
            external_id=external_id,
            legal_entity_id=legal_entity_id,
        )

        finance_ledger_account_resource.additional_properties = d
        return finance_ledger_account_resource

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
