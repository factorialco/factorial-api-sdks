from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsCountryDataInputsItem",
)


@_attrs_define
class PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetailsCountryDataInputsItem:
    field_name: str
    """ The templated field to set (e.g. contract_type). """
    value_id: str
    """ The id of the option to assign to the field. """
    integration_source: str | Unset = UNSET
    """ Only used when the option was sourced from an installed payroll integration (e.g. A3innuva). Leave unset for
    regular field inputs.
     """
    label: str | Unset = UNSET
    """ Only used together with integration_source, to label an option that does not yet exist locally. Leave unset
    for regular field inputs.
     """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        value_id = self.value_id

        integration_source = self.integration_source

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_name": field_name,
                "value_id": value_id,
            }
        )
        if integration_source is not UNSET:
            field_dict["integration_source"] = integration_source
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("field_name")

        value_id = d.pop("value_id")

        integration_source = d.pop("integration_source", UNSET)

        label = d.pop("label", UNSET)

        post_api_20261001_resources_contracts_legal_entity_changes_body_contract_details_country_data_inputs_item = cls(
            field_name=field_name,
            value_id=value_id,
            integration_source=integration_source,
            label=label,
        )

        post_api_20261001_resources_contracts_legal_entity_changes_body_contract_details_country_data_inputs_item.additional_properties = d
        return post_api_20261001_resources_contracts_legal_entity_changes_body_contract_details_country_data_inputs_item

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
