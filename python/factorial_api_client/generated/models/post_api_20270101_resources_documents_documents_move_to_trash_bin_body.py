from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20270101ResourcesDocumentsDocumentsMoveToTrashBinBody")


@_attrs_define
class PostApi20270101ResourcesDocumentsDocumentsMoveToTrashBinBody:
    document_ids: list[str]
    """ list of document identifiers. """
    deleted_by_id: str | Unset = UNSET
    """ access identifier recorded as the one who moved the documents to the trash bin, refers to
    /employees/employees endpoint. Required for API key requests; requests made on behalf of a user ignore it and
    record that user. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_ids = self.document_ids

        deleted_by_id = self.deleted_by_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document_ids": document_ids,
            }
        )
        if deleted_by_id is not UNSET:
            field_dict["deleted_by_id"] = deleted_by_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_ids = cast(list[str], d.pop("document_ids"))

        deleted_by_id = d.pop("deleted_by_id", UNSET)

        post_api_20270101_resources_documents_documents_move_to_trash_bin_body = cls(
            document_ids=document_ids,
            deleted_by_id=deleted_by_id,
        )

        post_api_20270101_resources_documents_documents_move_to_trash_bin_body.additional_properties = d
        return post_api_20270101_resources_documents_documents_move_to_trash_bin_body

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
