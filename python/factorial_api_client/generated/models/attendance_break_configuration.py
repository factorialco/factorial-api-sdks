from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttendanceBreakConfiguration")


@_attrs_define
class AttendanceBreakConfiguration:
    id: int
    attendance_employees_setting_id: int
    """ Id of the attendance employee setting """
    time_settings_break_configuration_id: int
    """ Id of the time settings break configuration """
    enabled: bool
    """ Status of the break configuration if enabled or not """
    name: str | Unset = UNSET
    """ Name of the break configuration """
    paid: bool | Unset = UNSET
    """ Check the break configuration is paid or not """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        attendance_employees_setting_id = self.attendance_employees_setting_id

        time_settings_break_configuration_id = self.time_settings_break_configuration_id

        enabled = self.enabled

        name = self.name

        paid = self.paid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "attendance_employees_setting_id": attendance_employees_setting_id,
                "time_settings_break_configuration_id": time_settings_break_configuration_id,
                "enabled": enabled,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if paid is not UNSET:
            field_dict["paid"] = paid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        attendance_employees_setting_id = d.pop("attendance_employees_setting_id")

        time_settings_break_configuration_id = d.pop("time_settings_break_configuration_id")

        enabled = d.pop("enabled")

        name = d.pop("name", UNSET)

        paid = d.pop("paid", UNSET)

        attendance_break_configuration = cls(
            id=id,
            attendance_employees_setting_id=attendance_employees_setting_id,
            time_settings_break_configuration_id=time_settings_break_configuration_id,
            enabled=enabled,
            name=name,
            paid=paid,
        )

        attendance_break_configuration.additional_properties = d
        return attendance_break_configuration

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
