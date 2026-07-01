from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractsSpanishEducationLevel")


@_attrs_define
class ContractsSpanishEducationLevel:
    id: str
    """ Education level identifier """
    name: str
    """ education level name """
    default: bool | Unset = UNSET
    """ Whether the education level is a predefined value """
    contracts_contract_template_id: str | Unset = UNSET
    """ Contract template identifier, refers to contracts/contract_templates """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        default = self.default

        contracts_contract_template_id = self.contracts_contract_template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if contracts_contract_template_id is not UNSET:
            field_dict["contracts_contract_template_id"] = contracts_contract_template_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        default = d.pop("default", UNSET)

        contracts_contract_template_id = d.pop("contracts_contract_template_id", UNSET)

        contracts_spanish_education_level = cls(
            id=id,
            name=name,
            default=default,
            contracts_contract_template_id=contracts_contract_template_id,
        )

        contracts_spanish_education_level.additional_properties = d
        return contracts_spanish_education_level

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
