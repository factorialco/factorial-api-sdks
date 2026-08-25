from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260401_resources_trainings_sessions_body_modality import (
    PostApi20260401ResourcesTrainingsSessionsBodyModality,
)
from ..models.post_api_20260401_resources_trainings_sessions_body_schedule import (
    PostApi20260401ResourcesTrainingsSessionsBodySchedule,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesTrainingsSessionsBody")


@_attrs_define
class PostApi20260401ResourcesTrainingsSessionsBody:
    name: str
    """ Session name """
    training_id: int
    """ Training this session belongs to """
    description: str | Unset = UNSET
    """ Session specific description """
    training_class_id: int | Unset = UNSET
    """ Training class it belongs to """
    starts_at: str | Unset = UNSET
    """ Start date for the session, if scheduled, starts at and ends at needs to happen within the same day. """
    ends_at: str | Unset = UNSET
    """ End date for the session, if scheduled, starts at and ends at needs to happen within the same day. """
    due_date: str | Unset = UNSET
    """ Only necessary for self paced sessions. """
    duration: str | Unset = UNSET
    """ Duration in hours of the session """
    modality: PostApi20260401ResourcesTrainingsSessionsBodyModality | Unset = UNSET
    """ Online, In person or mixed """
    schedule: PostApi20260401ResourcesTrainingsSessionsBodySchedule | Unset = UNSET
    """ Scheduled or Self paced. Scheduled needs to have a start time and end time within the same day, self paced
    can start and end in different days and specific time won't be shown in the frontend app. """
    link: str | Unset = UNSET
    """ Link to join the session if it's online, or to access or download related material for the session. """
    location: str | Unset = UNSET
    """ Place where the session will happen if modality is mixed or in person. """
    subsidized: bool | Unset = UNSET
    """ Mark the session as subsidized """
    recurrent: bool | Unset = UNSET
    """ - """
    reminders: list[Any] | Unset = UNSET
    """ Session reminder notifications for those assigned to the session """
    send_calendar_invites: bool | Unset = UNSET
    """ Send calendar invites to attendees assigned to the session """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        training_id = self.training_id

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

        subsidized = self.subsidized

        recurrent = self.recurrent

        reminders: list[Any] | Unset = UNSET
        if not isinstance(self.reminders, Unset):
            reminders = self.reminders

        send_calendar_invites = self.send_calendar_invites

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "training_id": training_id,
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
        if subsidized is not UNSET:
            field_dict["subsidized"] = subsidized
        if recurrent is not UNSET:
            field_dict["recurrent"] = recurrent
        if reminders is not UNSET:
            field_dict["reminders"] = reminders
        if send_calendar_invites is not UNSET:
            field_dict["send_calendar_invites"] = send_calendar_invites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        training_id = d.pop("training_id")

        description = d.pop("description", UNSET)

        training_class_id = d.pop("training_class_id", UNSET)

        starts_at = d.pop("starts_at", UNSET)

        ends_at = d.pop("ends_at", UNSET)

        due_date = d.pop("due_date", UNSET)

        duration = d.pop("duration", UNSET)

        _modality = d.pop("modality", UNSET)
        modality: PostApi20260401ResourcesTrainingsSessionsBodyModality | Unset
        if isinstance(_modality, Unset):
            modality = UNSET
        else:
            modality = PostApi20260401ResourcesTrainingsSessionsBodyModality(_modality) if _modality is not None else None

        _schedule = d.pop("schedule", UNSET)
        schedule: PostApi20260401ResourcesTrainingsSessionsBodySchedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = PostApi20260401ResourcesTrainingsSessionsBodySchedule(_schedule) if _schedule is not None else None

        link = d.pop("link", UNSET)

        location = d.pop("location", UNSET)

        subsidized = d.pop("subsidized", UNSET)

        recurrent = d.pop("recurrent", UNSET)

        reminders = cast(list[Any], d.pop("reminders", UNSET))

        send_calendar_invites = d.pop("send_calendar_invites", UNSET)

        post_api_20260401_resources_trainings_sessions_body = cls(
            name=name,
            training_id=training_id,
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
            subsidized=subsidized,
            recurrent=recurrent,
            reminders=reminders,
            send_calendar_invites=send_calendar_invites,
        )

        post_api_20260401_resources_trainings_sessions_body.additional_properties = d
        return post_api_20260401_resources_trainings_sessions_body

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
