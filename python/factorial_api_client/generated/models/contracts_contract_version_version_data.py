from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contracts_contract_version_version_data_country_data import (
        ContractsContractVersionVersionDataCountryData,
    )


T = TypeVar("T", bound="ContractsContractVersionVersionData")


@_attrs_define
class ContractsContractVersionVersionData:
    """Country-specific contract data (template fragments and fields).

    Example:
        {'country_data': {'country': 'es', 'fields': [{'name': 'contract_type', 'field_name': 'Tipo de contrato',
            'value_label': 'Indefinido', 'value_id': '1'}, {'name': 'working_hours', 'field_name': 'working_hours',
            'value_label': '40', 'value_id': '40'}], 'template_fragments': {'company_fragment_id': '1',
            'country_fragment_id': '2', 'legal_entity_fragment_id': '3'}}}

    """

    country_data: ContractsContractVersionVersionDataCountryData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country_data, Unset):
            country_data = self.country_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country_data is not UNSET:
            field_dict["country_data"] = country_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contracts_contract_version_version_data_country_data import (
            ContractsContractVersionVersionDataCountryData,
        )

        d = dict(src_dict)
        _country_data = d.pop("country_data", UNSET)
        country_data: ContractsContractVersionVersionDataCountryData | Unset
        if isinstance(_country_data, Unset):
            country_data = UNSET
        else:
            country_data = ContractsContractVersionVersionDataCountryData.from_dict(_country_data)

        contracts_contract_version_version_data = cls(
            country_data=country_data,
        )

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
