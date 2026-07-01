from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.documents_document_signature_status import DocumentsDocumentSignatureStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentsDocument")


@_attrs_define
class DocumentsDocument:
    created_at: str
    """ creation date of the document. """
    filename: str
    """ name of the document. """
    id: str
    """ document identifier. """
    public: bool
    """ flag to indicate if the document is public. """
    space: str
    """ document space. """
    updated_at: str
    """ last update date of the document. """
    author_id: str | Unset = UNSET
    """ access identifier of the author, refers to /employees/employees endpoint. """
    company_id: str | Unset = UNSET
    """ company identifier, refers to /api/me endpoint. """
    content_type: str | Unset = UNSET
    """ document content type. """
    employee_id: str | Unset = UNSET
    """ employee identifier associated to the document. """
    extension: str | Unset = UNSET
    """ document extension. """
    file_size: int | Unset = UNSET
    """ document file size in bytes. """
    folder_id: str | Unset = UNSET
    """ folder identifier, references to documents/folders endpoint. """
    is_company_document: bool | Unset = UNSET
    """ flag that indicates if the document is a company document. """
    is_management_document: bool | Unset = UNSET
    """ flag that indicates if the document is a management document. """
    is_pending_assignment: bool | Unset = UNSET
    """ flag that indicates if the document is pending assignment. """
    leave_id: str | Unset = UNSET
    """ leave identifier associated to the document, refers to /timeoff/leaves endpoint. """
    signature_status: DocumentsDocumentSignatureStatus | Unset = UNSET
    """ document signature status. """
    signees: list[str] | Unset = UNSET
    """ list of signee access identifiers associated to the document, refers to /employees/employees endpoint. """
    deleted_at: str | Unset = UNSET
    """ deletion date of the document. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        filename = self.filename

        id = self.id

        public = self.public

        space = self.space

        updated_at = self.updated_at

        author_id = self.author_id

        company_id = self.company_id

        content_type = self.content_type

        employee_id = self.employee_id

        extension = self.extension

        file_size = self.file_size

        folder_id = self.folder_id

        is_company_document = self.is_company_document

        is_management_document = self.is_management_document

        is_pending_assignment = self.is_pending_assignment

        leave_id = self.leave_id

        signature_status: str | Unset = UNSET
        if not isinstance(self.signature_status, Unset):
            signature_status = self.signature_status.value

        signees: list[str] | Unset = UNSET
        if not isinstance(self.signees, Unset):
            signees = self.signees

        deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "filename": filename,
                "id": id,
                "public": public,
                "space": space,
                "updated_at": updated_at,
            }
        )
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if extension is not UNSET:
            field_dict["extension"] = extension
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if folder_id is not UNSET:
            field_dict["folder_id"] = folder_id
        if is_company_document is not UNSET:
            field_dict["is_company_document"] = is_company_document
        if is_management_document is not UNSET:
            field_dict["is_management_document"] = is_management_document
        if is_pending_assignment is not UNSET:
            field_dict["is_pending_assignment"] = is_pending_assignment
        if leave_id is not UNSET:
            field_dict["leave_id"] = leave_id
        if signature_status is not UNSET:
            field_dict["signature_status"] = signature_status
        if signees is not UNSET:
            field_dict["signees"] = signees
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at")

        filename = d.pop("filename")

        id = d.pop("id")

        public = d.pop("public")

        space = d.pop("space")

        updated_at = d.pop("updated_at")

        author_id = d.pop("author_id", UNSET)

        company_id = d.pop("company_id", UNSET)

        content_type = d.pop("content_type", UNSET)

        employee_id = d.pop("employee_id", UNSET)

        extension = d.pop("extension", UNSET)

        file_size = d.pop("file_size", UNSET)

        folder_id = d.pop("folder_id", UNSET)

        is_company_document = d.pop("is_company_document", UNSET)

        is_management_document = d.pop("is_management_document", UNSET)

        is_pending_assignment = d.pop("is_pending_assignment", UNSET)

        leave_id = d.pop("leave_id", UNSET)

        _signature_status = d.pop("signature_status", UNSET)
        signature_status: DocumentsDocumentSignatureStatus | Unset
        if isinstance(_signature_status, Unset):
            signature_status = UNSET
        else:
            signature_status = DocumentsDocumentSignatureStatus(_signature_status) if _signature_status is not None else None

        signees = cast(list[str], d.pop("signees", UNSET))

        deleted_at = d.pop("deleted_at", UNSET)

        documents_document = cls(
            created_at=created_at,
            filename=filename,
            id=id,
            public=public,
            space=space,
            updated_at=updated_at,
            author_id=author_id,
            company_id=company_id,
            content_type=content_type,
            employee_id=employee_id,
            extension=extension,
            file_size=file_size,
            folder_id=folder_id,
            is_company_document=is_company_document,
            is_management_document=is_management_document,
            is_pending_assignment=is_pending_assignment,
            leave_id=leave_id,
            signature_status=signature_status,
            signees=signees,
            deleted_at=deleted_at,
        )

        documents_document.additional_properties = d
        return documents_document

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
