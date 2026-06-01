from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesTeamsTeamsIdBody")


@_attrs_define
class PutApi20260401ResourcesTeamsTeamsIdBody:
    id: int
    """ id of the team """
    name: str | Unset = UNSET
    """ name of the team """
    description: str | Unset = UNSET
    """ Description of the team """
    avatar: File | Unset = UNSET
    """ Avatar of the team """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        avatar: FileTypes | Unset = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _avatar = d.pop("avatar", UNSET)
        avatar: File | Unset
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = File(payload=BytesIO(_avatar))

        put_api_20260401_resources_teams_teams_id_body = cls(
            id=id,
            name=name,
            description=description,
            avatar=avatar,
        )

        put_api_20260401_resources_teams_teams_id_body.additional_properties = d
        return put_api_20260401_resources_teams_teams_id_body

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
