from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PerformanceTargetManager")


@_attrs_define
class PerformanceTargetManager:
    id: str
    """ Manager employee ID """
    performance_review_process_id: str
    """ Review process ID """
    manager_access_id: str
    """ Manager access ID """
    manager_full_name: str
    """ Manager full name """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        performance_review_process_id = self.performance_review_process_id

        manager_access_id = self.manager_access_id

        manager_full_name = self.manager_full_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "performance_review_process_id": performance_review_process_id,
                "manager_access_id": manager_access_id,
                "manager_full_name": manager_full_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        performance_review_process_id = d.pop("performance_review_process_id")

        manager_access_id = d.pop("manager_access_id")

        manager_full_name = d.pop("manager_full_name")

        performance_target_manager = cls(
            id=id,
            performance_review_process_id=performance_review_process_id,
            manager_access_id=manager_access_id,
            manager_full_name=manager_full_name,
        )

        performance_target_manager.additional_properties = d
        return performance_target_manager

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
