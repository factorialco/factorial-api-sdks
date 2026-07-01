from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ItManagementItAssetModel")


@_attrs_define
class ItManagementItAssetModel:
    id: str
    """ IT Asset Model identifier """
    type_name: str
    """ Type name of the IT asset model. Possible values are 'laptop', 'desktop', 'tablet', 'phone', 'screen',
    'mouse', 'keyboard', 'headset', 'other' """
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_name = self.type_name

        company_id = self.company_id

        brand = self.brand

        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

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

        it_management_it_asset_model = cls(
            id=id,
            type_name=type_name,
            company_id=company_id,
            brand=brand,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
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
