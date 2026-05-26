from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesAtsQuestionsIdBody")


@_attrs_define
class PutApi20260401ResourcesAtsQuestionsIdBody:
    id: int
    """ identifier of the question """
    label: str | Unset = UNSET
    """ text of the question """
    position: int | Unset = UNSET
    """ position of the question in the list """
    mandatory: bool | Unset = UNSET
    """ is the question mandatory or not """
    auto_disqualify: bool | Unset = UNSET
    """ if the question autodisqualifies the candidate depending on it's response. """
    options: list[Any] | Unset = UNSET
    """ options for the question. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        position = self.position

        mandatory = self.mandatory

        auto_disqualify = self.auto_disqualify

        options: list[Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if position is not UNSET:
            field_dict["position"] = position
        if mandatory is not UNSET:
            field_dict["mandatory"] = mandatory
        if auto_disqualify is not UNSET:
            field_dict["auto_disqualify"] = auto_disqualify
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label", UNSET)

        position = d.pop("position", UNSET)

        mandatory = d.pop("mandatory", UNSET)

        auto_disqualify = d.pop("auto_disqualify", UNSET)

        options = cast(list[Any], d.pop("options", UNSET))

        put_api_20260401_resources_ats_questions_id_body = cls(
            id=id,
            label=label,
            position=position,
            mandatory=mandatory,
            auto_disqualify=auto_disqualify,
            options=options,
        )

        put_api_20260401_resources_ats_questions_id_body.additional_properties = d
        return put_api_20260401_resources_ats_questions_id_body

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
