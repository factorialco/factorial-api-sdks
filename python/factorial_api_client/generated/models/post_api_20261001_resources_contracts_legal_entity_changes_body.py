from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_contracts_legal_entity_changes_body_contract_details import (
        PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetails,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesContractsLegalEntityChangesBody")


@_attrs_define
class PostApi20261001ResourcesContractsLegalEntityChangesBody:
    target_legal_entity_id: str
    """ The legal entity the employee is moving to. A new contract and contract version are created under this legal
    entity. """
    contract_details: PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetails
    """ The terms of the contract version that opens the new contract. Same fields as the contract version create
    endpoint. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_legal_entity_id = self.target_legal_entity_id

        contract_details = self.contract_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_legal_entity_id": target_legal_entity_id,
                "contract_details": contract_details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_contracts_legal_entity_changes_body_contract_details import (
            PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetails,
        )

        d = dict(src_dict)
        target_legal_entity_id = d.pop("target_legal_entity_id")

        contract_details = (
            PostApi20261001ResourcesContractsLegalEntityChangesBodyContractDetails.from_dict(
                d.pop("contract_details")
            )
        )

        post_api_20261001_resources_contracts_legal_entity_changes_body = cls(
            target_legal_entity_id=target_legal_entity_id,
            contract_details=contract_details,
        )

        post_api_20261001_resources_contracts_legal_entity_changes_body.additional_properties = d
        return post_api_20261001_resources_contracts_legal_entity_changes_body

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
