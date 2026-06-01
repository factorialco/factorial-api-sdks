from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingsSessionAccessMembership")


@_attrs_define
class TrainingsSessionAccessMembership:
    id: int
    """ ID of this membership """
    access_id: int
    """ ID of the access associated with this membership """
    session_id: int
    """ ID of the session associated with this membership """
    employee_id: int | Unset = UNSET
    """ ID of the employee associated with this membership """
    first_name: str | Unset = UNSET
    """ First name of the user associated with this membership """
    last_name: str | Unset = UNSET
    """ Last name of the user associated with this membership """
    job_title: str | Unset = UNSET
    """ Job title of the user associated with this membership """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        access_id = self.access_id

        session_id = self.session_id

        employee_id = self.employee_id

        first_name = self.first_name

        last_name = self.last_name

        job_title = self.job_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "access_id": access_id,
                "session_id": session_id,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if job_title is not UNSET:
            field_dict["job_title"] = job_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        access_id = d.pop("access_id")

        session_id = d.pop("session_id")

        employee_id = d.pop("employee_id", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        job_title = d.pop("job_title", UNSET)

        trainings_session_access_membership = cls(
            id=id,
            access_id=access_id,
            session_id=session_id,
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            job_title=job_title,
        )

        trainings_session_access_membership.additional_properties = d
        return trainings_session_access_membership

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
