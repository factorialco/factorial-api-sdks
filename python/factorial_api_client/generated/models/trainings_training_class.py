from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingsTrainingClass")


@_attrs_define
class TrainingsTrainingClass:
    id: str
    """ Identifier of the training to which the class belongs to """
    training_id: int
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
    description: str | Unset = UNSET
    """ Class description """
    start_date: str | Unset = UNSET
    """ Traning class start date """
    end_date: str | Unset = UNSET
    """ Traning class end date """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        training_id = self.training_id

        name = self.name

        cost = self.cost

        indirect_cost = self.indirect_cost

        salary_cost = self.salary_cost

        subsidized_cost = self.subsidized_cost

        description = self.description

        start_date = self.start_date

        end_date = self.end_date

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
            }
        )
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

        training_id = d.pop("training_id")

        name = d.pop("name")

        cost = d.pop("cost")

        indirect_cost = d.pop("indirect_cost")

        salary_cost = d.pop("salary_cost")

        subsidized_cost = d.pop("subsidized_cost")

        description = d.pop("description", UNSET)

        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        trainings_training_class = cls(
            id=id,
            training_id=training_id,
            name=name,
            cost=cost,
            indirect_cost=indirect_cost,
            salary_cost=salary_cost,
            subsidized_cost=subsidized_cost,
            description=description,
            start_date=start_date,
            end_date=end_date,
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
