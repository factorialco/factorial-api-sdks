from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20270101ResourcesLocationsEmployeesLocationsBulkAssignBody")


@_attrs_define
class PostApi20270101ResourcesLocationsEmployeesLocationsBulkAssignBody:
    employee_id: str
    """ The ID of the employee whose workplaces will be replaced. """
    location_ids: list[str]
    """ The complete list of workplace IDs to retain, including the current default workplace. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_id = self.employee_id

        location_ids = self.location_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_id": employee_id,
                "location_ids": location_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_id = d.pop("employee_id")

        location_ids = cast(list[str], d.pop("location_ids"))

        post_api_20270101_resources_locations_employees_locations_bulk_assign_body = cls(
            employee_id=employee_id,
            location_ids=location_ids,
        )

        post_api_20270101_resources_locations_employees_locations_bulk_assign_body.additional_properties = d
        return post_api_20270101_resources_locations_employees_locations_bulk_assign_body

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
