from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_20270101_resources_timeoff_allowance_incidences_bulk_update_body_allowance_incidences_item import (
        PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkUpdateBodyAllowanceIncidencesItem,
    )


T = TypeVar("T", bound="PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkUpdateBody")


@_attrs_define
class PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkUpdateBody:
    allowance_incidences: list[
        PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkUpdateBodyAllowanceIncidencesItem
    ]
    """ One patch per adjustment, at most 50 """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowance_incidences = []
        for allowance_incidences_item_data in self.allowance_incidences:
            allowance_incidences_item = allowance_incidences_item_data.to_dict()
            allowance_incidences.append(allowance_incidences_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowance_incidences": allowance_incidences,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20270101_resources_timeoff_allowance_incidences_bulk_update_body_allowance_incidences_item import (
            PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkUpdateBodyAllowanceIncidencesItem,
        )

        d = dict(src_dict)
        allowance_incidences = []
        _allowance_incidences = d.pop("allowance_incidences")
        for allowance_incidences_item_data in _allowance_incidences:
            allowance_incidences_item = PostApi20270101ResourcesTimeoffAllowanceIncidencesBulkUpdateBodyAllowanceIncidencesItem.from_dict(
                allowance_incidences_item_data
            )

            allowance_incidences.append(allowance_incidences_item)

        post_api_20270101_resources_timeoff_allowance_incidences_bulk_update_body = cls(
            allowance_incidences=allowance_incidences,
        )

        post_api_20270101_resources_timeoff_allowance_incidences_bulk_update_body.additional_properties = d
        return post_api_20270101_resources_timeoff_allowance_incidences_bulk_update_body

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
