from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesFinanceJournalEntriesBodyLinesItem")


@_attrs_define
class PostApi20261001ResourcesFinanceJournalEntriesBodyLinesItem:
    debit_amount_cents: int
    """ The debit amount in cents """
    credit_amount_cents: int
    """ The credit amount in cents """
    account_id: str
    """ ID of the associated account """
    external_id: str | Unset = UNSET
    """ External identifier for the journal line """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        debit_amount_cents = self.debit_amount_cents

        credit_amount_cents = self.credit_amount_cents

        account_id = self.account_id

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "debit_amount_cents": debit_amount_cents,
                "credit_amount_cents": credit_amount_cents,
                "account_id": account_id,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        debit_amount_cents = d.pop("debit_amount_cents")

        credit_amount_cents = d.pop("credit_amount_cents")

        account_id = d.pop("account_id")

        external_id = d.pop("external_id", UNSET)

        post_api_20261001_resources_finance_journal_entries_body_lines_item = cls(
            debit_amount_cents=debit_amount_cents,
            credit_amount_cents=credit_amount_cents,
            account_id=account_id,
            external_id=external_id,
        )

        post_api_20261001_resources_finance_journal_entries_body_lines_item.additional_properties = d
        return post_api_20261001_resources_finance_journal_entries_body_lines_item

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
