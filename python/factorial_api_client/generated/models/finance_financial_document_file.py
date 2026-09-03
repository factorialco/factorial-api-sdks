from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FinanceFinancialDocumentFile")


@_attrs_define
class FinanceFinancialDocumentFile:
    """File attached.

    Example:
        {'id': 1, 'filename': 'invoice.pdf', 'url': 'https://factorial.com/invoice.pdf', 'size': 1024, 'content_type':
            'application/pdf', 'created_at': '2020-01-01T00:00:00.000Z'}

    """

    id: str
    filename: str
    url: str
    size: int
    content_type: str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        filename = self.filename

        url = self.url

        size = self.size

        content_type = self.content_type

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "filename": filename,
                "url": url,
                "size": size,
                "content_type": content_type,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        filename = d.pop("filename")

        url = d.pop("url")

        size = d.pop("size")

        content_type = d.pop("content_type")

        created_at = d.pop("created_at")

        finance_financial_document_file = cls(
            id=id,
            filename=filename,
            url=url,
            size=size,
            content_type=content_type,
            created_at=created_at,
        )

        finance_financial_document_file.additional_properties = d
        return finance_financial_document_file

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
