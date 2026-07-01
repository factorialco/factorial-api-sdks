from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_catalog_node_attribute_value_competency import (
        JobCatalogNodeAttributeValueCompetency,
    )
    from ..models.job_catalog_node_attribute_value_it_management_asset import (
        JobCatalogNodeAttributeValueItManagementAsset,
    )
    from ..models.job_catalog_node_attribute_value_salary_range import (
        JobCatalogNodeAttributeValueSalaryRange,
    )
    from ..models.job_catalog_node_attribute_value_working_conditions import (
        JobCatalogNodeAttributeValueWorkingConditions,
    )


T = TypeVar("T", bound="JobCatalogNodeAttribute")


@_attrs_define
class JobCatalogNodeAttribute:
    id: str
    """ Unique identifier of the node attribute """
    type_: str
    """ Type of the attribute (e.g., competency, salary_range, working_conditions, it_management_asset) """
    attribute_id: str | Unset = UNSET
    """ Identifier of the attribute being assigned to the node it it makes sense like in competecies, but not for
    working_conditions """
    value_competency: JobCatalogNodeAttributeValueCompetency | Unset = UNSET
    """ Competency payload including name, short description and optional level metadata """
    value_it_management_asset: JobCatalogNodeAttributeValueItManagementAsset | Unset = UNSET
    """ IT asset payload describing the device assigned to the node """
    value_salary_range: JobCatalogNodeAttributeValueSalaryRange | Unset = UNSET
    """ Salary payload (cents) with currency, periodicity, range (min and max) or gross values in cents (35.000 EUR
    is stored as 3500000) and optional workplaces """
    value_working_conditions: JobCatalogNodeAttributeValueWorkingConditions | Unset = UNSET
    """ Working-conditions payload with agreement info and simple key/value constraints. Numeric values are stored
    in cents (40 hours is stored as 4000). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        attribute_id = self.attribute_id

        value_competency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_competency, Unset):
            value_competency = self.value_competency.to_dict()

        value_it_management_asset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_it_management_asset, Unset):
            value_it_management_asset = self.value_it_management_asset.to_dict()

        value_salary_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_salary_range, Unset):
            value_salary_range = self.value_salary_range.to_dict()

        value_working_conditions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_working_conditions, Unset):
            value_working_conditions = self.value_working_conditions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if attribute_id is not UNSET:
            field_dict["attribute_id"] = attribute_id
        if value_competency is not UNSET:
            field_dict["value_competency"] = value_competency
        if value_it_management_asset is not UNSET:
            field_dict["value_it_management_asset"] = value_it_management_asset
        if value_salary_range is not UNSET:
            field_dict["value_salary_range"] = value_salary_range
        if value_working_conditions is not UNSET:
            field_dict["value_working_conditions"] = value_working_conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_catalog_node_attribute_value_competency import (
            JobCatalogNodeAttributeValueCompetency,
        )
        from ..models.job_catalog_node_attribute_value_it_management_asset import (
            JobCatalogNodeAttributeValueItManagementAsset,
        )
        from ..models.job_catalog_node_attribute_value_salary_range import (
            JobCatalogNodeAttributeValueSalaryRange,
        )
        from ..models.job_catalog_node_attribute_value_working_conditions import (
            JobCatalogNodeAttributeValueWorkingConditions,
        )

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        attribute_id = d.pop("attribute_id", UNSET)

        _value_competency = d.pop("value_competency", UNSET)
        value_competency: JobCatalogNodeAttributeValueCompetency | Unset
        if isinstance(_value_competency, Unset):
            value_competency = UNSET
        else:
            value_competency = JobCatalogNodeAttributeValueCompetency.from_dict(_value_competency)

        _value_it_management_asset = d.pop("value_it_management_asset", UNSET)
        value_it_management_asset: JobCatalogNodeAttributeValueItManagementAsset | Unset
        if isinstance(_value_it_management_asset, Unset):
            value_it_management_asset = UNSET
        else:
            value_it_management_asset = JobCatalogNodeAttributeValueItManagementAsset.from_dict(
                _value_it_management_asset
            )

        _value_salary_range = d.pop("value_salary_range", UNSET)
        value_salary_range: JobCatalogNodeAttributeValueSalaryRange | Unset
        if isinstance(_value_salary_range, Unset):
            value_salary_range = UNSET
        else:
            value_salary_range = JobCatalogNodeAttributeValueSalaryRange.from_dict(
                _value_salary_range
            )

        _value_working_conditions = d.pop("value_working_conditions", UNSET)
        value_working_conditions: JobCatalogNodeAttributeValueWorkingConditions | Unset
        if isinstance(_value_working_conditions, Unset):
            value_working_conditions = UNSET
        else:
            value_working_conditions = JobCatalogNodeAttributeValueWorkingConditions.from_dict(
                _value_working_conditions
            )

        job_catalog_node_attribute = cls(
            id=id,
            type_=type_,
            attribute_id=attribute_id,
            value_competency=value_competency,
            value_it_management_asset=value_it_management_asset,
            value_salary_range=value_salary_range,
            value_working_conditions=value_working_conditions,
        )

        job_catalog_node_attribute.additional_properties = d
        return job_catalog_node_attribute

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
