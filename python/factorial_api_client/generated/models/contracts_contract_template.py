from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractsContractTemplate")


@_attrs_define
class ContractsContractTemplate:
    id: int
    """ Unique identifier for the contract template """
    company_id: int | Unset = UNSET
    """ ID of the company this template belongs to """
    contract_version_type: str | Unset = UNSET
    """ Type of contract version (e.g., es for Spain, fr for France) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        contract_version_type = self.contract_version_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if contract_version_type is not UNSET:
            field_dict["contract_version_type"] = contract_version_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id", UNSET)

        contract_version_type = d.pop("contract_version_type", UNSET)

        contracts_contract_template = cls(
            id=id,
            company_id=company_id,
            contract_version_type=contract_version_type,
        )

        contracts_contract_template.additional_properties = d
        return contracts_contract_template

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
