from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.goals_target_period_current_status import GoalsTargetPeriodCurrentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="GoalsTargetPeriod")


@_attrs_define
class GoalsTargetPeriod:
    id: str
    goal_id: str
    starts_on: str
    ends_on: str
    start_value: float
    current_value: float
    current_status: GoalsTargetPeriodCurrentStatus
    derived: bool
    target_value: float | Unset = UNSET
    current_value_id: str | Unset = UNSET
    progress_percentage: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        goal_id = self.goal_id

        starts_on = self.starts_on

        ends_on = self.ends_on

        start_value = self.start_value

        current_value = self.current_value

        current_status = self.current_status.value

        derived = self.derived

        target_value = self.target_value

        current_value_id = self.current_value_id

        progress_percentage = self.progress_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "goal_id": goal_id,
                "starts_on": starts_on,
                "ends_on": ends_on,
                "start_value": start_value,
                "current_value": current_value,
                "current_status": current_status,
                "derived": derived,
            }
        )
        if target_value is not UNSET:
            field_dict["target_value"] = target_value
        if current_value_id is not UNSET:
            field_dict["current_value_id"] = current_value_id
        if progress_percentage is not UNSET:
            field_dict["progress_percentage"] = progress_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        goal_id = d.pop("goal_id")

        starts_on = d.pop("starts_on")

        ends_on = d.pop("ends_on")

        start_value = d.pop("start_value")

        current_value = d.pop("current_value")

        current_status = GoalsTargetPeriodCurrentStatus(d.pop("current_status"))

        derived = d.pop("derived")

        target_value = d.pop("target_value", UNSET)

        current_value_id = d.pop("current_value_id", UNSET)

        progress_percentage = d.pop("progress_percentage", UNSET)

        goals_target_period = cls(
            id=id,
            goal_id=goal_id,
            starts_on=starts_on,
            ends_on=ends_on,
            start_value=start_value,
            current_value=current_value,
            current_status=current_status,
            derived=derived,
            target_value=target_value,
            current_value_id=current_value_id,
            progress_percentage=progress_percentage,
        )

        goals_target_period.additional_properties = d
        return goals_target_period

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
