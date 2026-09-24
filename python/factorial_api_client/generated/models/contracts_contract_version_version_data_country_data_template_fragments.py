from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractsContractVersionVersionDataCountryDataTemplateFragments")


@_attrs_define
class ContractsContractVersionVersionDataCountryDataTemplateFragments:
    """Identifiers of the materialized_template_fragment records that produced this country data. Compare against the
    current template's source_fragment_ids to detect when this data originated from a different template (e.g. after a
    legal entity or country change).

    """

    company_fragment_id: str | Unset = UNSET
    country_fragment_id: str | Unset = UNSET
    legal_entity_fragment_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_fragment_id = self.company_fragment_id

        country_fragment_id = self.country_fragment_id

        legal_entity_fragment_id = self.legal_entity_fragment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_fragment_id is not UNSET:
            field_dict["company_fragment_id"] = company_fragment_id
        if country_fragment_id is not UNSET:
            field_dict["country_fragment_id"] = country_fragment_id
        if legal_entity_fragment_id is not UNSET:
            field_dict["legal_entity_fragment_id"] = legal_entity_fragment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_fragment_id = d.pop("company_fragment_id", UNSET)

        country_fragment_id = d.pop("country_fragment_id", UNSET)

        legal_entity_fragment_id = d.pop("legal_entity_fragment_id", UNSET)

        contracts_contract_version_version_data_country_data_template_fragments = cls(
            company_fragment_id=company_fragment_id,
            country_fragment_id=country_fragment_id,
            legal_entity_fragment_id=legal_entity_fragment_id,
        )

        contracts_contract_version_version_data_country_data_template_fragments.additional_properties = d
        return contracts_contract_version_version_data_country_data_template_fragments

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
