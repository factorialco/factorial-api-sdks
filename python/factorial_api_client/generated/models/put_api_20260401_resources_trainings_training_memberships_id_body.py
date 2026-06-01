from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesTrainingsTrainingMembershipsIdBody")


@_attrs_define
class PutApi20260401ResourcesTrainingsTrainingMembershipsIdBody:
    id: int
    """ Unique identifier for the training membership. Only used to identify the training membership to update. """
    training_completed_at: str | Unset = UNSET
    """ This field is used to record the date a training was completed for trainings that have an expiry date. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        training_completed_at = self.training_completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if training_completed_at is not UNSET:
            field_dict["training_completed_at"] = training_completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        training_completed_at = d.pop("training_completed_at", UNSET)

        put_api_20260401_resources_trainings_training_memberships_id_body = cls(
            id=id,
            training_completed_at=training_completed_at,
        )

        put_api_20260401_resources_trainings_training_memberships_id_body.additional_properties = d
        return put_api_20260401_resources_trainings_training_memberships_id_body

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
