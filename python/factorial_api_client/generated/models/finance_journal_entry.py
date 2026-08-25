from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.finance_journal_entry_source_type import FinanceJournalEntrySourceType
from ..models.finance_journal_entry_status import FinanceJournalEntryStatus
from ..models.finance_journal_entry_type import FinanceJournalEntryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FinanceJournalEntry")


@_attrs_define
class FinanceJournalEntry:
    id: str
    """ Journal entry ID """
    number: int
    """ Incremental number assigned to the journal entry """
    published_at: str
    """ Timestamp when the journal entry was published. """
    type_: FinanceJournalEntryType
    """ Journal entry type (e.g. bank, invoice, tax) """
    reference_date: str
    """ Date of the associate source """
    legal_entity_id: str
    """ The associated Legal Entity ID """
    status: FinanceJournalEntryStatus
    """ The status of the journal entry (draft, published, etc.) """
    updated_at: str
    """ Timestamp when the journal entry was last updated. """
    source_id: str | Unset = UNSET
    """ Source id related with this journal entry """
    source_type: FinanceJournalEntrySourceType | Unset = UNSET
    """ Source type related with this journal entry """
    description: str | Unset = UNSET
    """ Description of the journal entry """
    external_id: str | Unset = UNSET
    """ External identifier for the journal entry """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        number = self.number

        published_at = self.published_at

        type_ = self.type_.value

        reference_date = self.reference_date

        legal_entity_id = self.legal_entity_id

        status = self.status.value

        updated_at = self.updated_at

        source_id = self.source_id

        source_type: str | Unset = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value if self.source_type is not None else None

        description = self.description

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "number": number,
                "published_at": published_at,
                "type": type_,
                "reference_date": reference_date,
                "legal_entity_id": legal_entity_id,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if description is not UNSET:
            field_dict["description"] = description
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        number = d.pop("number")

        published_at = d.pop("published_at")

        type_ = FinanceJournalEntryType(d.pop("type"))

        reference_date = d.pop("reference_date")

        legal_entity_id = d.pop("legal_entity_id")

        status = FinanceJournalEntryStatus(d.pop("status"))

        updated_at = d.pop("updated_at")

        source_id = d.pop("source_id", UNSET)

        _source_type = d.pop("source_type", UNSET)
        source_type: FinanceJournalEntrySourceType | Unset
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = FinanceJournalEntrySourceType(_source_type) if _source_type is not None else None

        description = d.pop("description", UNSET)

        external_id = d.pop("external_id", UNSET)

        finance_journal_entry = cls(
            id=id,
            number=number,
            published_at=published_at,
            type_=type_,
            reference_date=reference_date,
            legal_entity_id=legal_entity_id,
            status=status,
            updated_at=updated_at,
            source_id=source_id,
            source_type=source_type,
            description=description,
            external_id=external_id,
        )

        finance_journal_entry.additional_properties = d
        return finance_journal_entry

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
