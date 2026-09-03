from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_20261001_resources_ats_questions_id_body_options_item import (
        PutApi20261001ResourcesAtsQuestionsIdBodyOptionsItem,
    )


T = TypeVar("T", bound="PutApi20261001ResourcesAtsQuestionsIdBody")


@_attrs_define
class PutApi20261001ResourcesAtsQuestionsIdBody:
    id: str
    """ identifier of the question """
    label: str | Unset = UNSET
    """ text of the question """
    position: int | Unset = UNSET
    """ position of the question in the list """
    mandatory: bool | Unset = UNSET
    """ is the question mandatory or not """
    auto_disqualify: bool | Unset = UNSET
    """ if the question autodisqualifies the candidate depending on it's response. """
    options: list[PutApi20261001ResourcesAtsQuestionsIdBodyOptionsItem] | Unset = UNSET
    """ options for the question. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        position = self.position

        mandatory = self.mandatory

        auto_disqualify = self.auto_disqualify

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

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
        from ..models.put_api_20261001_resources_ats_questions_id_body_options_item import (
            PutApi20261001ResourcesAtsQuestionsIdBodyOptionsItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label", UNSET)

        position = d.pop("position", UNSET)

        mandatory = d.pop("mandatory", UNSET)

        auto_disqualify = d.pop("auto_disqualify", UNSET)

        _options = d.pop("options", UNSET)
        options: list[PutApi20261001ResourcesAtsQuestionsIdBodyOptionsItem] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = PutApi20261001ResourcesAtsQuestionsIdBodyOptionsItem.from_dict(
                    options_item_data
                )

                options.append(options_item)

        put_api_20261001_resources_ats_questions_id_body = cls(
            id=id,
            label=label,
            position=position,
            mandatory=mandatory,
            auto_disqualify=auto_disqualify,
            options=options,
        )

        put_api_20261001_resources_ats_questions_id_body.additional_properties = d
        return put_api_20261001_resources_ats_questions_id_body

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
