from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesProcessesMaterializedProcessesBody")


@_attrs_define
class PostApi20261001ResourcesProcessesMaterializedProcessesBody:
    company_id: str
    """ identifier of the company the workflow belongs to. """
    process_id: str
    """ identifier of the workflow to assign. Read /processes/processes to find it. """
    employee_id: str | Unset = UNSET
    """ identifier of the employee to assign, refers to the /employees/employees endpoint. The employee needs
    whatever the workflow's steps read about them — typically manager, team and contract — before being assigned; a
    step that cannot resolve them blocks until an admin unblocks it. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        process_id = self.process_id

        employee_id = self.employee_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_id": company_id,
                "process_id": process_id,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("company_id")

        process_id = d.pop("process_id")

        employee_id = d.pop("employee_id", UNSET)

        post_api_20261001_resources_processes_materialized_processes_body = cls(
            company_id=company_id,
            process_id=process_id,
            employee_id=employee_id,
        )

        post_api_20261001_resources_processes_materialized_processes_body.additional_properties = d
        return post_api_20261001_resources_processes_materialized_processes_body

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
