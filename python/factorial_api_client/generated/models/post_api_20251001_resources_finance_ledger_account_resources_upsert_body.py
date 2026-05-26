from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20251001_resources_finance_ledger_account_resources_upsert_body_balance_type import (
    PostApi20251001ResourcesFinanceLedgerAccountResourcesUpsertBodyBalanceType,
)
from ..models.post_api_20251001_resources_finance_ledger_account_resources_upsert_body_operation_type import (
    PostApi20251001ResourcesFinanceLedgerAccountResourcesUpsertBodyOperationType,
)
from ..models.post_api_20251001_resources_finance_ledger_account_resources_upsert_body_resource_type import (
    PostApi20251001ResourcesFinanceLedgerAccountResourcesUpsertBodyResourceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesFinanceLedgerAccountResourcesUpsertBody")


@_attrs_define
class PostApi20251001ResourcesFinanceLedgerAccountResourcesUpsertBody:
    legal_entity_id: int
    """ Legal entity identifier. """
    resource_type: PostApi20251001ResourcesFinanceLedgerAccountResourcesUpsertBodyResourceType
    """ Ledger account resource type. """
    id: int | Unset = UNSET
    """ Factorial unique identifier. """
    name: str | Unset = UNSET
    """ Name of the ledger account resource. """
    number: str | Unset = UNSET
    """ Number of the ledger account resource. """
    external_id: str | Unset = UNSET
    """ External identifier. """
    account_id: int | Unset = UNSET
    """ Finance account identifier. """
    resource_id: int | Unset = UNSET
    """ Factorial unique identifier of the resource associated to the ledger account resource. """
    balance_type: (
        PostApi20251001ResourcesFinanceLedgerAccountResourcesUpsertBodyBalanceType | Unset
    ) = UNSET
    """ Ledger account balance type. """
    operation_type: (
        PostApi20251001ResourcesFinanceLedgerAccountResourcesUpsertBodyOperationType | Unset
    ) = UNSET
    """ Ledger account operation type. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legal_entity_id = self.legal_entity_id

        resource_type = self.resource_type.value

        id = self.id

        name = self.name

        number = self.number

        external_id = self.external_id

        account_id = self.account_id

        resource_id = self.resource_id

        balance_type: str | Unset = UNSET
        if not isinstance(self.balance_type, Unset):
            balance_type = self.balance_type.value

        operation_type: str | Unset = UNSET
        if not isinstance(self.operation_type, Unset):
            operation_type = self.operation_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "legal_entity_id": legal_entity_id,
                "resource_type": resource_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if balance_type is not UNSET:
            field_dict["balance_type"] = balance_type
        if operation_type is not UNSET:
            field_dict["operation_type"] = operation_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        legal_entity_id = d.pop("legal_entity_id")

        resource_type = PostApi20251001ResourcesFinanceLedgerAccountResourcesUpsertBodyResourceType(
            d.pop("resource_type")
        )

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        number = d.pop("number", UNSET)

        external_id = d.pop("external_id", UNSET)

        account_id = d.pop("account_id", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        _balance_type = d.pop("balance_type", UNSET)
        balance_type: (
            PostApi20251001ResourcesFinanceLedgerAccountResourcesUpsertBodyBalanceType | Unset
        )
        if isinstance(_balance_type, Unset):
            balance_type = UNSET
        else:
            balance_type = (
                PostApi20251001ResourcesFinanceLedgerAccountResourcesUpsertBodyBalanceType(
                    _balance_type
                )
            )

        _operation_type = d.pop("operation_type", UNSET)
        operation_type: (
            PostApi20251001ResourcesFinanceLedgerAccountResourcesUpsertBodyOperationType | Unset
        )
        if isinstance(_operation_type, Unset):
            operation_type = UNSET
        else:
            operation_type = (
                PostApi20251001ResourcesFinanceLedgerAccountResourcesUpsertBodyOperationType(
                    _operation_type
                )
            )

        post_api_20251001_resources_finance_ledger_account_resources_upsert_body = cls(
            legal_entity_id=legal_entity_id,
            resource_type=resource_type,
            id=id,
            name=name,
            number=number,
            external_id=external_id,
            account_id=account_id,
            resource_id=resource_id,
            balance_type=balance_type,
            operation_type=operation_type,
        )

        post_api_20251001_resources_finance_ledger_account_resources_upsert_body.additional_properties = d
        return post_api_20251001_resources_finance_ledger_account_resources_upsert_body

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
