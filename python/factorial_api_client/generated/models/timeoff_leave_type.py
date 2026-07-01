from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeoffLeaveType")


@_attrs_define
class TimeoffLeaveType:
    id: str
    """ Identifier of the leave type """
    name: str
    """ Name of the leave type """
    identifier: str
    """ Unique identifier of the leave type """
    color: str
    """ The color associated with this leave type """
    attachment: bool
    """ Whether an attachment is required for this leave type """
    visibility: bool
    """ Whether the leave type is visible to employees """
    workable: bool
    """ Whether the leave type is workable """
    company_id: str
    """ Identifier of the company associated with this leave type """
    allowance_ids: list[str]
    """ List of allowance identifiers associated with this leave type """
    details_required: bool
    """ Whether additional details are required for the leave type """
    translated_name: str | Unset = UNSET
    """ Translated name of the leave type, if available """
    active: bool | Unset = UNSET
    """ Whether the leave type is active """
    editable: bool | Unset = UNSET
    """ Whether the leave type is editable """
    approval_required: bool | Unset = UNSET
    """ Whether approval is required for this leave type """
    accrues: bool | Unset = UNSET
    """ Whether the leave type accrues over time """
    allow_endless: bool | Unset = UNSET
    """ Whether endless leave is allowed """
    restricted: bool | Unset = UNSET
    """ Whether the leave type is restricted """
    payable: bool | Unset = UNSET
    """ Whether the leave type is payable """
    is_attachment_mandatory: bool | Unset = UNSET
    """ Whether the attachment is mandatory """
    half_days_units_enabled: bool | Unset = UNSET
    """ Whether half-day units are enabled for this leave type """
    max_days_in_cents: int | Unset = UNSET
    """ Maximum days in cents that can be taken """
    min_days_in_cents: int | Unset = UNSET
    """ Minimum days in cents that must be taken """
    description: str | Unset = UNSET
    """ Description of the leave type """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        identifier = self.identifier

        color = self.color

        attachment = self.attachment

        visibility = self.visibility

        workable = self.workable

        company_id = self.company_id

        allowance_ids = self.allowance_ids

        details_required = self.details_required

        translated_name = self.translated_name

        active = self.active

        editable = self.editable

        approval_required = self.approval_required

        accrues = self.accrues

        allow_endless = self.allow_endless

        restricted = self.restricted

        payable = self.payable

        is_attachment_mandatory = self.is_attachment_mandatory

        half_days_units_enabled = self.half_days_units_enabled

        max_days_in_cents = self.max_days_in_cents

        min_days_in_cents = self.min_days_in_cents

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "identifier": identifier,
                "color": color,
                "attachment": attachment,
                "visibility": visibility,
                "workable": workable,
                "company_id": company_id,
                "allowance_ids": allowance_ids,
                "details_required": details_required,
            }
        )
        if translated_name is not UNSET:
            field_dict["translated_name"] = translated_name
        if active is not UNSET:
            field_dict["active"] = active
        if editable is not UNSET:
            field_dict["editable"] = editable
        if approval_required is not UNSET:
            field_dict["approval_required"] = approval_required
        if accrues is not UNSET:
            field_dict["accrues"] = accrues
        if allow_endless is not UNSET:
            field_dict["allow_endless"] = allow_endless
        if restricted is not UNSET:
            field_dict["restricted"] = restricted
        if payable is not UNSET:
            field_dict["payable"] = payable
        if is_attachment_mandatory is not UNSET:
            field_dict["is_attachment_mandatory"] = is_attachment_mandatory
        if half_days_units_enabled is not UNSET:
            field_dict["half_days_units_enabled"] = half_days_units_enabled
        if max_days_in_cents is not UNSET:
            field_dict["max_days_in_cents"] = max_days_in_cents
        if min_days_in_cents is not UNSET:
            field_dict["min_days_in_cents"] = min_days_in_cents
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        identifier = d.pop("identifier")

        color = d.pop("color")

        attachment = d.pop("attachment")

        visibility = d.pop("visibility")

        workable = d.pop("workable")

        company_id = d.pop("company_id")

        allowance_ids = cast(list[str], d.pop("allowance_ids"))

        details_required = d.pop("details_required")

        translated_name = d.pop("translated_name", UNSET)

        active = d.pop("active", UNSET)

        editable = d.pop("editable", UNSET)

        approval_required = d.pop("approval_required", UNSET)

        accrues = d.pop("accrues", UNSET)

        allow_endless = d.pop("allow_endless", UNSET)

        restricted = d.pop("restricted", UNSET)

        payable = d.pop("payable", UNSET)

        is_attachment_mandatory = d.pop("is_attachment_mandatory", UNSET)

        half_days_units_enabled = d.pop("half_days_units_enabled", UNSET)

        max_days_in_cents = d.pop("max_days_in_cents", UNSET)

        min_days_in_cents = d.pop("min_days_in_cents", UNSET)

        description = d.pop("description", UNSET)

        timeoff_leave_type = cls(
            id=id,
            name=name,
            identifier=identifier,
            color=color,
            attachment=attachment,
            visibility=visibility,
            workable=workable,
            company_id=company_id,
            allowance_ids=allowance_ids,
            details_required=details_required,
            translated_name=translated_name,
            active=active,
            editable=editable,
            approval_required=approval_required,
            accrues=accrues,
            allow_endless=allow_endless,
            restricted=restricted,
            payable=payable,
            is_attachment_mandatory=is_attachment_mandatory,
            half_days_units_enabled=half_days_units_enabled,
            max_days_in_cents=max_days_in_cents,
            min_days_in_cents=min_days_in_cents,
            description=description,
        )

        timeoff_leave_type.additional_properties = d
        return timeoff_leave_type

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
