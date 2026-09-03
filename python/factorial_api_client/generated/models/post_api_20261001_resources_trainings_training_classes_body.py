from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_trainings_training_classes_body_payment_status import (
    PostApi20261001ResourcesTrainingsTrainingClassesBodyPaymentStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20261001ResourcesTrainingsTrainingClassesBody")


@_attrs_define
class PostApi20261001ResourcesTrainingsTrainingClassesBody:
    start_date: str
    """ Traning class start date """
    end_date: str
    """ Traning class end date """
    training_id: str
    """ Training the class belongs to """
    company_id: str
    """ Company identifier the class belongs to """
    author_id: str
    """ access_id associated to the employee that creates the training class, refers to employees/employees
    endpoint. """
    cost: str
    """ Training-related expenses, such as instructor fees, materials, venue, and logistics. """
    subsidized_cost: str
    """ Amount of training expenses covered by financial aid or grants for this group. """
    indirect_cost: str
    """ General business expenses related to training, such as utilities and administrative fees. """
    salary_cost: str
    """ Cost of all employees' time spent on the course. """
    payment_status: PostApi20261001ResourcesTrainingsTrainingClassesBodyPaymentStatus
    """ Payment status of the training class. """
    name: str | Unset = UNSET
    """ Class name """
    description: str | Unset = UNSET
    """ Class description """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date

        end_date = self.end_date

        training_id = self.training_id

        company_id = self.company_id

        author_id = self.author_id

        cost = self.cost

        subsidized_cost = self.subsidized_cost

        indirect_cost = self.indirect_cost

        salary_cost = self.salary_cost

        payment_status = self.payment_status.value

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_date": start_date,
                "end_date": end_date,
                "training_id": training_id,
                "company_id": company_id,
                "author_id": author_id,
                "cost": cost,
                "subsidized_cost": subsidized_cost,
                "indirect_cost": indirect_cost,
                "salary_cost": salary_cost,
                "payment_status": payment_status,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        training_id = d.pop("training_id")

        company_id = d.pop("company_id")

        author_id = d.pop("author_id")

        cost = d.pop("cost")

        subsidized_cost = d.pop("subsidized_cost")

        indirect_cost = d.pop("indirect_cost")

        salary_cost = d.pop("salary_cost")

        payment_status = PostApi20261001ResourcesTrainingsTrainingClassesBodyPaymentStatus(
            d.pop("payment_status")
        )

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        post_api_20261001_resources_trainings_training_classes_body = cls(
            start_date=start_date,
            end_date=end_date,
            training_id=training_id,
            company_id=company_id,
            author_id=author_id,
            cost=cost,
            subsidized_cost=subsidized_cost,
            indirect_cost=indirect_cost,
            salary_cost=salary_cost,
            payment_status=payment_status,
            name=name,
            description=description,
        )

        post_api_20261001_resources_trainings_training_classes_body.additional_properties = d
        return post_api_20261001_resources_trainings_training_classes_body

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
