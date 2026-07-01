from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookkeepersManagementIncidence")


@_attrs_define
class BookkeepersManagementIncidence:
    id: str
    """ identifier of the incidence (aka employee update). """
    legal_entity_id: str
    """ identifier of legal entity related. """
    name: str
    """ name of the incidence (aka employee update). It also represent the incidence type. For example a new hire
    incidence will be """
    target_id: str
    """ The incidence (aka employee update) is also related to a another resource, for example for a leave target,
    the target identifier will be the leave id. """
    target_type: str
    """ The incidence (aka employee update) is also related to a another resource, for example a leave. This is the
    target type. The other types are Employee, Contracts::ContractVersion, BookkeepersManagement::ManualIncidence,
    Finance::CostCenterMembership. """
    status: str
    company_id: str
    """ identifier of company related. """
    created_at: str
    """ Date in which incidence (aka employee update) was created. """
    is_reopened: bool
    """ Boolean that indicates if the incidence (aka employee update) has been reopened. """
    employee_id: str | Unset = UNSET
    """ identifier of employee related. """
    custom_name: str | Unset = UNSET
    starts_on: str | Unset = UNSET
    """ The date the incidence (aka employee update) starts. """
    ends_on: str | Unset = UNSET
    """ The date the incidence (aka employee update) end. """
    read_at: str | Unset = UNSET
    """ The date the incidence (aka employee update) was read. """
    message_from: str | Unset = UNSET
    """ Indicate the message sender on the incidence (aka employee update). It can be any of 'bookkeeper', 'admin'
    """
    has_message: bool | Unset = UNSET
    """ Boolean that indicates if the incidence (aka employee update) has unread messages. """
    legal_entity_name: str | Unset = UNSET
    employee_first_name: str | Unset = UNSET
    employee_last_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        legal_entity_id = self.legal_entity_id

        name = self.name

        target_id = self.target_id

        target_type = self.target_type

        status = self.status

        company_id = self.company_id

        created_at = self.created_at

        is_reopened = self.is_reopened

        employee_id = self.employee_id

        custom_name = self.custom_name

        starts_on = self.starts_on

        ends_on = self.ends_on

        read_at = self.read_at

        message_from = self.message_from

        has_message = self.has_message

        legal_entity_name = self.legal_entity_name

        employee_first_name = self.employee_first_name

        employee_last_name = self.employee_last_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "legal_entity_id": legal_entity_id,
                "name": name,
                "target_id": target_id,
                "target_type": target_type,
                "status": status,
                "company_id": company_id,
                "created_at": created_at,
                "is_reopened": is_reopened,
            }
        )
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if custom_name is not UNSET:
            field_dict["custom_name"] = custom_name
        if starts_on is not UNSET:
            field_dict["starts_on"] = starts_on
        if ends_on is not UNSET:
            field_dict["ends_on"] = ends_on
        if read_at is not UNSET:
            field_dict["read_at"] = read_at
        if message_from is not UNSET:
            field_dict["message_from"] = message_from
        if has_message is not UNSET:
            field_dict["has_message"] = has_message
        if legal_entity_name is not UNSET:
            field_dict["legal_entity_name"] = legal_entity_name
        if employee_first_name is not UNSET:
            field_dict["employee_first_name"] = employee_first_name
        if employee_last_name is not UNSET:
            field_dict["employee_last_name"] = employee_last_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        legal_entity_id = d.pop("legal_entity_id")

        name = d.pop("name")

        target_id = d.pop("target_id")

        target_type = d.pop("target_type")

        status = d.pop("status")

        company_id = d.pop("company_id")

        created_at = d.pop("created_at")

        is_reopened = d.pop("is_reopened")

        employee_id = d.pop("employee_id", UNSET)

        custom_name = d.pop("custom_name", UNSET)

        starts_on = d.pop("starts_on", UNSET)

        ends_on = d.pop("ends_on", UNSET)

        read_at = d.pop("read_at", UNSET)

        message_from = d.pop("message_from", UNSET)

        has_message = d.pop("has_message", UNSET)

        legal_entity_name = d.pop("legal_entity_name", UNSET)

        employee_first_name = d.pop("employee_first_name", UNSET)

        employee_last_name = d.pop("employee_last_name", UNSET)

        bookkeepers_management_incidence = cls(
            id=id,
            legal_entity_id=legal_entity_id,
            name=name,
            target_id=target_id,
            target_type=target_type,
            status=status,
            company_id=company_id,
            created_at=created_at,
            is_reopened=is_reopened,
            employee_id=employee_id,
            custom_name=custom_name,
            starts_on=starts_on,
            ends_on=ends_on,
            read_at=read_at,
            message_from=message_from,
            has_message=has_message,
            legal_entity_name=legal_entity_name,
            employee_first_name=employee_first_name,
            employee_last_name=employee_last_name,
        )

        bookkeepers_management_incidence.additional_properties = d
        return bookkeepers_management_incidence

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
