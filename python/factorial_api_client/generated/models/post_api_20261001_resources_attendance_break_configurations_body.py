from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20261001ResourcesAttendanceBreakConfigurationsBody")


@_attrs_define
class PostApi20261001ResourcesAttendanceBreakConfigurationsBody:
    time_settings_break_configuration_id: str
    """ Id of the time settings break configuration """
    attendance_employees_setting_id: str
    """ Id of the attendance employee setting """
    enabled: bool
    """ Status of the break configuration if enabled or not """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_settings_break_configuration_id = self.time_settings_break_configuration_id

        attendance_employees_setting_id = self.attendance_employees_setting_id

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time_settings_break_configuration_id": time_settings_break_configuration_id,
                "attendance_employees_setting_id": attendance_employees_setting_id,
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time_settings_break_configuration_id = d.pop("time_settings_break_configuration_id")

        attendance_employees_setting_id = d.pop("attendance_employees_setting_id")

        enabled = d.pop("enabled")

        post_api_20261001_resources_attendance_break_configurations_body = cls(
            time_settings_break_configuration_id=time_settings_break_configuration_id,
            attendance_employees_setting_id=attendance_employees_setting_id,
            enabled=enabled,
        )

        post_api_20261001_resources_attendance_break_configurations_body.additional_properties = d
        return post_api_20261001_resources_attendance_break_configurations_body

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
