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
    """ Id of the target period, or of the derived period of a goal tracked by its sub-goals """
    goal_id: str
    """ Id of the goal the period belongs to """
    starts_on: str
    """ First day of the period """
    ends_on: str
    """ Last day of the period """
    start_value: float
    """ Value of the goal when the period started """
    current_value: float
    """ Latest value recorded in the period """
    current_status: GoalsTargetPeriodCurrentStatus
    """ Status of the period, calculated from its progress and its end date """
    derived: bool
    """ True when the period is calculated from the sub-goals of the goal and has no row of its own """
    target_value: float | Unset = UNSET
    """ Target of the period, empty when the goal has no numeric target """
    current_value_id: str | Unset = UNSET
    """ Id of the latest value recorded in the period, empty for a derived period """
    progress_percentage: float | Unset = UNSET
    """ Progress towards the target, empty when the period has no target """
    updated_at: str | Unset = UNSET
    """ Last time the period changed, including when it was created and when its target changed. Empty for a derived
    period """
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

        updated_at = self.updated_at

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
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

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

        updated_at = d.pop("updated_at", UNSET)

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
            updated_at=updated_at,
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
