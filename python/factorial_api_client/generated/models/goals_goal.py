from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.goals_goal_frequency import GoalsGoalFrequency
from ..models.goals_goal_measure_type import GoalsGoalMeasureType
from ..models.goals_goal_status import GoalsGoalStatus
from ..models.goals_goal_tracking import GoalsGoalTracking
from ..types import UNSET, Unset

T = TypeVar("T", bound="GoalsGoal")


@_attrs_define
class GoalsGoal:
    id: str
    title: str
    author_id: str
    start_on: str
    end_on: str
    tracking: GoalsGoalTracking
    """ how the goal's progress is tracked, either by hand (manual) or derived from its sub-goals (sub_goals) """
    progress_percentage: float
    """ how far the goal is towards its target, from 0 upwards (100 means achieved) """
    status: GoalsGoalStatus
    """ where the goal stands today, worked out from its progress and end date (not_started, on_track, achieved or
    missed) """
    descendant_ids: list[str]
    updated_at: str
    frequency: GoalsGoalFrequency | Unset = UNSET
    """ how often the goal's attainment is measured (yearly, half_yearly, quarterly or monthly) """
    measure_type: GoalsGoalMeasureType | Unset = UNSET
    """ what the goal measures (currency, numeric, percentage, qualitative or sub_goal); for a goal tracked by sub-
    goals, the type its sub-goals share """
    parent_id: str | Unset = UNSET
    """ id of the goal this goal is a sub-goal of. Null for top-level goals """
    description: str | Unset = UNSET
    """ free text explaining the goal """
    performance_agreement_id: str | Unset = UNSET
    performance_agreement_action_item_uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        author_id = self.author_id

        start_on = self.start_on

        end_on = self.end_on

        tracking = self.tracking.value

        progress_percentage = self.progress_percentage

        status = self.status.value

        descendant_ids = self.descendant_ids

        updated_at = self.updated_at

        frequency: str | Unset = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value if self.frequency is not None else None

        measure_type: str | Unset = UNSET
        if not isinstance(self.measure_type, Unset):
            measure_type = self.measure_type.value if self.measure_type is not None else None

        parent_id = self.parent_id

        description = self.description

        performance_agreement_id = self.performance_agreement_id

        performance_agreement_action_item_uuid = self.performance_agreement_action_item_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "author_id": author_id,
                "start_on": start_on,
                "end_on": end_on,
                "tracking": tracking,
                "progress_percentage": progress_percentage,
                "status": status,
                "descendant_ids": descendant_ids,
                "updated_at": updated_at,
            }
        )
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if measure_type is not UNSET:
            field_dict["measure_type"] = measure_type
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if description is not UNSET:
            field_dict["description"] = description
        if performance_agreement_id is not UNSET:
            field_dict["performance_agreement_id"] = performance_agreement_id
        if performance_agreement_action_item_uuid is not UNSET:
            field_dict["performance_agreement_action_item_uuid"] = (
                performance_agreement_action_item_uuid
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        author_id = d.pop("author_id")

        start_on = d.pop("start_on")

        end_on = d.pop("end_on")

        tracking = GoalsGoalTracking(d.pop("tracking"))

        progress_percentage = d.pop("progress_percentage")

        status = GoalsGoalStatus(d.pop("status"))

        descendant_ids = cast(list[str], d.pop("descendant_ids"))

        updated_at = d.pop("updated_at")

        _frequency = d.pop("frequency", UNSET)
        frequency: GoalsGoalFrequency | Unset
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = GoalsGoalFrequency(_frequency) if _frequency is not None else None

        _measure_type = d.pop("measure_type", UNSET)
        measure_type: GoalsGoalMeasureType | Unset
        if isinstance(_measure_type, Unset):
            measure_type = UNSET
        else:
            measure_type = GoalsGoalMeasureType(_measure_type) if _measure_type is not None else None

        parent_id = d.pop("parent_id", UNSET)

        description = d.pop("description", UNSET)

        performance_agreement_id = d.pop("performance_agreement_id", UNSET)

        performance_agreement_action_item_uuid = d.pop(
            "performance_agreement_action_item_uuid", UNSET
        )

        goals_goal = cls(
            id=id,
            title=title,
            author_id=author_id,
            start_on=start_on,
            end_on=end_on,
            tracking=tracking,
            progress_percentage=progress_percentage,
            status=status,
            descendant_ids=descendant_ids,
            updated_at=updated_at,
            frequency=frequency,
            measure_type=measure_type,
            parent_id=parent_id,
            description=description,
            performance_agreement_id=performance_agreement_id,
            performance_agreement_action_item_uuid=performance_agreement_action_item_uuid,
        )

        goals_goal.additional_properties = d
        return goals_goal

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
