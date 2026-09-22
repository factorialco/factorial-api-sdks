from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesTrainingsTrainingMembershipsBulkCreateBody")


@_attrs_define
class PostApi20261001ResourcesTrainingsTrainingMembershipsBulkCreateBody:
    training_id: str
    """ Training id to be assigned """
    employee_ids: list[str] | Unset = UNSET
    """ ids for the accesses to be assigned in a training """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        training_id = self.training_id

        employee_ids: list[str] | Unset = UNSET
        if not isinstance(self.employee_ids, Unset):
            employee_ids = self.employee_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "training_id": training_id,
            }
        )
        if employee_ids is not UNSET:
            field_dict["employee_ids"] = employee_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        training_id = d.pop("training_id")

        employee_ids = cast(list[str], d.pop("employee_ids", UNSET))

        post_api_20261001_resources_trainings_training_memberships_bulk_create_body = cls(
            training_id=training_id,
            employee_ids=employee_ids,
        )

        post_api_20261001_resources_trainings_training_memberships_bulk_create_body.additional_properties = d
        return post_api_20261001_resources_trainings_training_memberships_bulk_create_body

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
