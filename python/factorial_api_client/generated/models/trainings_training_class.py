from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trainings_training_class_payment_status import TrainingsTrainingClassPaymentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingsTrainingClass")


@_attrs_define
class TrainingsTrainingClass:
    id: str
    """ Identifier of the training to which the class belongs to """
    training_id: str
    """ Identifier of the course """
    name: str
    """ Class name """
    cost: str
    """ Training-related expenses, such as instructor fees, materials, venue, and logistics. """
    indirect_cost: str
    """ General business expenses related to training, such as utilities and administrative fees. """
    salary_cost: str
    """ Cost of all employees' time spent on the course. """
    subsidized_cost: str
    """ Amount of training expenses covered by financial aid or grants for this group. """
    gross_cost: str
    """ Total cost before subsidies, calculated as the sum of cost, indirect_cost, and salary_cost. """
    net_cost: str
    """ Final cost after subsidies, calculated as gross_cost minus subsidized_cost. """
    completed_attendances_count: int
    """ Number of completed session attendances in this group. """
    total_attendances_count: int
    """ Total number of session attendances expected in this group. """
    currency: str
    """ Currency of the training class """
    created_at: str
    """ Date and time when the training class was created """
    description: str | Unset = UNSET
    """ Class description """
    start_date: str | Unset = UNSET
    """ Traning class start date """
    end_date: str | Unset = UNSET
    """ Traning class end date """
    payment_status: TrainingsTrainingClassPaymentStatus | Unset = UNSET
    """ Payment status of the cost of training class. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        training_id = self.training_id

        name = self.name

        cost = self.cost

        indirect_cost = self.indirect_cost

        salary_cost = self.salary_cost

        subsidized_cost = self.subsidized_cost

        gross_cost = self.gross_cost

        net_cost = self.net_cost

        completed_attendances_count = self.completed_attendances_count

        total_attendances_count = self.total_attendances_count

        currency = self.currency

        created_at = self.created_at

        description = self.description

        start_date = self.start_date

        end_date = self.end_date

        payment_status: str | Unset = UNSET
        if not isinstance(self.payment_status, Unset):
            payment_status = self.payment_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "training_id": training_id,
                "name": name,
                "cost": cost,
                "indirect_cost": indirect_cost,
                "salary_cost": salary_cost,
                "subsidized_cost": subsidized_cost,
                "gross_cost": gross_cost,
                "net_cost": net_cost,
                "completed_attendances_count": completed_attendances_count,
                "total_attendances_count": total_attendances_count,
                "currency": currency,
                "created_at": created_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if payment_status is not UNSET:
            field_dict["payment_status"] = payment_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        training_id = d.pop("training_id")

        name = d.pop("name")

        cost = d.pop("cost")

        indirect_cost = d.pop("indirect_cost")

        salary_cost = d.pop("salary_cost")

        subsidized_cost = d.pop("subsidized_cost")

        gross_cost = d.pop("gross_cost")

        net_cost = d.pop("net_cost")

        completed_attendances_count = d.pop("completed_attendances_count")

        total_attendances_count = d.pop("total_attendances_count")

        currency = d.pop("currency")

        created_at = d.pop("created_at")

        description = d.pop("description", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        _payment_status = d.pop("payment_status", UNSET)
        payment_status: TrainingsTrainingClassPaymentStatus | Unset
        if isinstance(_payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = TrainingsTrainingClassPaymentStatus(_payment_status) if _payment_status is not None else None

        trainings_training_class = cls(
            id=id,
            training_id=training_id,
            name=name,
            cost=cost,
            indirect_cost=indirect_cost,
            salary_cost=salary_cost,
            subsidized_cost=subsidized_cost,
            gross_cost=gross_cost,
            net_cost=net_cost,
            completed_attendances_count=completed_attendances_count,
            total_attendances_count=total_attendances_count,
            currency=currency,
            created_at=created_at,
            description=description,
            start_date=start_date,
            end_date=end_date,
            payment_status=payment_status,
        )

        trainings_training_class.additional_properties = d
        return trainings_training_class

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
