from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPublicCredential")


@_attrs_define
class ApiPublicCredential:
    company_id: str
    """ company id for all kind of accesses """
    id: str
    """ id of the credential prefixed by the type of credential """
    employee_id: str
    """ Id for hte employee related. Only for Access Oauth token """
    email: str | Unset = UNSET
    """ Only for Access Oauth token """
    login_email: str | Unset = UNSET
    """ Only for Access Oauth token """
    full_name: str | Unset = UNSET
    first_name: str | Unset = UNSET
    """ Only for Access Oauth token """
    last_name: str | Unset = UNSET
    """ Only for Access Oauth token """
    role: str | Unset = UNSET
    """ Employee role in the Company. Only for Access Oauth token """
    gdpr_tos: bool | Unset = UNSET
    """ Only for Company Oauth or API key """
    legal_name: str | Unset = UNSET
    """ Only for Company Oauth or API key """
    locale: str | Unset = UNSET
    """ Only for Company Oauth or API key """
    logo: str | Unset = UNSET
    """ Only for Company Oauth or API key """
    name: str | Unset = UNSET
    """ Only for Company Oauth or API key """
    onboarded_on: str | Unset = UNSET
    """ Only for Company Oauth or API key """
    subscription_plan: str | Unset = UNSET
    """ Only for Company Oauth or API key """
    tin: str | Unset = UNSET
    """ Only for Company Oauth or API key """
    to_be_deleted: str | Unset = UNSET
    """ Only for Company Oauth or API key """
    tos: bool | Unset = UNSET
    """ Only for Company Oauth or API key """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        id = self.id

        employee_id = self.employee_id

        email = self.email

        login_email = self.login_email

        full_name = self.full_name

        first_name = self.first_name

        last_name = self.last_name

        role = self.role

        gdpr_tos = self.gdpr_tos

        legal_name = self.legal_name

        locale = self.locale

        logo = self.logo

        name = self.name

        onboarded_on = self.onboarded_on

        subscription_plan = self.subscription_plan

        tin = self.tin

        to_be_deleted = self.to_be_deleted

        tos = self.tos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_id": company_id,
                "id": id,
                "employee_id": employee_id,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if login_email is not UNSET:
            field_dict["login_email"] = login_email
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if role is not UNSET:
            field_dict["role"] = role
        if gdpr_tos is not UNSET:
            field_dict["gdpr_tos"] = gdpr_tos
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if locale is not UNSET:
            field_dict["locale"] = locale
        if logo is not UNSET:
            field_dict["logo"] = logo
        if name is not UNSET:
            field_dict["name"] = name
        if onboarded_on is not UNSET:
            field_dict["onboarded_on"] = onboarded_on
        if subscription_plan is not UNSET:
            field_dict["subscription_plan"] = subscription_plan
        if tin is not UNSET:
            field_dict["tin"] = tin
        if to_be_deleted is not UNSET:
            field_dict["to_be_deleted"] = to_be_deleted
        if tos is not UNSET:
            field_dict["tos"] = tos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("company_id")

        id = d.pop("id")

        employee_id = d.pop("employee_id")

        email = d.pop("email", UNSET)

        login_email = d.pop("login_email", UNSET)

        full_name = d.pop("full_name", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        role = d.pop("role", UNSET)

        gdpr_tos = d.pop("gdpr_tos", UNSET)

        legal_name = d.pop("legal_name", UNSET)

        locale = d.pop("locale", UNSET)

        logo = d.pop("logo", UNSET)

        name = d.pop("name", UNSET)

        onboarded_on = d.pop("onboarded_on", UNSET)

        subscription_plan = d.pop("subscription_plan", UNSET)

        tin = d.pop("tin", UNSET)

        to_be_deleted = d.pop("to_be_deleted", UNSET)

        tos = d.pop("tos", UNSET)

        api_public_credential = cls(
            company_id=company_id,
            id=id,
            employee_id=employee_id,
            email=email,
            login_email=login_email,
            full_name=full_name,
            first_name=first_name,
            last_name=last_name,
            role=role,
            gdpr_tos=gdpr_tos,
            legal_name=legal_name,
            locale=locale,
            logo=logo,
            name=name,
            onboarded_on=onboarded_on,
            subscription_plan=subscription_plan,
            tin=tin,
            to_be_deleted=to_be_deleted,
            tos=tos,
        )

        api_public_credential.additional_properties = d
        return api_public_credential

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
