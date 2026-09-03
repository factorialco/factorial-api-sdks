from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcurementPoTemplateVersion")


@_attrs_define
class ProcurementPoTemplateVersion:
    id: str
    """ The id of the PO template version """
    po_template_id: str
    """ The PO template this version belongs to """
    company_id: str
    """ Identifier of the company that owns this version """
    version_number: int
    """ The sequential version number """
    status: str
    """ Version status (draft, active, archived) """
    created_at: str
    """ When this version was created """
    updated_at: str
    """ When this version was last updated """
    based_on_version_id: str | Unset = UNSET
    """ The version this was forked from (null for original) """
    created_by_id: str | Unset = UNSET
    """ Employee ID who created this version """
    published_by_id: str | Unset = UNSET
    """ Employee ID who published this version (null if not published) """
    published_at: str | Unset = UNSET
    """ When this version was published (null if not published) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        po_template_id = self.po_template_id

        company_id = self.company_id

        version_number = self.version_number

        status = self.status

        created_at = self.created_at

        updated_at = self.updated_at

        based_on_version_id = self.based_on_version_id

        created_by_id = self.created_by_id

        published_by_id = self.published_by_id

        published_at = self.published_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "po_template_id": po_template_id,
                "company_id": company_id,
                "version_number": version_number,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if based_on_version_id is not UNSET:
            field_dict["based_on_version_id"] = based_on_version_id
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if published_by_id is not UNSET:
            field_dict["published_by_id"] = published_by_id
        if published_at is not UNSET:
            field_dict["published_at"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        po_template_id = d.pop("po_template_id")

        company_id = d.pop("company_id")

        version_number = d.pop("version_number")

        status = d.pop("status")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        based_on_version_id = d.pop("based_on_version_id", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        published_by_id = d.pop("published_by_id", UNSET)

        published_at = d.pop("published_at", UNSET)

        procurement_po_template_version = cls(
            id=id,
            po_template_id=po_template_id,
            company_id=company_id,
            version_number=version_number,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            based_on_version_id=based_on_version_id,
            created_by_id=created_by_id,
            published_by_id=published_by_id,
            published_at=published_at,
        )

        procurement_po_template_version.additional_properties = d
        return procurement_po_template_version

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
