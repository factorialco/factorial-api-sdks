from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expenses_expense_signed_document_file import ExpensesExpenseSignedDocumentFile
    from ..models.expenses_expense_signed_document_original_files_item import (
        ExpensesExpenseSignedDocumentOriginalFilesItem,
    )


T = TypeVar("T", bound="ExpensesExpenseSignedDocument")


@_attrs_define
class ExpensesExpenseSignedDocument:
    """The signed document of the expense"""

    id: str
    original_files: list[ExpensesExpenseSignedDocumentOriginalFilesItem]
    signed_for_organization: str
    created_at: str
    signing: bool
    file: ExpensesExpenseSignedDocumentFile | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        original_files = []
        for original_files_item_data in self.original_files:
            original_files_item = original_files_item_data.to_dict()
            original_files.append(original_files_item)

        signed_for_organization = self.signed_for_organization

        created_at = self.created_at

        signing = self.signing

        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "original_files": original_files,
                "signed_for_organization": signed_for_organization,
                "created_at": created_at,
                "signing": signing,
            }
        )
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.expenses_expense_signed_document_file import ExpensesExpenseSignedDocumentFile
        from ..models.expenses_expense_signed_document_original_files_item import (
            ExpensesExpenseSignedDocumentOriginalFilesItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        original_files = []
        _original_files = d.pop("original_files")
        for original_files_item_data in _original_files:
            original_files_item = ExpensesExpenseSignedDocumentOriginalFilesItem.from_dict(
                original_files_item_data
            )

            original_files.append(original_files_item)

        signed_for_organization = d.pop("signed_for_organization")

        created_at = d.pop("created_at")

        signing = d.pop("signing")

        _file = d.pop("file", UNSET)
        file: ExpensesExpenseSignedDocumentFile | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = ExpensesExpenseSignedDocumentFile.from_dict(_file)

        expenses_expense_signed_document = cls(
            id=id,
            original_files=original_files,
            signed_for_organization=signed_for_organization,
            created_at=created_at,
            signing=signing,
            file=file,
        )

        expenses_expense_signed_document.additional_properties = d
        return expenses_expense_signed_document

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
