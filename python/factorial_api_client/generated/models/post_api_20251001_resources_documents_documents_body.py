from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.post_api_20251001_resources_documents_documents_body_space import (
    PostApi20251001ResourcesDocumentsDocumentsBodySpace,
)
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesDocumentsDocumentsBody")


@_attrs_define
class PostApi20251001ResourcesDocumentsDocumentsBody:
    public: bool
    """ flag to indicate if the document is public. """
    space: PostApi20251001ResourcesDocumentsDocumentsBodySpace
    """ document space, in case of employee_my_documents it's necessary to fill employee_id. """
    is_pending_assignment: bool
    """ flag that indicates if the document is pending assignment. """
    file: File
    """ file to upload, the binary file. """
    author_id: int
    """ access identifier of the author, refers to /employees/employees endpoint. """
    company_id: int
    """ company identifier, refers to /api/me endpoint. """
    signee_ids: list[int]
    """ list of user access identifiers associated to the document, refers to /employees/employees endpoint. """
    request_esignature: bool
    """ flag to indicate if the document requires an electronic signature. """
    folder_id: int | Unset = UNSET
    """ folder identifier, references to documents/folders endpoint. """
    file_filename: str | Unset = UNSET
    """ final name of the file, even if the file has been uploaded with a different name. """
    leave_id: int | Unset = UNSET
    """ leave identifier associated to the document, refers to /timeoff/leaves endpoint. """
    employee_id: int | Unset = UNSET
    """ employee identifier associated to the document. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public = self.public

        space = self.space.value

        is_pending_assignment = self.is_pending_assignment

        file = self.file.to_tuple()

        author_id = self.author_id

        company_id = self.company_id

        signee_ids = self.signee_ids

        request_esignature = self.request_esignature

        folder_id = self.folder_id

        file_filename = self.file_filename

        leave_id = self.leave_id

        employee_id = self.employee_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public": public,
                "space": space,
                "is_pending_assignment": is_pending_assignment,
                "file": file,
                "author_id": author_id,
                "company_id": company_id,
                "signee_ids[]": signee_ids,
                "request_esignature": request_esignature,
            }
        )
        if folder_id is not UNSET:
            field_dict["folder_id"] = folder_id
        if file_filename is not UNSET:
            field_dict["file_filename"] = file_filename
        if leave_id is not UNSET:
            field_dict["leave_id"] = leave_id
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("public", (None, str(self.public).encode(), "text/plain")))

        files.append(("space", (None, str(self.space.value).encode(), "text/plain")))

        files.append(
            (
                "is_pending_assignment",
                (None, str(self.is_pending_assignment).encode(), "text/plain"),
            )
        )

        files.append(("file", self.file.to_tuple()))

        files.append(("author_id", (None, str(self.author_id).encode(), "text/plain")))

        files.append(("company_id", (None, str(self.company_id).encode(), "text/plain")))

        for signee_ids_item_element in self.signee_ids:
            files.append(
                ("signee_ids[]", (None, str(signee_ids_item_element).encode(), "text/plain"))
            )

        files.append(
            ("request_esignature", (None, str(self.request_esignature).encode(), "text/plain"))
        )

        if not isinstance(self.folder_id, Unset):
            files.append(("folder_id", (None, str(self.folder_id).encode(), "text/plain")))

        if not isinstance(self.file_filename, Unset):
            files.append(("file_filename", (None, str(self.file_filename).encode(), "text/plain")))

        if not isinstance(self.leave_id, Unset):
            files.append(("leave_id", (None, str(self.leave_id).encode(), "text/plain")))

        if not isinstance(self.employee_id, Unset):
            files.append(("employee_id", (None, str(self.employee_id).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public = d.pop("public")

        space = PostApi20251001ResourcesDocumentsDocumentsBodySpace(d.pop("space"))

        is_pending_assignment = d.pop("is_pending_assignment")

        file = File(payload=BytesIO(d.pop("file")))

        author_id = d.pop("author_id")

        company_id = d.pop("company_id")

        signee_ids = cast(list[int], d.pop("signee_ids[]"))

        request_esignature = d.pop("request_esignature")

        folder_id = d.pop("folder_id", UNSET)

        file_filename = d.pop("file_filename", UNSET)

        leave_id = d.pop("leave_id", UNSET)

        employee_id = d.pop("employee_id", UNSET)

        post_api_20251001_resources_documents_documents_body = cls(
            public=public,
            space=space,
            is_pending_assignment=is_pending_assignment,
            file=file,
            author_id=author_id,
            company_id=company_id,
            signee_ids=signee_ids,
            request_esignature=request_esignature,
            folder_id=folder_id,
            file_filename=file_filename,
            leave_id=leave_id,
            employee_id=employee_id,
        )

        post_api_20251001_resources_documents_documents_body.additional_properties = d
        return post_api_20251001_resources_documents_documents_body

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
