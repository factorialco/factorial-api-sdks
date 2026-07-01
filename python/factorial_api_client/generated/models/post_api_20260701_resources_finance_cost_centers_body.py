from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesFinanceCostCentersBody")


@_attrs_define
class PostApi20260701ResourcesFinanceCostCentersBody:
    name: str
    company_id: str
    legal_entity_id: str | Unset = UNSET
    code: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        company_id = self.company_id

        legal_entity_id = self.legal_entity_id

        code = self.code

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "company_id": company_id,
            }
        )
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        company_id = d.pop("company_id")

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        post_api_20260701_resources_finance_cost_centers_body = cls(
            name=name,
            company_id=company_id,
            legal_entity_id=legal_entity_id,
            code=code,
            description=description,
        )

        post_api_20260701_resources_finance_cost_centers_body.additional_properties = d
        return post_api_20260701_resources_finance_cost_centers_body

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
