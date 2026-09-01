from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20261001ResourcesItManagementItAssetModelsIdBody")


@_attrs_define
class PutApi20261001ResourcesItManagementItAssetModelsIdBody:
    id: str
    """ IT Asset Model identifier """
    brand: str
    """ Brand of the IT asset model """
    name: str
    """ Name/model of the IT asset model """
    type_name: str | Unset = UNSET
    """ Deprecated: legacy IT-only type. Possible values are 'laptop', 'desktop', 'tablet', 'phone', 'screen',
    'mouse', 'keyboard', 'headset', 'other'. Prefer `asset_category_id`, which covers the full catalog (IT and
    beyond). Ignored when `asset_category_id` is also given. """
    asset_category_id: str | Unset = UNSET
    """ ID of the asset subtype from the `it_management.asset_category` catalog (e.g. the id of 'vehicles.car').
    Takes precedence over `type_name` when both are given. """
    company_id: str | Unset = UNSET
    """ Company identifier """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        brand = self.brand

        name = self.name

        type_name = self.type_name

        asset_category_id = self.asset_category_id

        company_id = self.company_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "brand": brand,
                "name": name,
            }
        )
        if type_name is not UNSET:
            field_dict["type_name"] = type_name
        if asset_category_id is not UNSET:
            field_dict["asset_category_id"] = asset_category_id
        if company_id is not UNSET:
            field_dict["company_id"] = company_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        brand = d.pop("brand")

        name = d.pop("name")

        type_name = d.pop("type_name", UNSET)

        asset_category_id = d.pop("asset_category_id", UNSET)

        company_id = d.pop("company_id", UNSET)

        put_api_20261001_resources_it_management_it_asset_models_id_body = cls(
            id=id,
            brand=brand,
            name=name,
            type_name=type_name,
            asset_category_id=asset_category_id,
            company_id=company_id,
        )

        put_api_20261001_resources_it_management_it_asset_models_id_body.additional_properties = d
        return put_api_20261001_resources_it_management_it_asset_models_id_body

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
