from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_management_imputable_project_status import (
    ProjectManagementImputableProjectStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectManagementImputableProject")


@_attrs_define
class ProjectManagementImputableProject:
    id: str
    """ The id of the imputable project """
    name: str
    """ The name of the imputable project """
    status: ProjectManagementImputableProjectStatus
    """ The status of the imputable project """
    currency: str
    """ The currency of the imputable project """
    code: str | Unset = UNSET
    """ The code of the imputable project """
    start_date: str | Unset = UNSET
    """ The start date of the imputable project """
    due_date: str | Unset = UNSET
    """ The due date of the imputable project """
    client_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status.value

        currency = self.currency

        code = self.code

        start_date = self.start_date

        due_date = self.due_date

        client_id = self.client_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "currency": currency,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if client_id is not UNSET:
            field_dict["client_id"] = client_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status = ProjectManagementImputableProjectStatus(d.pop("status"))

        currency = d.pop("currency")

        code = d.pop("code", UNSET)

        start_date = d.pop("start_date", UNSET)

        due_date = d.pop("due_date", UNSET)

        client_id = d.pop("client_id", UNSET)

        project_management_imputable_project = cls(
            id=id,
            name=name,
            status=status,
            currency=currency,
            code=code,
            start_date=start_date,
            due_date=due_date,
            client_id=client_id,
        )

        project_management_imputable_project.additional_properties = d
        return project_management_imputable_project

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
