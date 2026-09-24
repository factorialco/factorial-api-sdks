from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketplaceInstallationSettingsLeaveTypesItem")


@_attrs_define
class MarketplaceInstallationSettingsLeaveTypesItem:
    id: str
    value: str
    forfait_jours: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value = self.value

        forfait_jours = self.forfait_jours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "value": value,
            }
        )
        if forfait_jours is not UNSET:
            field_dict["forfait_jours"] = forfait_jours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        value = d.pop("value")

        forfait_jours = d.pop("forfait_jours", UNSET)

        marketplace_installation_settings_leave_types_item = cls(
            id=id,
            value=value,
            forfait_jours=forfait_jours,
        )

        marketplace_installation_settings_leave_types_item.additional_properties = d
        return marketplace_installation_settings_leave_types_item

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
