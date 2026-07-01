from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.banking_bank_account_number_format import BankingBankAccountNumberFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="BankingBankAccountNumber")


@_attrs_define
class BankingBankAccountNumber:
    id: str
    """ Employee id. """
    company_id: str
    """ Company identifier """
    account_number: str
    """ Account number """
    format_: BankingBankAccountNumberFormat
    """ The format of the account number. """
    complementary_data: str | Unset = UNSET
    """ Additional banking information, depending on the selected format. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        account_number = self.account_number

        format_ = self.format_.value

        complementary_data = self.complementary_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "account_number": account_number,
                "format": format_,
            }
        )
        if complementary_data is not UNSET:
            field_dict["complementary_data"] = complementary_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        account_number = d.pop("account_number")

        format_ = BankingBankAccountNumberFormat(d.pop("format"))

        complementary_data = d.pop("complementary_data", UNSET)

        banking_bank_account_number = cls(
            id=id,
            company_id=company_id,
            account_number=account_number,
            format_=format_,
            complementary_data=complementary_data,
        )

        banking_bank_account_number.additional_properties = d
        return banking_bank_account_number

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
