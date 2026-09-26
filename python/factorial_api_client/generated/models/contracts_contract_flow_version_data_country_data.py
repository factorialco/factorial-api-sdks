from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.contracts_contract_flow_version_data_country_data_fields_item import (
        ContractsContractFlowVersionDataCountryDataFieldsItem,
    )
    from ..models.contracts_contract_flow_version_data_country_data_template_fragments import (
        ContractsContractFlowVersionDataCountryDataTemplateFragments,
    )


T = TypeVar("T", bound="ContractsContractFlowVersionDataCountryData")


@_attrs_define
class ContractsContractFlowVersionDataCountryData:
    country: str
    """ Country code (e.g. es, fr, de, pt). """
    fields: list[ContractsContractFlowVersionDataCountryDataFieldsItem]
    template_fragments: ContractsContractFlowVersionDataCountryDataTemplateFragments
    """ Identifiers of the materialized_template_fragment records that produced this country data. After a legal
    entity change they are the target legal entity's fragments.
     """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        template_fragments = self.template_fragments.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country": country,
                "fields": fields,
                "template_fragments": template_fragments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contracts_contract_flow_version_data_country_data_fields_item import (
            ContractsContractFlowVersionDataCountryDataFieldsItem,
        )
        from ..models.contracts_contract_flow_version_data_country_data_template_fragments import (
            ContractsContractFlowVersionDataCountryDataTemplateFragments,
        )

        d = dict(src_dict)
        country = d.pop("country")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = ContractsContractFlowVersionDataCountryDataFieldsItem.from_dict(
                fields_item_data
            )

            fields.append(fields_item)

        template_fragments = ContractsContractFlowVersionDataCountryDataTemplateFragments.from_dict(
            d.pop("template_fragments")
        )

        contracts_contract_flow_version_data_country_data = cls(
            country=country,
            fields=fields,
            template_fragments=template_fragments,
        )

        contracts_contract_flow_version_data_country_data.additional_properties = d
        return contracts_contract_flow_version_data_country_data

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
