from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItManagementItAssetModel")


@_attrs_define
class ItManagementItAssetModel:
    id: str
    """ IT Asset Model identifier """
    type_name: str
    """ Deprecated: legacy IT-only type. Possible values are 'laptop', 'desktop', 'tablet', 'phone', 'screen',
    'mouse', 'keyboard', 'headset', 'other'. Use `subtype`/`asset_category_id` instead, which cover the full catalog
    (IT and beyond). """
    company_id: str
    """ Company identifier """
    brand: str
    """ Brand of the IT asset model """
    name: str
    """ Name/model of the IT asset """
    created_at: str
    """ Creation date of the IT asset model """
    updated_at: str
    """ Last update date of the IT asset model """
    asset_category_id: str | Unset = UNSET
    """ FK to the leaf AssetCategory (Subtype). NULL if not yet categorised. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_name = self.type_name

        company_id = self.company_id

        brand = self.brand

        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        asset_category_id = self.asset_category_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type_name": type_name,
                "company_id": company_id,
                "brand": brand,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if asset_category_id is not UNSET:
            field_dict["asset_category_id"] = asset_category_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_name = d.pop("type_name")

        company_id = d.pop("company_id")

        brand = d.pop("brand")

        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        asset_category_id = d.pop("asset_category_id", UNSET)

        it_management_it_asset_model = cls(
            id=id,
            type_name=type_name,
            company_id=company_id,
            brand=brand,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            asset_category_id=asset_category_id,
        )

        it_management_it_asset_model.additional_properties = d
        return it_management_it_asset_model

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
