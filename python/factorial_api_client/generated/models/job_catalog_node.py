from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_catalog_node_type import JobCatalogNodeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_catalog_node_full_path_to_root_item import JobCatalogNodeFullPathToRootItem


T = TypeVar("T", bound="JobCatalogNode")


@_attrs_define
class JobCatalogNode:
    type_: JobCatalogNodeType
    """ Type of the node. """
    uuid: str
    """ UUIDs of the node. """
    created_at: str
    """ Creation date of the node. """
    updated_at: str
    """ Update date of the node. """
    ancestor_uuid: str | Unset = UNSET
    """ UUID of the parent node. """
    name: str | Unset = UNSET
    """ Name of the node. """
    description: str | Unset = UNSET
    """ Description of the node in the Job Catalog. """
    full_path_to_root: list[JobCatalogNodeFullPathToRootItem] | Unset = UNSET
    """ Array with the list of nodes tha compose full path from the current node to the root node. """
    job_catalog_title: str | Unset = UNSET
    """ Full title that represents the job position. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        uuid = self.uuid

        created_at = self.created_at

        updated_at = self.updated_at

        ancestor_uuid = self.ancestor_uuid

        name = self.name

        description = self.description

        full_path_to_root: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.full_path_to_root, Unset):
            full_path_to_root = []
            for full_path_to_root_item_data in self.full_path_to_root:
                full_path_to_root_item = full_path_to_root_item_data.to_dict()
                full_path_to_root.append(full_path_to_root_item)

        job_catalog_title = self.job_catalog_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "uuid": uuid,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if ancestor_uuid is not UNSET:
            field_dict["ancestor_uuid"] = ancestor_uuid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if full_path_to_root is not UNSET:
            field_dict["full_path_to_root"] = full_path_to_root
        if job_catalog_title is not UNSET:
            field_dict["job_catalog_title"] = job_catalog_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_catalog_node_full_path_to_root_item import (
            JobCatalogNodeFullPathToRootItem,
        )

        d = dict(src_dict)
        type_ = JobCatalogNodeType(d.pop("type"))

        uuid = d.pop("uuid")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        ancestor_uuid = d.pop("ancestor_uuid", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _full_path_to_root = d.pop("full_path_to_root", UNSET)
        full_path_to_root: list[JobCatalogNodeFullPathToRootItem] | Unset = UNSET
        if _full_path_to_root is not UNSET:
            full_path_to_root = []
            for full_path_to_root_item_data in _full_path_to_root:
                full_path_to_root_item = JobCatalogNodeFullPathToRootItem.from_dict(
                    full_path_to_root_item_data
                )

                full_path_to_root.append(full_path_to_root_item)

        job_catalog_title = d.pop("job_catalog_title", UNSET)

        job_catalog_node = cls(
            type_=type_,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
            ancestor_uuid=ancestor_uuid,
            name=name,
            description=description,
            full_path_to_root=full_path_to_root,
            job_catalog_title=job_catalog_title,
        )

        job_catalog_node.additional_properties = d
        return job_catalog_node

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
