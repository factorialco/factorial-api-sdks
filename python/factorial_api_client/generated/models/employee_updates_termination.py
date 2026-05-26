from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployeeUpdatesTermination")


@_attrs_define
class EmployeeUpdatesTermination:
    id: int
    status: str
    employee_id: int
    remaining_holidays: list[Any]
    terminated_on: str | Unset = UNSET
    termination_reason: str | Unset = UNSET
    termination_observations: str | Unset = UNSET
    legal_entity_id: int | Unset = UNSET
    termination_reason_type: str | Unset = UNSET
    termination_type_description: str | Unset = UNSET
    """ The description of the termination type. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        employee_id = self.employee_id

        remaining_holidays = self.remaining_holidays

        terminated_on = self.terminated_on

        termination_reason = self.termination_reason

        termination_observations = self.termination_observations

        legal_entity_id = self.legal_entity_id

        termination_reason_type = self.termination_reason_type

        termination_type_description = self.termination_type_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "employee_id": employee_id,
                "remaining_holidays": remaining_holidays,
            }
        )
        if terminated_on is not UNSET:
            field_dict["terminated_on"] = terminated_on
        if termination_reason is not UNSET:
            field_dict["termination_reason"] = termination_reason
        if termination_observations is not UNSET:
            field_dict["termination_observations"] = termination_observations
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if termination_reason_type is not UNSET:
            field_dict["termination_reason_type"] = termination_reason_type
        if termination_type_description is not UNSET:
            field_dict["termination_type_description"] = termination_type_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        employee_id = d.pop("employee_id")

        remaining_holidays = cast(list[Any], d.pop("remaining_holidays"))

        terminated_on = d.pop("terminated_on", UNSET)

        termination_reason = d.pop("termination_reason", UNSET)

        termination_observations = d.pop("termination_observations", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        termination_reason_type = d.pop("termination_reason_type", UNSET)

        termination_type_description = d.pop("termination_type_description", UNSET)

        employee_updates_termination = cls(
            id=id,
            status=status,
            employee_id=employee_id,
            remaining_holidays=remaining_holidays,
            terminated_on=terminated_on,
            termination_reason=termination_reason,
            termination_observations=termination_observations,
            legal_entity_id=legal_entity_id,
            termination_reason_type=termination_reason_type,
            termination_type_description=termination_type_description,
        )

        employee_updates_termination.additional_properties = d
        return employee_updates_termination

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
