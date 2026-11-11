from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationEmployee")


@_attrs_define
class AuthenticationEmployee:
    id: str
    """ employee identifier, refers to /employees/employees endpoint. """
    company_id: str
    """ company identifier. """
    login_email: str | Unset = UNSET
    """ the email the employee currently logs in with. It only changes once the email change is confirmed. """
    unconfirmed_login_email: str | Unset = UNSET
    """ the email waiting for confirmation, or null when there is no pending email change. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        login_email = self.login_email

        unconfirmed_login_email = self.unconfirmed_login_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
            }
        )
        if login_email is not UNSET:
            field_dict["login_email"] = login_email
        if unconfirmed_login_email is not UNSET:
            field_dict["unconfirmed_login_email"] = unconfirmed_login_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        login_email = d.pop("login_email", UNSET)

        unconfirmed_login_email = d.pop("unconfirmed_login_email", UNSET)

        authentication_employee = cls(
            id=id,
            company_id=company_id,
            login_email=login_email,
            unconfirmed_login_email=unconfirmed_login_email,
        )

        authentication_employee.additional_properties = d
        return authentication_employee

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
