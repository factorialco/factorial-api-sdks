from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesTrainingsTrainingMembershipsBulkDestroyBody")


@_attrs_define
class PostApi20260701ResourcesTrainingsTrainingMembershipsBulkDestroyBody:
    ids: list[str]
    """ IDs of training memberships to delete. When 'all' is true, these IDs are excluded from deletion. """
    training_id: str | Unset = UNSET
    """ Training ID. Required when 'all' is true to identify which training's memberships to delete. """
    all_: bool | Unset = UNSET
    """ When true, deletes all memberships for the given training_id, excluding those in the 'ids' array. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        training_id = self.training_id

        all_ = self.all_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
            }
        )
        if training_id is not UNSET:
            field_dict["training_id"] = training_id
        if all_ is not UNSET:
            field_dict["all"] = all_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))

        training_id = d.pop("training_id", UNSET)

        all_ = d.pop("all", UNSET)

        post_api_20260701_resources_trainings_training_memberships_bulk_destroy_body = cls(
            ids=ids,
            training_id=training_id,
            all_=all_,
        )

        post_api_20260701_resources_trainings_training_memberships_bulk_destroy_body.additional_properties = d
        return post_api_20260701_resources_trainings_training_memberships_bulk_destroy_body

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
