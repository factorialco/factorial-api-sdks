from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MarketplaceInstallationSettingsPayrollConceptCodesItem")


@_attrs_define
class MarketplaceInstallationSettingsPayrollConceptCodesItem:
    legal_entity_id: str
    id: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legal_entity_id = self.legal_entity_id

        id = self.id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "legal_entity_id": legal_entity_id,
                "id": id,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        legal_entity_id = d.pop("legal_entity_id")

        id = d.pop("id")

        value = d.pop("value")

        marketplace_installation_settings_payroll_concept_codes_item = cls(
            legal_entity_id=legal_entity_id,
            id=id,
            value=value,
        )

        marketplace_installation_settings_payroll_concept_codes_item.additional_properties = d
        return marketplace_installation_settings_payroll_concept_codes_item

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
