from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationsEmployeesLocation")


@_attrs_define
class LocationsEmployeesLocation:
    location_id: str
    """ The ID of the assigned workplace. """
    employee_id: str
    """ The ID of the employee assigned to the workplace. """
    is_default: bool
    """ Whether this assignment is the employee's default workplace. Use set_as_default to change it. """
    employees_location_work_area_ids: list[str]
    """ The IDs of the employee's work area assignments within this workplace. """
    id: str | Unset = UNSET
    """ The assignment ID, which differs from the workplace ID. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_id = self.location_id

        employee_id = self.employee_id

        is_default = self.is_default

        employees_location_work_area_ids = self.employees_location_work_area_ids

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location_id": location_id,
                "employee_id": employee_id,
                "is_default": is_default,
                "employees_location_work_area_ids": employees_location_work_area_ids,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location_id = d.pop("location_id")

        employee_id = d.pop("employee_id")

        is_default = d.pop("is_default")

        employees_location_work_area_ids = cast(
            list[str], d.pop("employees_location_work_area_ids")
        )

        id = d.pop("id", UNSET)

        locations_employees_location = cls(
            location_id=location_id,
            employee_id=employee_id,
            is_default=is_default,
            employees_location_work_area_ids=employees_location_work_area_ids,
            id=id,
        )

        locations_employees_location.additional_properties = d
        return locations_employees_location

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
