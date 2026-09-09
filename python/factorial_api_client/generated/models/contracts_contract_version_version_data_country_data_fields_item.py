from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractsContractVersionVersionDataCountryDataFieldsItem")


@_attrs_define
class ContractsContractVersionVersionDataCountryDataFieldsItem:
    name: str
    field_name: str
    value_id: str
    value_label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_name = self.field_name

        value_id = self.value_id

        value_label = self.value_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "field_name": field_name,
                "value_id": value_id,
            }
        )
        if value_label is not UNSET:
            field_dict["value_label"] = value_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        field_name = d.pop("field_name")

        value_id = d.pop("value_id")

        value_label = d.pop("value_label", UNSET)

        contracts_contract_version_version_data_country_data_fields_item = cls(
            name=name,
            field_name=field_name,
            value_id=value_id,
            value_label=value_label,
        )

        contracts_contract_version_version_data_country_data_fields_item.additional_properties = d
        return contracts_contract_version_version_data_country_data_fields_item

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
