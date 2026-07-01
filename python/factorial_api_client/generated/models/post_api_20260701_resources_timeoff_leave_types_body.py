from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260701ResourcesTimeoffLeaveTypesBody")


@_attrs_define
class PostApi20260701ResourcesTimeoffLeaveTypesBody:
    accrues: bool
    """ Whether the leave type accrues over time """
    approval_required: bool
    """ Whether approval is required for this leave type """
    identifier: str
    """ A unique identifier for the leave type """
    color: str
    """ The color associated with this leave type """
    name: str
    """ The name of the leave type """
    workable: bool
    """ Whether the leave type is workable (can be worked on during leave) """
    company_id: str
    """ Identifier of the company associated with this leave type """
    details_required: bool
    """ Whether additional details are required for the leave type """
    attachment: bool | Unset = UNSET
    """ Whether an attachment is required for this leave type """
    visibility: bool | Unset = UNSET
    """ Whether the leave type is visible to employees """
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
    editable: bool | Unset = UNSET
    """ Whether the leave type is editable """
    allow_endless: bool | Unset = UNSET
    """ Whether endless leave is allowed """
    restricted: bool | Unset = UNSET
    """ Whether the leave type is restricted """
    description: str | Unset = UNSET
    """ Description of the leave type """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accrues = self.accrues

        approval_required = self.approval_required

        identifier = self.identifier

        color = self.color

        name = self.name

        workable = self.workable

        company_id = self.company_id

        details_required = self.details_required

        attachment = self.attachment

        visibility = self.visibility

        payable = self.payable

        is_attachment_mandatory = self.is_attachment_mandatory

        half_days_units_enabled = self.half_days_units_enabled

        max_days_in_cents = self.max_days_in_cents

        min_days_in_cents = self.min_days_in_cents

        editable = self.editable

        allow_endless = self.allow_endless

        restricted = self.restricted

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accrues": accrues,
                "approval_required": approval_required,
                "identifier": identifier,
                "color": color,
                "name": name,
                "workable": workable,
                "company_id": company_id,
                "details_required": details_required,
            }
        )
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
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
        if editable is not UNSET:
            field_dict["editable"] = editable
        if allow_endless is not UNSET:
            field_dict["allow_endless"] = allow_endless
        if restricted is not UNSET:
            field_dict["restricted"] = restricted
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accrues = d.pop("accrues")

        approval_required = d.pop("approval_required")

        identifier = d.pop("identifier")

        color = d.pop("color")

        name = d.pop("name")

        workable = d.pop("workable")

        company_id = d.pop("company_id")

        details_required = d.pop("details_required")

        attachment = d.pop("attachment", UNSET)

        visibility = d.pop("visibility", UNSET)

        payable = d.pop("payable", UNSET)

        is_attachment_mandatory = d.pop("is_attachment_mandatory", UNSET)

        half_days_units_enabled = d.pop("half_days_units_enabled", UNSET)

        max_days_in_cents = d.pop("max_days_in_cents", UNSET)

        min_days_in_cents = d.pop("min_days_in_cents", UNSET)

        editable = d.pop("editable", UNSET)

        allow_endless = d.pop("allow_endless", UNSET)

        restricted = d.pop("restricted", UNSET)

        description = d.pop("description", UNSET)

        post_api_20260701_resources_timeoff_leave_types_body = cls(
            accrues=accrues,
            approval_required=approval_required,
            identifier=identifier,
            color=color,
            name=name,
            workable=workable,
            company_id=company_id,
            details_required=details_required,
            attachment=attachment,
            visibility=visibility,
            payable=payable,
            is_attachment_mandatory=is_attachment_mandatory,
            half_days_units_enabled=half_days_units_enabled,
            max_days_in_cents=max_days_in_cents,
            min_days_in_cents=min_days_in_cents,
            editable=editable,
            allow_endless=allow_endless,
            restricted=restricted,
            description=description,
        )

        post_api_20260701_resources_timeoff_leave_types_body.additional_properties = d
        return post_api_20260701_resources_timeoff_leave_types_body

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
