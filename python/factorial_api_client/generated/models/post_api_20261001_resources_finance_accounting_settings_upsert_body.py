from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesFinanceAccountingSettingsUpsertBody")


@_attrs_define
class PostApi20261001ResourcesFinanceAccountingSettingsUpsertBody:
    legal_entity_id: str
    """ ID of the associated Legal Entity. """
    external_id: str | Unset = UNSET
    """ External ID for the accounting setting. """
    default_account_for_purchase_invoices_id: str | Unset = UNSET
    """ Default account for purchase invoices. """
    default_account_for_vendors_id: str | Unset = UNSET
    """ Default account for vendors. """
    default_account_for_banks_id: str | Unset = UNSET
    """ Default account for banks. """
    default_account_for_suspense_id: str | Unset = UNSET
    """ Default suspense account. """
    default_account_for_expenses_id: str | Unset = UNSET
    """ Default account for expenses. """
    default_account_for_employees_id: str | Unset = UNSET
    """ Default account for employees. """
    default_account_for_sale_invoices_id: str | Unset = UNSET
    """ Default account for sale invoices. """
    default_account_for_clients_id: str | Unset = UNSET
    """ Default account for clients. """
    default_account_for_benefits_id: str | Unset = UNSET
    """ Default account for benefits. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legal_entity_id = self.legal_entity_id

        external_id = self.external_id

        default_account_for_purchase_invoices_id = self.default_account_for_purchase_invoices_id

        default_account_for_vendors_id = self.default_account_for_vendors_id

        default_account_for_banks_id = self.default_account_for_banks_id

        default_account_for_suspense_id = self.default_account_for_suspense_id

        default_account_for_expenses_id = self.default_account_for_expenses_id

        default_account_for_employees_id = self.default_account_for_employees_id

        default_account_for_sale_invoices_id = self.default_account_for_sale_invoices_id

        default_account_for_clients_id = self.default_account_for_clients_id

        default_account_for_benefits_id = self.default_account_for_benefits_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "legal_entity_id": legal_entity_id,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if default_account_for_purchase_invoices_id is not UNSET:
            field_dict["default_account_for_purchase_invoices_id"] = (
                default_account_for_purchase_invoices_id
            )
        if default_account_for_vendors_id is not UNSET:
            field_dict["default_account_for_vendors_id"] = default_account_for_vendors_id
        if default_account_for_banks_id is not UNSET:
            field_dict["default_account_for_banks_id"] = default_account_for_banks_id
        if default_account_for_suspense_id is not UNSET:
            field_dict["default_account_for_suspense_id"] = default_account_for_suspense_id
        if default_account_for_expenses_id is not UNSET:
            field_dict["default_account_for_expenses_id"] = default_account_for_expenses_id
        if default_account_for_employees_id is not UNSET:
            field_dict["default_account_for_employees_id"] = default_account_for_employees_id
        if default_account_for_sale_invoices_id is not UNSET:
            field_dict["default_account_for_sale_invoices_id"] = (
                default_account_for_sale_invoices_id
            )
        if default_account_for_clients_id is not UNSET:
            field_dict["default_account_for_clients_id"] = default_account_for_clients_id
        if default_account_for_benefits_id is not UNSET:
            field_dict["default_account_for_benefits_id"] = default_account_for_benefits_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        legal_entity_id = d.pop("legal_entity_id")

        external_id = d.pop("external_id", UNSET)

        default_account_for_purchase_invoices_id = d.pop(
            "default_account_for_purchase_invoices_id", UNSET
        )

        default_account_for_vendors_id = d.pop("default_account_for_vendors_id", UNSET)

        default_account_for_banks_id = d.pop("default_account_for_banks_id", UNSET)

        default_account_for_suspense_id = d.pop("default_account_for_suspense_id", UNSET)

        default_account_for_expenses_id = d.pop("default_account_for_expenses_id", UNSET)

        default_account_for_employees_id = d.pop("default_account_for_employees_id", UNSET)

        default_account_for_sale_invoices_id = d.pop("default_account_for_sale_invoices_id", UNSET)

        default_account_for_clients_id = d.pop("default_account_for_clients_id", UNSET)

        default_account_for_benefits_id = d.pop("default_account_for_benefits_id", UNSET)

        post_api_20261001_resources_finance_accounting_settings_upsert_body = cls(
            legal_entity_id=legal_entity_id,
            external_id=external_id,
            default_account_for_purchase_invoices_id=default_account_for_purchase_invoices_id,
            default_account_for_vendors_id=default_account_for_vendors_id,
            default_account_for_banks_id=default_account_for_banks_id,
            default_account_for_suspense_id=default_account_for_suspense_id,
            default_account_for_expenses_id=default_account_for_expenses_id,
            default_account_for_employees_id=default_account_for_employees_id,
            default_account_for_sale_invoices_id=default_account_for_sale_invoices_id,
            default_account_for_clients_id=default_account_for_clients_id,
            default_account_for_benefits_id=default_account_for_benefits_id,
        )

        post_api_20261001_resources_finance_accounting_settings_upsert_body.additional_properties = d
        return post_api_20261001_resources_finance_accounting_settings_upsert_body

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
