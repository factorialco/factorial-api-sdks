from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contracts_materialized_template_template_item_edit_mode import (
    ContractsMaterializedTemplateTemplateItemEditMode,
)
from ..models.contracts_materialized_template_template_item_field_type import (
    ContractsMaterializedTemplateTemplateItemFieldType,
)
from ..models.contracts_materialized_template_template_item_source_level import (
    ContractsMaterializedTemplateTemplateItemSourceLevel,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contracts_materialized_template_template_item_dependencies_item import (
        ContractsMaterializedTemplateTemplateItemDependenciesItem,
    )
    from ..models.contracts_materialized_template_template_item_options_item import (
        ContractsMaterializedTemplateTemplateItemOptionsItem,
    )


T = TypeVar("T", bound="ContractsMaterializedTemplateTemplateItem")


@_attrs_define
class ContractsMaterializedTemplateTemplateItem:
    id: str
    field_id: str
    label: str
    field_type: ContractsMaterializedTemplateTemplateItemFieldType
    edit_mode: ContractsMaterializedTemplateTemplateItemEditMode
    dependencies: list[ContractsMaterializedTemplateTemplateItemDependenciesItem]
    source_level: ContractsMaterializedTemplateTemplateItemSourceLevel | Unset = UNSET
    options: list[ContractsMaterializedTemplateTemplateItemOptionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_id = self.field_id

        label = self.label

        field_type = self.field_type.value

        edit_mode = self.edit_mode.value

        dependencies = []
        for dependencies_item_data in self.dependencies:
            dependencies_item = dependencies_item_data.to_dict()
            dependencies.append(dependencies_item)

        source_level: str | Unset = UNSET
        if not isinstance(self.source_level, Unset):
            source_level = self.source_level.value if self.source_level is not None else None

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "field_id": field_id,
                "label": label,
                "field_type": field_type,
                "edit_mode": edit_mode,
                "dependencies": dependencies,
            }
        )
        if source_level is not UNSET:
            field_dict["source_level"] = source_level
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contracts_materialized_template_template_item_dependencies_item import (
            ContractsMaterializedTemplateTemplateItemDependenciesItem,
        )
        from ..models.contracts_materialized_template_template_item_options_item import (
            ContractsMaterializedTemplateTemplateItemOptionsItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        field_id = d.pop("field_id")

        label = d.pop("label")

        field_type = ContractsMaterializedTemplateTemplateItemFieldType(d.pop("field_type"))

        edit_mode = ContractsMaterializedTemplateTemplateItemEditMode(d.pop("edit_mode"))

        dependencies = []
        _dependencies = d.pop("dependencies")
        for dependencies_item_data in _dependencies:
            dependencies_item = ContractsMaterializedTemplateTemplateItemDependenciesItem.from_dict(
                dependencies_item_data
            )

            dependencies.append(dependencies_item)

        _source_level = d.pop("source_level", UNSET)
        source_level: ContractsMaterializedTemplateTemplateItemSourceLevel | Unset
        if isinstance(_source_level, Unset):
            source_level = UNSET
        else:
            source_level = ContractsMaterializedTemplateTemplateItemSourceLevel(_source_level) if _source_level is not None else None

        _options = d.pop("options", UNSET)
        options: list[ContractsMaterializedTemplateTemplateItemOptionsItem] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = ContractsMaterializedTemplateTemplateItemOptionsItem.from_dict(
                    options_item_data
                )

                options.append(options_item)

        contracts_materialized_template_template_item = cls(
            id=id,
            field_id=field_id,
            label=label,
            field_type=field_type,
            edit_mode=edit_mode,
            dependencies=dependencies,
            source_level=source_level,
            options=options,
        )

        contracts_materialized_template_template_item.additional_properties = d
        return contracts_materialized_template_template_item

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
