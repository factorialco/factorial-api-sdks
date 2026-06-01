from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesDocumentsDocumentsIdBody")


@_attrs_define
class PutApi20260401ResourcesDocumentsDocumentsIdBody:
    id: int
    """ document identifiers. """
    public: bool
    """ flag to indicate if the document is public. """
    request_esignature: bool
    """ flag to indicate if the document requires an electronic signature. """
    signee_ids: list[int]
    """ list of user access identifiers associated to the document, refers to /employees/employees endpoint. """
    employee_id: int | Unset = UNSET
    """ employee identifier associated to the document. """
    folder_id: int | Unset = UNSET
    """ folder identifier, references to documents/folders endpoint. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        public = self.public

        request_esignature = self.request_esignature

        signee_ids = self.signee_ids

        employee_id = self.employee_id

        folder_id = self.folder_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "public": public,
                "request_esignature": request_esignature,
                "signee_ids": signee_ids,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if folder_id is not UNSET:
            field_dict["folder_id"] = folder_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        public = d.pop("public")

        request_esignature = d.pop("request_esignature")

        signee_ids = cast(list[int], d.pop("signee_ids"))

        employee_id = d.pop("employee_id", UNSET)

        folder_id = d.pop("folder_id", UNSET)

        put_api_20260401_resources_documents_documents_id_body = cls(
            id=id,
            public=public,
            request_esignature=request_esignature,
            signee_ids=signee_ids,
            employee_id=employee_id,
            folder_id=folder_id,
        )

        put_api_20260401_resources_documents_documents_id_body.additional_properties = d
        return put_api_20260401_resources_documents_documents_id_body

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
