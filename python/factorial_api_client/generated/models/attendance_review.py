from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AttendanceReview")


@_attrs_define
class AttendanceReview:
    id: str
    employee_id: str
    """ Employee identifier """
    date: str
    """ Date reviewed """
    reviewed_at: str
    """ Reviewed at (ISO 8601 format string) """
    author_id: str
    """ Author of the review """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        date = self.date

        reviewed_at = self.reviewed_at

        author_id = self.author_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "employee_id": employee_id,
                "date": date,
                "reviewed_at": reviewed_at,
                "author_id": author_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id")

        date = d.pop("date")

        reviewed_at = d.pop("reviewed_at")

        author_id = d.pop("author_id")

        attendance_review = cls(
            id=id,
            employee_id=employee_id,
            date=date,
            reviewed_at=reviewed_at,
            author_id=author_id,
        )

        attendance_review.additional_properties = d
        return attendance_review

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
