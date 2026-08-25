from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trainings_session_modality import TrainingsSessionModality
from ..models.trainings_session_schedule import TrainingsSessionSchedule
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingsSession")


@_attrs_define
class TrainingsSession:
    id: int
    """ id of the session """
    name: str
    training_id: int
    """ Identifier of the course """
    subsidized: bool
    """ if the session is subsidized """
    description: str | Unset = UNSET
    """ Session description """
    training_class_id: str | Unset = UNSET
    """ Identifier of the group """
    starts_at: str | Unset = UNSET
    """ Date when the session should start """
    ends_at: str | Unset = UNSET
    """ Date when the session should end """
    due_date: str | Unset = UNSET
    """ Date when the session should end """
    duration: str | Unset = UNSET
    """ The duration in hours and minutes of the session """
    modality: TrainingsSessionModality | Unset = UNSET
    """ The mode the session will be handled, online, in person or hybrid. """
    schedule: TrainingsSessionSchedule | Unset = UNSET
    """ Session schedule information (scheduled, self-paced) """
    link: str | Unset = UNSET
    """ The link to see material from the session """
    location: str | Unset = UNSET
    """ The place where the session takes place """
    session_attendance_ids: list[int] | Unset = UNSET
    session_feedback_id: int | Unset = UNSET
    status: str | Unset = UNSET
    """ Status of the session """
    parent_id: int | Unset = UNSET
    """ Id of the recurrent session that is parent of the current one """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        training_id = self.training_id

        subsidized = self.subsidized

        description = self.description

        training_class_id = self.training_class_id

        starts_at = self.starts_at

        ends_at = self.ends_at

        due_date = self.due_date

        duration = self.duration

        modality: str | Unset = UNSET
        if not isinstance(self.modality, Unset):
            modality = self.modality.value if self.modality is not None else None

        schedule: str | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.value if self.schedule is not None else None

        link = self.link

        location = self.location

        session_attendance_ids: list[int] | Unset = UNSET
        if not isinstance(self.session_attendance_ids, Unset):
            session_attendance_ids = self.session_attendance_ids

        session_feedback_id = self.session_feedback_id

        status = self.status

        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "training_id": training_id,
                "subsidized": subsidized,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if training_class_id is not UNSET:
            field_dict["training_class_id"] = training_class_id
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if duration is not UNSET:
            field_dict["duration"] = duration
        if modality is not UNSET:
            field_dict["modality"] = modality
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if link is not UNSET:
            field_dict["link"] = link
        if location is not UNSET:
            field_dict["location"] = location
        if session_attendance_ids is not UNSET:
            field_dict["session_attendance_ids"] = session_attendance_ids
        if session_feedback_id is not UNSET:
            field_dict["session_feedback_id"] = session_feedback_id
        if status is not UNSET:
            field_dict["status"] = status
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        training_id = d.pop("training_id")

        subsidized = d.pop("subsidized")

        description = d.pop("description", UNSET)

        training_class_id = d.pop("training_class_id", UNSET)

        starts_at = d.pop("starts_at", UNSET)

        ends_at = d.pop("ends_at", UNSET)

        due_date = d.pop("due_date", UNSET)

        duration = d.pop("duration", UNSET)

        _modality = d.pop("modality", UNSET)
        modality: TrainingsSessionModality | Unset
        if isinstance(_modality, Unset):
            modality = UNSET
        else:
            modality = TrainingsSessionModality(_modality) if _modality is not None else None

        _schedule = d.pop("schedule", UNSET)
        schedule: TrainingsSessionSchedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = TrainingsSessionSchedule(_schedule) if _schedule is not None else None

        link = d.pop("link", UNSET)

        location = d.pop("location", UNSET)

        session_attendance_ids = cast(list[int], d.pop("session_attendance_ids", UNSET))

        session_feedback_id = d.pop("session_feedback_id", UNSET)

        status = d.pop("status", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        trainings_session = cls(
            id=id,
            name=name,
            training_id=training_id,
            subsidized=subsidized,
            description=description,
            training_class_id=training_class_id,
            starts_at=starts_at,
            ends_at=ends_at,
            due_date=due_date,
            duration=duration,
            modality=modality,
            schedule=schedule,
            link=link,
            location=location,
            session_attendance_ids=session_attendance_ids,
            session_feedback_id=session_feedback_id,
            status=status,
            parent_id=parent_id,
        )

        trainings_session.additional_properties = d
        return trainings_session

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
