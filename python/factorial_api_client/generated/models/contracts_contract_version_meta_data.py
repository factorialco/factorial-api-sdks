from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractsContractVersionMetaData")


@_attrs_define
class ContractsContractVersionMetaData:
    contract_version_id: int
    """ identifier for the contract version. """
    action_type: str | Unset = UNSET
    """ the action that has been performed on the contract version ex:promotion / evolution / null. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contract_version_id = self.contract_version_id

        action_type = self.action_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contract_version_id": contract_version_id,
            }
        )
        if action_type is not UNSET:
            field_dict["action_type"] = action_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contract_version_id = d.pop("contract_version_id")

        action_type = d.pop("action_type", UNSET)

        contracts_contract_version_meta_data = cls(
            contract_version_id=contract_version_id,
            action_type=action_type,
        )

        contracts_contract_version_meta_data.additional_properties = d
        return contracts_contract_version_meta_data

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
