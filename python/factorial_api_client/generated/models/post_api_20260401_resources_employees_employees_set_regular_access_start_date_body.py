from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesEmployeesEmployeesSetRegularAccessStartDateBody")


@_attrs_define
class PostApi20260401ResourcesEmployeesEmployeesSetRegularAccessStartDateBody:
    id: int
    """ id of the employee. """
    starts_on: str | Unset = UNSET
    """ the date the employee will start working in the company. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        starts_on = self.starts_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if starts_on is not UNSET:
            field_dict["starts_on"] = starts_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        starts_on = d.pop("starts_on", UNSET)

        post_api_20260401_resources_employees_employees_set_regular_access_start_date_body = cls(
            id=id,
            starts_on=starts_on,
        )

        post_api_20260401_resources_employees_employees_set_regular_access_start_date_body.additional_properties = d
        return post_api_20260401_resources_employees_employees_set_regular_access_start_date_body

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
