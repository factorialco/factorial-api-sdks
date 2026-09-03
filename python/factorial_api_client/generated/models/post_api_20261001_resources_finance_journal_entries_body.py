from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_finance_journal_entries_body_status import (
    PostApi20261001ResourcesFinanceJournalEntriesBodyStatus,
)
from ..models.post_api_20261001_resources_finance_journal_entries_body_type import (
    PostApi20261001ResourcesFinanceJournalEntriesBodyType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_finance_journal_entries_body_lines_item import (
        PostApi20261001ResourcesFinanceJournalEntriesBodyLinesItem,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesFinanceJournalEntriesBody")


@_attrs_define
class PostApi20261001ResourcesFinanceJournalEntriesBody:
    legal_entity_id: str
    """ The associated Legal Entity ID """
    lines: list[PostApi20261001ResourcesFinanceJournalEntriesBodyLinesItem]
    """ Array of journal lines for this entry, example: [{"account_id": 9876, "debit_amount_cents": 0,
    "credit_amount_cents": 100, "external_id": "LINE-001"}, {"account_id": 9876, "debit_amount_cents": 100,
    "credit_amount_cents": 0, "external_id": "LINE-002"}] """
    reference_date: str
    """ Date of the associate source """
    external_id: str | Unset = UNSET
    """ External identifier for the journal entry """
    type_: PostApi20261001ResourcesFinanceJournalEntriesBodyType | Unset = UNSET
    """ Journal entry type (e.g. bank, invoice, tax) """
    description: str | Unset = UNSET
    """ Description of the journal entry """
    status: PostApi20261001ResourcesFinanceJournalEntriesBodyStatus | Unset = UNSET
    """ Status of the journal entry (reversed, published, etc.) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legal_entity_id = self.legal_entity_id

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        reference_date = self.reference_date

        external_id = self.external_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value if self.type_ is not None else None

        description = self.description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status is not None else None

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "legal_entity_id": legal_entity_id,
                "lines": lines,
                "reference_date": reference_date,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_finance_journal_entries_body_lines_item import (
            PostApi20261001ResourcesFinanceJournalEntriesBodyLinesItem,
        )

        d = dict(src_dict)
        legal_entity_id = d.pop("legal_entity_id")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = PostApi20261001ResourcesFinanceJournalEntriesBodyLinesItem.from_dict(
                lines_item_data
            )

            lines.append(lines_item)

        reference_date = d.pop("reference_date")

        external_id = d.pop("external_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PostApi20261001ResourcesFinanceJournalEntriesBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PostApi20261001ResourcesFinanceJournalEntriesBodyType(_type_) if _type_ is not None else None

        description = d.pop("description", UNSET)

        _status = d.pop("status", UNSET)
        status: PostApi20261001ResourcesFinanceJournalEntriesBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PostApi20261001ResourcesFinanceJournalEntriesBodyStatus(_status) if _status is not None else None

        post_api_20261001_resources_finance_journal_entries_body = cls(
            legal_entity_id=legal_entity_id,
            lines=lines,
            reference_date=reference_date,
            external_id=external_id,
            type_=type_,
            description=description,
            status=status,
        )

        post_api_20261001_resources_finance_journal_entries_body.additional_properties = d
        return post_api_20261001_resources_finance_journal_entries_body

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
