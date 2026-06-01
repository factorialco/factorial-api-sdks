from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ats_application_phase_phase_type import AtsApplicationPhasePhaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AtsApplicationPhase")


@_attrs_define
class AtsApplicationPhase:
    id: int
    """ Identifier of the application Phase """
    ats_job_posting_id: int
    """ Job posting of the application phase """
    name: str
    """ Name of the application phase """
    position: int
    """ Position of the application phase """
    editable: bool
    """ If the application phase is editable """
    phase_type: AtsApplicationPhasePhaseType
    """ Application phase type """
    applications_count: int | Unset = UNSET
    """ Active application count """
    active_applications_count: int | Unset = UNSET
    ats_hiring_stage_id: int | Unset = UNSET
    """ Hiring stage identifier """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ats_job_posting_id = self.ats_job_posting_id

        name = self.name

        position = self.position

        editable = self.editable

        phase_type = self.phase_type.value

        applications_count = self.applications_count

        active_applications_count = self.active_applications_count

        ats_hiring_stage_id = self.ats_hiring_stage_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ats_job_posting_id": ats_job_posting_id,
                "name": name,
                "position": position,
                "editable": editable,
                "phase_type": phase_type,
            }
        )
        if applications_count is not UNSET:
            field_dict["applications_count"] = applications_count
        if active_applications_count is not UNSET:
            field_dict["active_applications_count"] = active_applications_count
        if ats_hiring_stage_id is not UNSET:
            field_dict["ats_hiring_stage_id"] = ats_hiring_stage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ats_job_posting_id = d.pop("ats_job_posting_id")

        name = d.pop("name")

        position = d.pop("position")

        editable = d.pop("editable")

        phase_type = AtsApplicationPhasePhaseType(d.pop("phase_type"))

        applications_count = d.pop("applications_count", UNSET)

        active_applications_count = d.pop("active_applications_count", UNSET)

        ats_hiring_stage_id = d.pop("ats_hiring_stage_id", UNSET)

        ats_application_phase = cls(
            id=id,
            ats_job_posting_id=ats_job_posting_id,
            name=name,
            position=position,
            editable=editable,
            phase_type=phase_type,
            applications_count=applications_count,
            active_applications_count=active_applications_count,
            ats_hiring_stage_id=ats_hiring_stage_id,
        )

        ats_application_phase.additional_properties = d
        return ats_application_phase

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
