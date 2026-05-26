from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MarketplaceInstallationSettings")


@_attrs_define
class MarketplaceInstallationSettings:
    leave_types: list[Any]
    """ Leave types codes """
    file_numbers: list[Any]
    """ Legal Entity file numbers """
    establishment_codes: list[Any]
    """ Workplace establishment codes """
    timeoff_allowance_code: list[Any]
    """ Timeoff allowance codes """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        leave_types = self.leave_types

        file_numbers = self.file_numbers

        establishment_codes = self.establishment_codes

        timeoff_allowance_code = self.timeoff_allowance_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "leave_types": leave_types,
                "file_numbers": file_numbers,
                "establishment_codes": establishment_codes,
                "timeoff_allowance_code": timeoff_allowance_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        leave_types = cast(list[Any], d.pop("leave_types"))

        file_numbers = cast(list[Any], d.pop("file_numbers"))

        establishment_codes = cast(list[Any], d.pop("establishment_codes"))

        timeoff_allowance_code = cast(list[Any], d.pop("timeoff_allowance_code"))

        marketplace_installation_settings = cls(
            leave_types=leave_types,
            file_numbers=file_numbers,
            establishment_codes=establishment_codes,
            timeoff_allowance_code=timeoff_allowance_code,
        )

        marketplace_installation_settings.additional_properties = d
        return marketplace_installation_settings

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
