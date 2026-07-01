from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesEmployeesEmployeesTerminateBody")


@_attrs_define
class PostApi20260701ResourcesEmployeesEmployeesTerminateBody:
    id: str
    """ id of the employee. """
    terminated_on: str
    """ when the employee will be terminated. """
    termination_reason: str | Unset = UNSET
    """ A reason for the termination. """
    termination_assigned_manager_id: str | Unset = UNSET
    """ id of manager that terminates the employee, you can get the manager_id from employees endpoint. """
    open_backfill: bool | Unset = UNSET
    """ When true, automatically opens a backfill position (vacancy or requisition) for the terminated employee.
    Requires ATS to be enabled with an automatic backfill setting configured. When false or omitted, no backfill is
    created. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        terminated_on = self.terminated_on

        termination_reason = self.termination_reason

        termination_assigned_manager_id = self.termination_assigned_manager_id

        open_backfill = self.open_backfill

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "terminated_on": terminated_on,
            }
        )
        if termination_reason is not UNSET:
            field_dict["termination_reason"] = termination_reason
        if termination_assigned_manager_id is not UNSET:
            field_dict["termination_assigned_manager_id"] = termination_assigned_manager_id
        if open_backfill is not UNSET:
            field_dict["open_backfill"] = open_backfill

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        terminated_on = d.pop("terminated_on")

        termination_reason = d.pop("termination_reason", UNSET)

        termination_assigned_manager_id = d.pop("termination_assigned_manager_id", UNSET)

        open_backfill = d.pop("open_backfill", UNSET)

        post_api_20260701_resources_employees_employees_terminate_body = cls(
            id=id,
            terminated_on=terminated_on,
            termination_reason=termination_reason,
            termination_assigned_manager_id=termination_assigned_manager_id,
            open_backfill=open_backfill,
        )

        post_api_20260701_resources_employees_employees_terminate_body.additional_properties = d
        return post_api_20260701_resources_employees_employees_terminate_body

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
