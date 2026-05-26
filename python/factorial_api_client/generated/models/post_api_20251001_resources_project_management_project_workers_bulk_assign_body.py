from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesProjectManagementProjectWorkersBulkAssignBody")


@_attrs_define
class PostApi20251001ResourcesProjectManagementProjectWorkersBulkAssignBody:
    employee_ids: list[int]
    """ Set of a employee_ids that must be **assigned** after execution. """
    project_id: int | Unset = UNSET
    """ **DEPRECATED** in favor of `project_ids`. Please use `project_ids` instead """
    project_ids: list[int] | Unset = UNSET
    """ Set of project_ids to assign to the employees specified in the next param. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_ids = self.employee_ids

        project_id = self.project_id

        project_ids: list[int] | Unset = UNSET
        if not isinstance(self.project_ids, Unset):
            project_ids = self.project_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_ids": employee_ids,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if project_ids is not UNSET:
            field_dict["project_ids"] = project_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_ids = cast(list[int], d.pop("employee_ids"))

        project_id = d.pop("project_id", UNSET)

        project_ids = cast(list[int], d.pop("project_ids", UNSET))

        post_api_20251001_resources_project_management_project_workers_bulk_assign_body = cls(
            employee_ids=employee_ids,
            project_id=project_id,
            project_ids=project_ids,
        )

        post_api_20251001_resources_project_management_project_workers_bulk_assign_body.additional_properties = d
        return post_api_20251001_resources_project_management_project_workers_bulk_assign_body

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
