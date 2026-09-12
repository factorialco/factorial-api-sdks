from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesProjectManagementTimeRecordsUpdateObservationsBody")


@_attrs_define
class PostApi20261001ResourcesProjectManagementTimeRecordsUpdateObservationsBody:
    id: str
    """ Id of the time record """
    observations: str | Unset = UNSET
    """ Comment for the time record """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        observations = self.observations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if observations is not UNSET:
            field_dict["observations"] = observations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        observations = d.pop("observations", UNSET)

        post_api_20261001_resources_project_management_time_records_update_observations_body = cls(
            id=id,
            observations=observations,
        )

        post_api_20261001_resources_project_management_time_records_update_observations_body.additional_properties = d
        return post_api_20261001_resources_project_management_time_records_update_observations_body

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
