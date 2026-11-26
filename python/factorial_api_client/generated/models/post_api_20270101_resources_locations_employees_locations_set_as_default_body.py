from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20270101ResourcesLocationsEmployeesLocationsSetAsDefaultBody")


@_attrs_define
class PostApi20270101ResourcesLocationsEmployeesLocationsSetAsDefaultBody:
    employees_location_id: str
    """ The assignment ID to make default, rather than the workplace ID. """
    employee_location_work_area_id: str | Unset = UNSET
    """ An optional work area assignment ID that belongs to this workplace assignment. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employees_location_id = self.employees_location_id

        employee_location_work_area_id = self.employee_location_work_area_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employees_location_id": employees_location_id,
            }
        )
        if employee_location_work_area_id is not UNSET:
            field_dict["employee_location_work_area_id"] = employee_location_work_area_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employees_location_id = d.pop("employees_location_id")

        employee_location_work_area_id = d.pop("employee_location_work_area_id", UNSET)

        post_api_20270101_resources_locations_employees_locations_set_as_default_body = cls(
            employees_location_id=employees_location_id,
            employee_location_work_area_id=employee_location_work_area_id,
        )

        post_api_20270101_resources_locations_employees_locations_set_as_default_body.additional_properties = d
        return post_api_20270101_resources_locations_employees_locations_set_as_default_body

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
