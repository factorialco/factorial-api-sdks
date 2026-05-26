from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobCatalogRole")


@_attrs_define
class JobCatalogRole:
    id: int
    """ identifier for the job catalog role. """
    company_id: int
    """ Identifier for the company. """
    name: str
    """ Role name. """
    legal_entities_ids: list[int]
    """ List of legal entities. """
    archived: bool
    """ Shows if the role is archived. """
    description: str | Unset = UNSET
    """ Role description. """
    supervisors_ids: list[int] | Unset = UNSET
    """ List of supervisors. """
    competencies_ids: list[int] | Unset = UNSET
    """ List of competencies. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        name = self.name

        legal_entities_ids = self.legal_entities_ids

        archived = self.archived

        description = self.description

        supervisors_ids: list[int] | Unset = UNSET
        if not isinstance(self.supervisors_ids, Unset):
            supervisors_ids = self.supervisors_ids

        competencies_ids: list[int] | Unset = UNSET
        if not isinstance(self.competencies_ids, Unset):
            competencies_ids = self.competencies_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "name": name,
                "legal_entities_ids": legal_entities_ids,
                "archived": archived,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if supervisors_ids is not UNSET:
            field_dict["supervisors_ids"] = supervisors_ids
        if competencies_ids is not UNSET:
            field_dict["competencies_ids"] = competencies_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        name = d.pop("name")

        legal_entities_ids = cast(list[int], d.pop("legal_entities_ids"))

        archived = d.pop("archived")

        description = d.pop("description", UNSET)

        supervisors_ids = cast(list[int], d.pop("supervisors_ids", UNSET))

        competencies_ids = cast(list[int], d.pop("competencies_ids", UNSET))

        job_catalog_role = cls(
            id=id,
            company_id=company_id,
            name=name,
            legal_entities_ids=legal_entities_ids,
            archived=archived,
            description=description,
            supervisors_ids=supervisors_ids,
            competencies_ids=competencies_ids,
        )

        job_catalog_role.additional_properties = d
        return job_catalog_role

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
