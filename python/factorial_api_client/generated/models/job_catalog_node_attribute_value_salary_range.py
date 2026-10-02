from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_catalog_node_attribute_value_salary_range_workplaces_item import (
        JobCatalogNodeAttributeValueSalaryRangeWorkplacesItem,
    )


T = TypeVar("T", bound="JobCatalogNodeAttributeValueSalaryRange")


@_attrs_define
class JobCatalogNodeAttributeValueSalaryRange:
    """Salary payload (cents) with currency, periodicity, range (min and max) or gross values in cents (35.000 EUR is
    stored as 3500000) and optional workplaces

        Example:
            ['{"currency":"EUR","periodicity":"yearly","min":18000,"max":25000,"workplaces":[{"id":1,"name":"Barcelona
                HQ"}]}', '{"currency":"EUR","periodicity":"yearly","gross":2000000,"workplaces":[{"id":1,"name":"Barcelona
                HQ"}]}']

    """

    currency: str
    periodicity: str | Unset = UNSET
    min_: int | Unset = UNSET
    max_: int | Unset = UNSET
    gross: int | Unset = UNSET
    workplaces: list[JobCatalogNodeAttributeValueSalaryRangeWorkplacesItem] | Unset = UNSET
    """ Workplaces where the salary range applies """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        periodicity = self.periodicity

        min_ = self.min_

        max_ = self.max_

        gross = self.gross

        workplaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workplaces, Unset):
            workplaces = []
            for workplaces_item_data in self.workplaces:
                workplaces_item = workplaces_item_data.to_dict()
                workplaces.append(workplaces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
            }
        )
        if periodicity is not UNSET:
            field_dict["periodicity"] = periodicity
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if gross is not UNSET:
            field_dict["gross"] = gross
        if workplaces is not UNSET:
            field_dict["workplaces"] = workplaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_catalog_node_attribute_value_salary_range_workplaces_item import (
            JobCatalogNodeAttributeValueSalaryRangeWorkplacesItem,
        )

        d = dict(src_dict)
        currency = d.pop("currency")

        periodicity = d.pop("periodicity", UNSET)

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        gross = d.pop("gross", UNSET)

        _workplaces = d.pop("workplaces", UNSET)
        workplaces: list[JobCatalogNodeAttributeValueSalaryRangeWorkplacesItem] | Unset = UNSET
        if _workplaces is not UNSET:
            workplaces = []
            for workplaces_item_data in _workplaces:
                workplaces_item = JobCatalogNodeAttributeValueSalaryRangeWorkplacesItem.from_dict(
                    workplaces_item_data
                )

                workplaces.append(workplaces_item)

        job_catalog_node_attribute_value_salary_range = cls(
            currency=currency,
            periodicity=periodicity,
            min_=min_,
            max_=max_,
            gross=gross,
            workplaces=workplaces,
        )

        job_catalog_node_attribute_value_salary_range.additional_properties = d
        return job_catalog_node_attribute_value_salary_range

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
