from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20270101ResourcesTimeoffPoliciesBody")


@_attrs_define
class PostApi20270101ResourcesTimeoffPoliciesBody:
    name: str
    """ The name of the policy. """
    main: bool | Unset = UNSET
    """ If the policy is the main policy. """
    description: str | Unset = UNSET
    """ Policy description. """
    company_id: str | Unset = UNSET
    """ Company ID. """
    based_on_policy_id: str | Unset = UNSET
    """ ID of an existing policy to copy. When set, the new policy is created with a copy of that policy's
    allowances, without that policy's employees. Omit it to create a policy from scratch. """
    employee_ids: list[str] | Unset = UNSET
    """ IDs of the active employees to place on the new policy from today, in the same request. Omit it to create
    the policy with nobody on it. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        main = self.main

        description = self.description

        company_id = self.company_id

        based_on_policy_id = self.based_on_policy_id

        employee_ids: list[str] | Unset = UNSET
        if not isinstance(self.employee_ids, Unset):
            employee_ids = self.employee_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if main is not UNSET:
            field_dict["main"] = main
        if description is not UNSET:
            field_dict["description"] = description
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if based_on_policy_id is not UNSET:
            field_dict["based_on_policy_id"] = based_on_policy_id
        if employee_ids is not UNSET:
            field_dict["employee_ids"] = employee_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        main = d.pop("main", UNSET)

        description = d.pop("description", UNSET)

        company_id = d.pop("company_id", UNSET)

        based_on_policy_id = d.pop("based_on_policy_id", UNSET)

        employee_ids = cast(list[str], d.pop("employee_ids", UNSET))

        post_api_20270101_resources_timeoff_policies_body = cls(
            name=name,
            main=main,
            description=description,
            company_id=company_id,
            based_on_policy_id=based_on_policy_id,
            employee_ids=employee_ids,
        )

        post_api_20270101_resources_timeoff_policies_body.additional_properties = d
        return post_api_20270101_resources_timeoff_policies_body

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
