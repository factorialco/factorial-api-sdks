from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinanceJournalLine")


@_attrs_define
class FinanceJournalLine:
    id: int
    """ Factorial id """
    number: int
    """ Sequential number assigned to the line """
    debit_amount_cents: int
    """ The debit amount in cents """
    credit_amount_cents: int
    """ The credit amount in cents """
    journal_entry_id: int
    """ ID of the parent journal entry """
    account_id: int
    """ ID of the associated account """
    updated_at: str
    """ Timestamp when the journal line was last updated. """
    fully_reconciled_at: str | Unset = UNSET
    """ Timestamp when the journal line was reconciled """
    external_id: str | Unset = UNSET
    """ External identifier for the journal line """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        number = self.number

        debit_amount_cents = self.debit_amount_cents

        credit_amount_cents = self.credit_amount_cents

        journal_entry_id = self.journal_entry_id

        account_id = self.account_id

        updated_at = self.updated_at

        fully_reconciled_at = self.fully_reconciled_at

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "number": number,
                "debit_amount_cents": debit_amount_cents,
                "credit_amount_cents": credit_amount_cents,
                "journal_entry_id": journal_entry_id,
                "account_id": account_id,
                "updated_at": updated_at,
            }
        )
        if fully_reconciled_at is not UNSET:
            field_dict["fully_reconciled_at"] = fully_reconciled_at
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        number = d.pop("number")

        debit_amount_cents = d.pop("debit_amount_cents")

        credit_amount_cents = d.pop("credit_amount_cents")

        journal_entry_id = d.pop("journal_entry_id")

        account_id = d.pop("account_id")

        updated_at = d.pop("updated_at")

        fully_reconciled_at = d.pop("fully_reconciled_at", UNSET)

        external_id = d.pop("external_id", UNSET)

        finance_journal_line = cls(
            id=id,
            number=number,
            debit_amount_cents=debit_amount_cents,
            credit_amount_cents=credit_amount_cents,
            journal_entry_id=journal_entry_id,
            account_id=account_id,
            updated_at=updated_at,
            fully_reconciled_at=fully_reconciled_at,
            external_id=external_id,
        )

        finance_journal_line.additional_properties = d
        return finance_journal_line

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
