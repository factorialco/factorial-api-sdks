from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApi20260701ResourcesAtsApplicationsMoveToPhaseBody")


@_attrs_define
class PostApi20260701ResourcesAtsApplicationsMoveToPhaseBody:
    id: str
    """ Application id to move """
    ats_application_phase_id: str
    """ Target application phase id. Must belong to the same job posting as the application. Refers to
    ats/application_phases. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ats_application_phase_id = self.ats_application_phase_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ats_application_phase_id": ats_application_phase_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ats_application_phase_id = d.pop("ats_application_phase_id")

        post_api_20260701_resources_ats_applications_move_to_phase_body = cls(
            id=id,
            ats_application_phase_id=ats_application_phase_id,
        )

        post_api_20260701_resources_ats_applications_move_to_phase_body.additional_properties = d
        return post_api_20260701_resources_ats_applications_move_to_phase_body

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
