from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20260701_resources_trainings_sessions_id_body_schedule import (
    PutApi20260701ResourcesTrainingsSessionsIdBodySchedule,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260701ResourcesTrainingsSessionsIdBody")


@_attrs_define
class PutApi20260701ResourcesTrainingsSessionsIdBody:
    id: str
    """ The session id you want to update """
    name: str
    """ Session name """
    starts_at: str | Unset = UNSET
    """ Start date for the session, if scheduled, starts at and ends at needs to happen within the same day. """
    ends_at: str | Unset = UNSET
    """ End date for the session, if scheduled, starts at and ends at needs to happen within the same day. """
    due_date: str | Unset = UNSET
    """ Only necessary for self paced sessions. """
    duration: str | Unset = UNSET
    """ Duration in hours of the session """
    modality: str | Unset = UNSET
    """ Online, In person or mixed """
    schedule: PutApi20260701ResourcesTrainingsSessionsIdBodySchedule | Unset = UNSET
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
    send_calendar_invites: bool | Unset = UNSET
    """ Send calendar invites to attendees assigned to the session """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        starts_at = self.starts_at

        ends_at = self.ends_at

        due_date = self.due_date

        duration = self.duration

        modality = self.modality

        schedule: str | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.value

        link = self.link

        location = self.location

        subsidized = self.subsidized

        recurrent = self.recurrent

        send_calendar_invites = self.send_calendar_invites

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
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
        if send_calendar_invites is not UNSET:
            field_dict["send_calendar_invites"] = send_calendar_invites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        starts_at = d.pop("starts_at", UNSET)

        ends_at = d.pop("ends_at", UNSET)

        due_date = d.pop("due_date", UNSET)

        duration = d.pop("duration", UNSET)

        modality = d.pop("modality", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: PutApi20260701ResourcesTrainingsSessionsIdBodySchedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = PutApi20260701ResourcesTrainingsSessionsIdBodySchedule(_schedule) if _schedule is not None else None

        link = d.pop("link", UNSET)

        location = d.pop("location", UNSET)

        subsidized = d.pop("subsidized", UNSET)

        recurrent = d.pop("recurrent", UNSET)

        send_calendar_invites = d.pop("send_calendar_invites", UNSET)

        put_api_20260701_resources_trainings_sessions_id_body = cls(
            id=id,
            name=name,
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
            send_calendar_invites=send_calendar_invites,
        )

        put_api_20260701_resources_trainings_sessions_id_body.additional_properties = d
        return put_api_20260701_resources_trainings_sessions_id_body

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
