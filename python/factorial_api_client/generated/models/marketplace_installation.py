from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MarketplaceInstallation")


@_attrs_define
class MarketplaceInstallation:
    id: str
    integration_uuid: str
    """ UUID of the integration """
    company_id: str
    """ Identifier of the company """
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        integration_uuid = self.integration_uuid

        company_id = self.company_id

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "integration_uuid": integration_uuid,
                "company_id": company_id,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        integration_uuid = d.pop("integration_uuid")

        company_id = d.pop("company_id")

        created_at = d.pop("created_at")

        marketplace_installation = cls(
            id=id,
            integration_uuid=integration_uuid,
            company_id=company_id,
            created_at=created_at,
        )

        marketplace_installation.additional_properties = d
        return marketplace_installation

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
