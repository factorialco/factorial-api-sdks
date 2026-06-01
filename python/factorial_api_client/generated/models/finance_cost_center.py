from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinanceCostCenter")


@_attrs_define
class FinanceCostCenter:
    id: int
    name: str
    company_id: int
    active_employees_count: int
    historical_employees_count: int
    status: str
    legal_entity_id: int | Unset = UNSET
    code: str | Unset = UNSET
    description: str | Unset = UNSET
    deactivation_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        company_id = self.company_id

        active_employees_count = self.active_employees_count

        historical_employees_count = self.historical_employees_count

        status = self.status

        legal_entity_id = self.legal_entity_id

        code = self.code

        description = self.description

        deactivation_date = self.deactivation_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "company_id": company_id,
                "active_employees_count": active_employees_count,
                "historical_employees_count": historical_employees_count,
                "status": status,
            }
        )
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if deactivation_date is not UNSET:
            field_dict["deactivation_date"] = deactivation_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        company_id = d.pop("company_id")

        active_employees_count = d.pop("active_employees_count")

        historical_employees_count = d.pop("historical_employees_count")

        status = d.pop("status")

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        deactivation_date = d.pop("deactivation_date", UNSET)

        finance_cost_center = cls(
            id=id,
            name=name,
            company_id=company_id,
            active_employees_count=active_employees_count,
            historical_employees_count=historical_employees_count,
            status=status,
            legal_entity_id=legal_entity_id,
            code=code,
            description=description,
            deactivation_date=deactivation_date,
        )

        finance_cost_center.additional_properties = d
        return finance_cost_center

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
