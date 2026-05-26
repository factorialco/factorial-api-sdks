from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinanceAccountingSetting")


@_attrs_define
class FinanceAccountingSetting:
    id: int
    """ Identifier for the AccountingSetting. """
    company_id: int
    """ ID of the associated Company. """
    legal_entity_id: int
    """ ID of the associated Legal Entity. """
    updated_at: str
    """ Timestamp when the accounting setting was last updated. """
    external_id: str | Unset = UNSET
    """ External ID for the accounting setting. """
    default_account_for_purchase_invoices_id: int | Unset = UNSET
    """ Default account for purchase invoices. """
    default_account_for_vendors_id: int | Unset = UNSET
    """ Default account for vendors. """
    default_account_for_banks_id: int | Unset = UNSET
    """ Default account for banks. """
    default_account_for_suspense_id: int | Unset = UNSET
    """ Default suspense account. """
    default_account_for_expenses_id: int | Unset = UNSET
    """ Default account for expenses. """
    default_account_for_employees_id: int | Unset = UNSET
    """ Default account for employees. """
    default_account_for_sale_invoices_id: int | Unset = UNSET
    """ Default account for sale invoices. """
    default_account_for_clients_id: int | Unset = UNSET
    """ Default account for clients. """
    default_account_for_benefits_id: int | Unset = UNSET
    """ Default account for benefits. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        legal_entity_id = self.legal_entity_id

        updated_at = self.updated_at

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
                "id": id,
                "company_id": company_id,
                "legal_entity_id": legal_entity_id,
                "updated_at": updated_at,
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
        id = d.pop("id")

        company_id = d.pop("company_id")

        legal_entity_id = d.pop("legal_entity_id")

        updated_at = d.pop("updated_at")

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

        finance_accounting_setting = cls(
            id=id,
            company_id=company_id,
            legal_entity_id=legal_entity_id,
            updated_at=updated_at,
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

        finance_accounting_setting.additional_properties = d
        return finance_accounting_setting

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
