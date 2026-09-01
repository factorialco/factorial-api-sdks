from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesFinanceCostCentersEditBody")


@_attrs_define
class PostApi20261001ResourcesFinanceCostCentersEditBody:
    id: str
    """ Id of the cost center to edit. """
    name: str | Unset = UNSET
    """ New name of the cost center. """
    code: str | Unset = UNSET
    """ New code of the cost center. """
    description: str | Unset = UNSET
    """ New description of the cost center. """
    company_id: str | Unset = UNSET
    """ Deprecated and unused; the company is derived from the authenticated credentials. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        code = self.code

        description = self.description

        company_id = self.company_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if company_id is not UNSET:
            field_dict["company_id"] = company_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        company_id = d.pop("company_id", UNSET)

        post_api_20261001_resources_finance_cost_centers_edit_body = cls(
            id=id,
            name=name,
            code=code,
            description=description,
            company_id=company_id,
        )

        post_api_20261001_resources_finance_cost_centers_edit_body.additional_properties = d
        return post_api_20261001_resources_finance_cost_centers_edit_body

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
