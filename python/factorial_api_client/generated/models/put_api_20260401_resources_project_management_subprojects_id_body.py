from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20260401_resources_project_management_subprojects_id_body_status import (
    PutApi20260401ResourcesProjectManagementSubprojectsIdBodyStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesProjectManagementSubprojectsIdBody")


@_attrs_define
class PutApi20260401ResourcesProjectManagementSubprojectsIdBody:
    id: int
    """ The id of the subproject. """
    name: str | Unset = UNSET
    """ The name of the subproject. """
    description: str | Unset = UNSET
    """ The description of the subproject. """
    status: PutApi20260401ResourcesProjectManagementSubprojectsIdBodyStatus | Unset = UNSET
    """ The status of the subproject. """
    code: str | Unset = UNSET
    """ The code of the subproject. """
    start_date: str | Unset = UNSET
    """ The start date of the subproject. """
    due_date: str | Unset = UNSET
    """ The due date of the subproject. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status is not None else None

        code = self.code

        start_date = self.start_date

        due_date = self.due_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if code is not UNSET:
            field_dict["code"] = code
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if due_date is not UNSET:
            field_dict["due_date"] = due_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _status = d.pop("status", UNSET)
        status: PutApi20260401ResourcesProjectManagementSubprojectsIdBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PutApi20260401ResourcesProjectManagementSubprojectsIdBodyStatus(_status) if _status is not None else None

        code = d.pop("code", UNSET)

        start_date = d.pop("start_date", UNSET)

        due_date = d.pop("due_date", UNSET)

        put_api_20260401_resources_project_management_subprojects_id_body = cls(
            id=id,
            name=name,
            description=description,
            status=status,
            code=code,
            start_date=start_date,
            due_date=due_date,
        )

        put_api_20260401_resources_project_management_subprojects_id_body.additional_properties = d
        return put_api_20260401_resources_project_management_subprojects_id_body

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
