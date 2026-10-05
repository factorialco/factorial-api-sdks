from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_compensations_payroll_results_bulk_create_body_results_item import (
        PostApi20261001ResourcesCompensationsPayrollResultsBulkCreateBodyResultsItem,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesCompensationsPayrollResultsBulkCreateBody")


@_attrs_define
class PostApi20261001ResourcesCompensationsPayrollResultsBulkCreateBody:
    payroll_run_id: str
    """ Parent payroll run id, refers to compensations/payroll_runs endpoint. The run must already exist; find it
    through compensations/cycles and compensations/payroll_runs. """
    results: list[PostApi20261001ResourcesCompensationsPayrollResultsBulkCreateBodyResultsItem]
    """ One entry per employee (maximum 1000 amounts in total per request) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payroll_run_id = self.payroll_run_id

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payroll_run_id": payroll_run_id,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_compensations_payroll_results_bulk_create_body_results_item import (
            PostApi20261001ResourcesCompensationsPayrollResultsBulkCreateBodyResultsItem,
        )

        d = dict(src_dict)
        payroll_run_id = d.pop("payroll_run_id")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = PostApi20261001ResourcesCompensationsPayrollResultsBulkCreateBodyResultsItem.from_dict(
                results_item_data
            )

            results.append(results_item)

        post_api_20261001_resources_compensations_payroll_results_bulk_create_body = cls(
            payroll_run_id=payroll_run_id,
            results=results,
        )

        post_api_20261001_resources_compensations_payroll_results_bulk_create_body.additional_properties = d
        return post_api_20261001_resources_compensations_payroll_results_bulk_create_body

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
