from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItManagementItAsset")


@_attrs_define
class ItManagementItAsset:
    id: str
    """ IT Asset identifier """
    company_id: int
    """ Company identifier """
    it_asset_model_id: str
    """ IT Asset Model identifier """
    serial_number: str
    """ Serial number of the IT asset """
    status: str
    """ Status of the IT asset. Possible values:
    - `assigned`: Asset is assigned to an employee
    - `in_stock`: Asset is available in inventory
    - `maintenance`: Asset is under maintenance or repair
    - `retired`: Asset has been retired or decommissioned

    Note: Not all status transitions are allowed. For example, an asset cannot be directly changed from `assigned`
    or `in_stock` to certain other statuses without proper workflow validation.
     """
    created_at: str
    """ Creation date of the IT asset """
    updated_at: str
    """ Last update date of the IT asset """
    owner_id: int | Unset = UNSET
    """ Owner (employee) identifier """
    location_id: int | Unset = UNSET
    """ Location identifier """
    workplace_id: int | Unset = UNSET
    """ Workplace identifier """
    team_id: int | Unset = UNSET
    """ Team identifier """
    purchase_date: str | Unset = UNSET
    """ Purchase date of the IT asset """
    purchase_price_cents: int | Unset = UNSET
    """ Purchase price in cents """
    currency: str | Unset = UNSET
    """ Currency of the purchase price """
    warranty_end_date: str | Unset = UNSET
    """ Warranty end date of the IT asset """
    label: str | Unset = UNSET
    """ Label of the IT asset """
    notes: str | Unset = UNSET
    """ Notes about the IT asset """
    discarded_at: str | Unset = UNSET
    """ Timestamp when the IT asset was soft deleted """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        it_asset_model_id = self.it_asset_model_id

        serial_number = self.serial_number

        status = self.status

        created_at = self.created_at

        updated_at = self.updated_at

        owner_id = self.owner_id

        location_id = self.location_id

        workplace_id = self.workplace_id

        team_id = self.team_id

        purchase_date = self.purchase_date

        purchase_price_cents = self.purchase_price_cents

        currency = self.currency

        warranty_end_date = self.warranty_end_date

        label = self.label

        notes = self.notes

        discarded_at = self.discarded_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "it_asset_model_id": it_asset_model_id,
                "serial_number": serial_number,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if workplace_id is not UNSET:
            field_dict["workplace_id"] = workplace_id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if purchase_date is not UNSET:
            field_dict["purchase_date"] = purchase_date
        if purchase_price_cents is not UNSET:
            field_dict["purchase_price_cents"] = purchase_price_cents
        if currency is not UNSET:
            field_dict["currency"] = currency
        if warranty_end_date is not UNSET:
            field_dict["warranty_end_date"] = warranty_end_date
        if label is not UNSET:
            field_dict["label"] = label
        if notes is not UNSET:
            field_dict["notes"] = notes
        if discarded_at is not UNSET:
            field_dict["discarded_at"] = discarded_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        it_asset_model_id = d.pop("it_asset_model_id")

        serial_number = d.pop("serial_number")

        status = d.pop("status")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        owner_id = d.pop("owner_id", UNSET)

        location_id = d.pop("location_id", UNSET)

        workplace_id = d.pop("workplace_id", UNSET)

        team_id = d.pop("team_id", UNSET)

        purchase_date = d.pop("purchase_date", UNSET)

        purchase_price_cents = d.pop("purchase_price_cents", UNSET)

        currency = d.pop("currency", UNSET)

        warranty_end_date = d.pop("warranty_end_date", UNSET)

        label = d.pop("label", UNSET)

        notes = d.pop("notes", UNSET)

        discarded_at = d.pop("discarded_at", UNSET)

        it_management_it_asset = cls(
            id=id,
            company_id=company_id,
            it_asset_model_id=it_asset_model_id,
            serial_number=serial_number,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            owner_id=owner_id,
            location_id=location_id,
            workplace_id=workplace_id,
            team_id=team_id,
            purchase_date=purchase_date,
            purchase_price_cents=purchase_price_cents,
            currency=currency,
            warranty_end_date=warranty_end_date,
            label=label,
            notes=notes,
            discarded_at=discarded_at,
        )

        it_management_it_asset.additional_properties = d
        return it_management_it_asset

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
