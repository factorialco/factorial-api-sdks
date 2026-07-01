from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260701ResourcesItManagementItAssetModelsIdBody")


@_attrs_define
class PutApi20260701ResourcesItManagementItAssetModelsIdBody:
    id: str
    """ IT Asset Model identifier """
    type_name: str
    """ Type name of the IT asset model. Possible values are 'laptop', 'desktop', 'tablet', 'phone', 'screen',
    'mouse', 'keyboard', 'headset', 'other' """
    brand: str
    """ Brand of the IT asset model """
    name: str
    """ Name/model of the IT asset model """
    company_id: str | Unset = UNSET
    """ Company identifier """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_name = self.type_name

        brand = self.brand

        name = self.name

        company_id = self.company_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type_name": type_name,
                "brand": brand,
                "name": name,
            }
        )
        if company_id is not UNSET:
            field_dict["company_id"] = company_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_name = d.pop("type_name")

        brand = d.pop("brand")

        name = d.pop("name")

        company_id = d.pop("company_id", UNSET)

        put_api_20260701_resources_it_management_it_asset_models_id_body = cls(
            id=id,
            type_name=type_name,
            brand=brand,
            name=name,
            company_id=company_id,
        )

        put_api_20260701_resources_it_management_it_asset_models_id_body.additional_properties = d
        return put_api_20260701_resources_it_management_it_asset_models_id_body

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
