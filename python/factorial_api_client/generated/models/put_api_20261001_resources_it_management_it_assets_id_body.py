from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesItManagementItAssetsIdBody")


@_attrs_define
class PutApi20261001ResourcesItManagementItAssetsIdBody:
    id: str
    """ IT Asset identifier """
    it_asset_model_id: str | Unset = UNSET
    """ IT Asset Model identifier (Endpoints related to ItManagement/it_asset_models). """
    serial_number: str | Unset = UNSET
    """ Serial number of the IT asset """
    status: str | Unset = UNSET
    """ Status of the IT asset. Possible values:
    - `assigned`: Asset is assigned to an employee
    - `in_stock`: Asset is available in inventory
    - `maintenance`: Asset is under maintenance or repair
    - `retired`: Asset has been retired or decommissioned

    Note: Not all status transitions are allowed. For example, an asset cannot be directly changed from `assigned`
    or `in_stock` to certain other statuses without proper workflow validation.
     """
    owner_id: str | Unset = UNSET
    """ Owner (employee) identifier """
    location_id: str | Unset = UNSET
    """ Space identifier """
    workplace_id: str | Unset = UNSET
    """ Workplace identifier """
    team_id: str | Unset = UNSET
    """ Team identifier """
    purchase_date: str | Unset = UNSET
    """ Purchase date of the IT asset (YYYY-MM-DD) """
    purchase_price_cents: int | Unset = UNSET
    """ Purchase price in cents """
    currency: str | Unset = UNSET
    """ Currency of the purchase price """
    warranty_end_date: str | Unset = UNSET
    """ Warranty end date of the IT asset (YYYY-MM-DD) """
    label: str | Unset = UNSET
    """ Label of the IT asset """
    notes: str | Unset = UNSET
    """ Notes about the IT asset """
    company_id: str | Unset = UNSET
    """ Company identifier """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        it_asset_model_id = self.it_asset_model_id

        serial_number = self.serial_number

        status = self.status

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

        company_id = self.company_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if it_asset_model_id is not UNSET:
            field_dict["it_asset_model_id"] = it_asset_model_id
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if status is not UNSET:
            field_dict["status"] = status
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
        if company_id is not UNSET:
            field_dict["company_id"] = company_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        it_asset_model_id = d.pop("it_asset_model_id", UNSET)

        serial_number = d.pop("serial_number", UNSET)

        status = d.pop("status", UNSET)

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

        company_id = d.pop("company_id", UNSET)

        put_api_20261001_resources_it_management_it_assets_id_body = cls(
            id=id,
            it_asset_model_id=it_asset_model_id,
            serial_number=serial_number,
            status=status,
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
            company_id=company_id,
        )

        put_api_20261001_resources_it_management_it_assets_id_body.additional_properties = d
        return put_api_20261001_resources_it_management_it_assets_id_body

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
