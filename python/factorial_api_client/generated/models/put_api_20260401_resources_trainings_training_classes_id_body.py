from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20260401_resources_trainings_training_classes_id_body_payment_status import (
    PutApi20260401ResourcesTrainingsTrainingClassesIdBodyPaymentStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesTrainingsTrainingClassesIdBody")


@_attrs_define
class PutApi20260401ResourcesTrainingsTrainingClassesIdBody:
    id: int
    """ Identifier of the training class to update """
    cost: str
    """ Training-related expenses, such as instructor fees, materials, venue, and logistics. """
    subsidized_cost: str
    """ Amount of training expenses covered by financial aid or grants for this group. """
    salary_cost: str
    """ Cost of all employees' time spent on the course. """
    indirect_cost: str
    """ General business expenses related to training, such as utilities and administrative fees. """
    payment_status: PutApi20260401ResourcesTrainingsTrainingClassesIdBodyPaymentStatus
    """ Payment status of the training class. """
    name: str | Unset = UNSET
    """ Class name """
    description: str | Unset = UNSET
    """ Class description """
    start_date: str | Unset = UNSET
    """ Traning class start date """
    end_date: str | Unset = UNSET
    """ Traning class end date """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        cost = self.cost

        subsidized_cost = self.subsidized_cost

        salary_cost = self.salary_cost

        indirect_cost = self.indirect_cost

        payment_status = self.payment_status.value

        name = self.name

        description = self.description

        start_date = self.start_date

        end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "cost": cost,
                "subsidized_cost": subsidized_cost,
                "salary_cost": salary_cost,
                "indirect_cost": indirect_cost,
                "payment_status": payment_status,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        cost = d.pop("cost")

        subsidized_cost = d.pop("subsidized_cost")

        salary_cost = d.pop("salary_cost")

        indirect_cost = d.pop("indirect_cost")

        payment_status = PutApi20260401ResourcesTrainingsTrainingClassesIdBodyPaymentStatus(
            d.pop("payment_status")
        )

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        put_api_20260401_resources_trainings_training_classes_id_body = cls(
            id=id,
            cost=cost,
            subsidized_cost=subsidized_cost,
            salary_cost=salary_cost,
            indirect_cost=indirect_cost,
            payment_status=payment_status,
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
        )

        put_api_20260401_resources_trainings_training_classes_id_body.additional_properties = d
        return put_api_20260401_resources_trainings_training_classes_id_body

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
