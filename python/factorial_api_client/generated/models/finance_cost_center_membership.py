from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinanceCostCenterMembership")


@_attrs_define
class FinanceCostCenterMembership:
    id: str
    """ The unique identifier of the cost center membership """
    employee_id: str
    """ The identifier of the associated employee """
    cost_center_id: str
    """ The identifier of the associated cost center """
    start_date: str
    """ The date the employee started being assigned to the cost center """
    percentage: float
    """ The percentage allocation of the employee to the cost center """
    end_date: str | Unset = UNSET
    """ The date the em'ployee stopped being assigned to the cost center """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        cost_center_id = self.cost_center_id

        start_date = self.start_date

        percentage = self.percentage

        end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "employee_id": employee_id,
                "cost_center_id": cost_center_id,
                "start_date": start_date,
                "percentage": percentage,
            }
        )
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        employee_id = d.pop("employee_id")

        cost_center_id = d.pop("cost_center_id")

        start_date = d.pop("start_date")

        percentage = d.pop("percentage")

        end_date = d.pop("end_date", UNSET)

        finance_cost_center_membership = cls(
            id=id,
            employee_id=employee_id,
            cost_center_id=cost_center_id,
            start_date=start_date,
            percentage=percentage,
            end_date=end_date,
        )

        finance_cost_center_membership.additional_properties = d
        return finance_cost_center_membership

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
