from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20251001ResourcesTimeoffLeaveTypesIdBody")


@_attrs_define
class PutApi20251001ResourcesTimeoffLeaveTypesIdBody:
    id: int | Unset = UNSET
    """ Identifier of the leave type to update """
    accrues: bool | Unset = UNSET
    """ Whether the leave type accrues over time """
    approval_required: bool | Unset = UNSET
    """ Whether approval is required for this leave type """
    identifier: str | Unset = UNSET
    """ A unique identifier for the leave type """
    attachment: bool | Unset = UNSET
    """ Whether an attachment is required for this leave type """
    color: str | Unset = UNSET
    """ The color associated with this leave type (hex code) """
    name: str | Unset = UNSET
    """ The name of the leave type """
    visibility: bool | Unset = UNSET
    """ Whether the leave type is visible to employees """
    workable: bool | Unset = UNSET
    """ Whether the leave type is workable (can be worked on during leave) """
    payable: bool | Unset = UNSET
    """ Whether the leave type is payable """
    is_attachment_mandatory: str | Unset = UNSET
    """ Whether the attachment is mandatory or a status description (boolean or string) """
    half_days_units_enabled: bool | Unset = UNSET
    """ Whether half-day units are enabled for this leave type """
    max_days_in_cents: int | Unset = UNSET
    """ Maximum days in cents that can be taken """
    min_days_in_cents: int | Unset = UNSET
    """ Minimum days in cents that must be taken """
    active: bool | Unset = UNSET
    """ Whether the leave type is active """
    allow_endless: bool | Unset = UNSET
    """ Whether endless leave is allowed """
    restricted: bool | Unset = UNSET
    """ Whether the leave type is restricted """
    description: str | Unset = UNSET
    """ Description of the leave type """
    details_required: bool | Unset = UNSET
    """ Whether additional details are required for the leave type """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        accrues = self.accrues

        approval_required = self.approval_required

        identifier = self.identifier

        attachment = self.attachment

        color = self.color

        name = self.name

        visibility = self.visibility

        workable = self.workable

        payable = self.payable

        is_attachment_mandatory = self.is_attachment_mandatory

        half_days_units_enabled = self.half_days_units_enabled

        max_days_in_cents = self.max_days_in_cents

        min_days_in_cents = self.min_days_in_cents

        active = self.active

        allow_endless = self.allow_endless

        restricted = self.restricted

        description = self.description

        details_required = self.details_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if accrues is not UNSET:
            field_dict["accrues"] = accrues
        if approval_required is not UNSET:
            field_dict["approval_required"] = approval_required
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if color is not UNSET:
            field_dict["color"] = color
        if name is not UNSET:
            field_dict["name"] = name
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if workable is not UNSET:
            field_dict["workable"] = workable
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
        if active is not UNSET:
            field_dict["active"] = active
        if allow_endless is not UNSET:
            field_dict["allow_endless"] = allow_endless
        if restricted is not UNSET:
            field_dict["restricted"] = restricted
        if description is not UNSET:
            field_dict["description"] = description
        if details_required is not UNSET:
            field_dict["details_required"] = details_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        accrues = d.pop("accrues", UNSET)

        approval_required = d.pop("approval_required", UNSET)

        identifier = d.pop("identifier", UNSET)

        attachment = d.pop("attachment", UNSET)

        color = d.pop("color", UNSET)

        name = d.pop("name", UNSET)

        visibility = d.pop("visibility", UNSET)

        workable = d.pop("workable", UNSET)

        payable = d.pop("payable", UNSET)

        is_attachment_mandatory = d.pop("is_attachment_mandatory", UNSET)

        half_days_units_enabled = d.pop("half_days_units_enabled", UNSET)

        max_days_in_cents = d.pop("max_days_in_cents", UNSET)

        min_days_in_cents = d.pop("min_days_in_cents", UNSET)

        active = d.pop("active", UNSET)

        allow_endless = d.pop("allow_endless", UNSET)

        restricted = d.pop("restricted", UNSET)

        description = d.pop("description", UNSET)

        details_required = d.pop("details_required", UNSET)

        put_api_20251001_resources_timeoff_leave_types_id_body = cls(
            id=id,
            accrues=accrues,
            approval_required=approval_required,
            identifier=identifier,
            attachment=attachment,
            color=color,
            name=name,
            visibility=visibility,
            workable=workable,
            payable=payable,
            is_attachment_mandatory=is_attachment_mandatory,
            half_days_units_enabled=half_days_units_enabled,
            max_days_in_cents=max_days_in_cents,
            min_days_in_cents=min_days_in_cents,
            active=active,
            allow_endless=allow_endless,
            restricted=restricted,
            description=description,
            details_required=details_required,
        )

        put_api_20251001_resources_timeoff_leave_types_id_body.additional_properties = d
        return put_api_20251001_resources_timeoff_leave_types_id_body

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
