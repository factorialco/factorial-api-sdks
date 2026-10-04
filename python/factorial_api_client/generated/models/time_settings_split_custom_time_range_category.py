from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_settings_split_custom_time_range_category_time_type import (
    TimeSettingsSplitCustomTimeRangeCategoryTimeType,
)

T = TypeVar("T", bound="TimeSettingsSplitCustomTimeRangeCategory")


@_attrs_define
class TimeSettingsSplitCustomTimeRangeCategory:
    id: str
    """ Split custom time range category identifier. """
    name: str
    """ The parent custom time range category's name (the split has no name of its own); combine with time_type to
    label the split, e.g. "Night work (overtime)". """
    time_type: TimeSettingsSplitCustomTimeRangeCategoryTimeType
    """ Whether the split covers regular or overtime work. """
    active: bool
    """ Whether the split is active, i.e. its parent category is not archived. """
    company_id: str
    """ Company the category belongs to. """
    custom_time_range_category_id: str
    """ Parent custom time range category this split belongs to. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        time_type = self.time_type.value

        active = self.active

        company_id = self.company_id

        custom_time_range_category_id = self.custom_time_range_category_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "time_type": time_type,
                "active": active,
                "company_id": company_id,
                "custom_time_range_category_id": custom_time_range_category_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        time_type = TimeSettingsSplitCustomTimeRangeCategoryTimeType(d.pop("time_type"))

        active = d.pop("active")

        company_id = d.pop("company_id")

        custom_time_range_category_id = d.pop("custom_time_range_category_id")

        time_settings_split_custom_time_range_category = cls(
            id=id,
            name=name,
            time_type=time_type,
            active=active,
            company_id=company_id,
            custom_time_range_category_id=custom_time_range_category_id,
        )

        time_settings_split_custom_time_range_category.additional_properties = d
        return time_settings_split_custom_time_range_category

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
