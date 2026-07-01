from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ContractsContractVersionVersionData")


@_attrs_define
class ContractsContractVersionVersionData:
    """Country-specific contract data (template fragments and fields).

    Example:
        {'country_data': {'country': 'es', 'fields': [{'name': 'contract_type', 'field_name': 'Tipo de contrato',
            'value_label': 'Indefinido', 'value_id': '1'}, {'name': 'working_hours', 'field_name': 'working_hours',
            'value_label': '40', 'value_id': '40'}]}}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contracts_contract_version_version_data = cls()

        contracts_contract_version_version_data.additional_properties = d
        return contracts_contract_version_version_data

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
