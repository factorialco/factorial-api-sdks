from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcurementPoTemplateFieldDefinition")


@_attrs_define
class ProcurementPoTemplateFieldDefinition:
    id: str
    """ The id of the field definition """
    po_template_version_id: str
    """ The PO template version this field belongs to """
    company_id: str
    """ Identifier of the company """
    section_type: str
    """ Section this field belongs to (general_information, vendor_contact, notes_and_delivery, line_item_columns)
    """
    label: str
    """ Display label for the field """
    field_type: str
    """ Data type of the field, driving how its value must be supplied when creating a purchase order. Scalar types:
    "text", "long_text", "number", "money", "percentage", "date", "boolean". "select" is a closed list — the value
    must be one of the strings in the "options" array. Reference types point to another Factorial value. Most are
    supplied as the referenced record's id, resolved via the existing public master-data endpoints: "vendor" -> a
    Finance vendor/contact, "employee" -> an employee, "team" -> a team, "cost_center" -> a cost center, "project"
    -> a project, "legal_entity" -> a legal entity, "tax_rate" -> a tax rate. Two are supplied as codes rather than
    ids: "payment_method" -> a payment-method enum value, and "currency" -> an ISO 4217 currency code.
     """
    predefined: bool
    """ Whether this is a system-predefined field """
    visible: bool
    """ Whether this field is visible in the PO form """
    required: bool
    """ Whether this field is required when filling out a PO """
    position: int
    """ Sort order within the section (0-based) """
    computed: bool
    """ Whether this field is auto-calculated """
    locked: bool
    """ Whether this field's mandatory flag is locked (cannot be toggled by admins) """
    visible_in_pdf: bool
    """ Whether this field appears in the PDF export """
    created_at: str
    """ When this field definition was created """
    updated_at: str
    """ When this field definition was last updated """
    field_key: str | Unset = UNSET
    """ Stable machine key identifying the field within its version, unique per version. This is the key used to
    supply the field's value when creating or updating a purchase order via the API. May be null only for legacy
    rows created before the key became mandatory.
     """
    options: list[str] | Unset = UNSET
    """ Closed list of allowed values for a "select" field_type (array of strings). Null for every other field_type.
    When present, a purchase order value for this field must be one of these strings.
     """
    default_value: str | Unset = UNSET
    """ Default value for this field """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        po_template_version_id = self.po_template_version_id

        company_id = self.company_id

        section_type = self.section_type

        label = self.label

        field_type = self.field_type

        predefined = self.predefined

        visible = self.visible

        required = self.required

        position = self.position

        computed = self.computed

        locked = self.locked

        visible_in_pdf = self.visible_in_pdf

        created_at = self.created_at

        updated_at = self.updated_at

        field_key = self.field_key

        options: list[str] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        default_value = self.default_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "po_template_version_id": po_template_version_id,
                "company_id": company_id,
                "section_type": section_type,
                "label": label,
                "field_type": field_type,
                "predefined": predefined,
                "visible": visible,
                "required": required,
                "position": position,
                "computed": computed,
                "locked": locked,
                "visible_in_pdf": visible_in_pdf,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if field_key is not UNSET:
            field_dict["field_key"] = field_key
        if options is not UNSET:
            field_dict["options"] = options
        if default_value is not UNSET:
            field_dict["default_value"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        po_template_version_id = d.pop("po_template_version_id")

        company_id = d.pop("company_id")

        section_type = d.pop("section_type")

        label = d.pop("label")

        field_type = d.pop("field_type")

        predefined = d.pop("predefined")

        visible = d.pop("visible")

        required = d.pop("required")

        position = d.pop("position")

        computed = d.pop("computed")

        locked = d.pop("locked")

        visible_in_pdf = d.pop("visible_in_pdf")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        field_key = d.pop("field_key", UNSET)

        options = cast(list[str], d.pop("options", UNSET))

        default_value = d.pop("default_value", UNSET)

        procurement_po_template_field_definition = cls(
            id=id,
            po_template_version_id=po_template_version_id,
            company_id=company_id,
            section_type=section_type,
            label=label,
            field_type=field_type,
            predefined=predefined,
            visible=visible,
            required=required,
            position=position,
            computed=computed,
            locked=locked,
            visible_in_pdf=visible_in_pdf,
            created_at=created_at,
            updated_at=updated_at,
            field_key=field_key,
            options=options,
            default_value=default_value,
        )

        procurement_po_template_field_definition.additional_properties = d
        return procurement_po_template_field_definition

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
