from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20261001ResourcesAttendanceReviewsBulkCreateBody")


@_attrs_define
class PostApi20261001ResourcesAttendanceReviewsBulkCreateBody:
    employee_ids: list[str]
    """ Employee identifiers to review """
    start_on: str
    """ Start date of the reviews """
    end_on: str
    """ End date of the reviews """
    reviewed_by: str
    """ Reviewed by employee identifier """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_ids = self.employee_ids

        start_on = self.start_on

        end_on = self.end_on

        reviewed_by = self.reviewed_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_ids": employee_ids,
                "start_on": start_on,
                "end_on": end_on,
                "reviewed_by": reviewed_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_ids = cast(list[str], d.pop("employee_ids"))

        start_on = d.pop("start_on")

        end_on = d.pop("end_on")

        reviewed_by = d.pop("reviewed_by")

        post_api_20261001_resources_attendance_reviews_bulk_create_body = cls(
            employee_ids=employee_ids,
            start_on=start_on,
            end_on=end_on,
            reviewed_by=reviewed_by,
        )

        post_api_20261001_resources_attendance_reviews_bulk_create_body.additional_properties = d
        return post_api_20261001_resources_attendance_reviews_bulk_create_body

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
