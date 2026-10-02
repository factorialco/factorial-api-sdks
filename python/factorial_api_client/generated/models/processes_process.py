from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.processes_process_category import ProcessesProcessCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessesProcess")


@_attrs_define
class ProcessesProcess:
    id: str
    """ identifier of the workflow. """
    name: str
    """ name of the workflow, as it reads in the product. """
    description: str | Unset = UNSET
    """ description of the workflow. """
    category: ProcessesProcessCategory | Unset = UNSET
    """ what the workflow is for: `onboarding`, `offboarding`, `training` or `custom`. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value if self.category is not None else None

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        _category = d.pop("category", UNSET)
        category: ProcessesProcessCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ProcessesProcessCategory(_category) if _category is not None else None

        processes_process = cls(
            id=id,
            name=name,
            description=description,
            category=category,
        )

        processes_process.additional_properties = d
        return processes_process

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
