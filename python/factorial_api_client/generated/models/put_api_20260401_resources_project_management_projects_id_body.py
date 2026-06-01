from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesProjectManagementProjectsIdBody")


@_attrs_define
class PutApi20260401ResourcesProjectManagementProjectsIdBody:
    id: int
    """ Id project. """
    name: str
    """ Name of the project. """
    code: str | Unset = UNSET
    """ Code for the project to be identifiable and searchable. """
    description: str | Unset = UNSET
    """ Description of the project. """
    start_date: str | Unset = UNSET
    """ Start date for the project. If given must be in iso-8601 format (YYYY-MM-DD). """
    due_date: str | Unset = UNSET
    """ Due date for the project. If given must be in iso-8601 format (YYYY-MM-DD). """
    client_id: int | Unset = UNSET
    """ Client associated to the project, refers to finance/contacts. """
    legal_entity_id: int | Unset = UNSET
    """ Id of the legal entity for the currency of the project """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        code = self.code

        description = self.description

        start_date = self.start_date

        due_date = self.due_date

        client_id = self.client_id

        legal_entity_id = self.legal_entity_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        start_date = d.pop("start_date", UNSET)

        due_date = d.pop("due_date", UNSET)

        client_id = d.pop("client_id", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        put_api_20260401_resources_project_management_projects_id_body = cls(
            id=id,
            name=name,
            code=code,
            description=description,
            start_date=start_date,
            due_date=due_date,
            client_id=client_id,
            legal_entity_id=legal_entity_id,
        )

        put_api_20260401_resources_project_management_projects_id_body.additional_properties = d
        return put_api_20260401_resources_project_management_projects_id_body

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
