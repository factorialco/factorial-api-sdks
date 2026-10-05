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
    """ Whether an attachment (e.g. a sick note) can be added to leaves of this type """
    visibility: bool
    """ Whether the leave type is visible to employees (vs. admin-only) """
    workable: bool
    """ Whether days taken under this leave type still count as workable (working) days """
    company_id: str
    """ ID of the company this leave type belongs to """
    allowance_ids: list[str]
    """ IDs of the allowances this leave type draws its balance from """
    details_required: bool
    """ Whether the requester must provide additional details (a reason) when requesting this leave type """
    translated_name: str | Unset = UNSET
    """ Translated name of the leave type, if available """
    active: bool | Unset = UNSET
    """ Whether the leave type is active """
    editable: bool | Unset = UNSET
    """ Whether the leave type is editable """
    approval_required: bool | Unset = UNSET
    """ Whether leaves of this type must be approved before they take effect (when false, requests are auto-approved
    on creation) """
    accrues: bool | Unset = UNSET
    """ Whether leaves of this type consume an accruing balance/allowance (vs. a non-accruing type that does not
    draw down a balance) """
    allow_endless: bool | Unset = UNSET
    """ Whether leaves of this type may be open-ended (created with no finish date) """
    restricted: bool | Unset = UNSET
    """ Whether requesting this leave type is restricted to specific employees or conditions rather than open to
    everyone """
    payable: bool | Unset = UNSET
    """ Whether leaves of this type are paid """
    is_attachment_mandatory: bool | Unset = UNSET
    """ Whether an attachment is mandatory (not just allowed) to request this leave type """
    half_days_units_enabled: bool | Unset = UNSET
    """ Whether leaves of this type can be requested in half-day units """
    max_days_in_cents: int | Unset = UNSET
    """ Maximum number of days a single request may take, in hundredths of a day (e.g. 5000 = 50 days); null if
    unbounded """
    min_days_in_cents: int | Unset = UNSET
    """ Minimum number of days a single request must take, in hundredths of a day (e.g. 1000 = 10 days); null if
    unbounded """
    description: str | Unset = UNSET
    """ Free-text description of the leave type """
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
