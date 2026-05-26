from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trainings_training_status import TrainingsTrainingStatus
from ..models.trainings_training_training_attendance_status import (
    TrainingsTrainingTrainingAttendanceStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingsTraining")


@_attrs_define
class TrainingsTraining:
    id: int
    """ Identifier of the course """
    company_id: int
    """ Company identifier """
    author_id: int
    """ The person that creates the training """
    name: str
    """ Name of the training """
    description: str
    """ Description of the training """
    external: bool
    """ External training """
    fundae_subsidized: bool
    """ Subsidized by Fundae """
    subsidized: bool
    """ Marked as subsidized """
    cost: int
    subsidized_cost: int
    cost_decimal: str
    subsidized_cost_decimal: str
    year: int
    """ Year of the training """
    catalog: bool
    """ Visible in catalog """
    competency_ids: list[int]
    """ List of ids of training competencies """
    total_training_cost: str
    """ The total direct cost of all course's groups """
    total_training_indirect_cost: str
    """ The total indirect cost of all course's groups """
    total_training_salary_cost: str
    """ The total salary cost of all course's groups """
    total_training_subsidized_cost: str
    """ The total subsidized cost of all course's groups """
    total_participants: int
    """ Number of participants of all course's groups """
    training_attendance_status: TrainingsTrainingTrainingAttendanceStatus
    code: str | Unset = UNSET
    """ Code of the training """
    created_at: str | Unset = UNSET
    """ Creation date of the course """
    updated_at: str | Unset = UNSET
    """ Last modification date of the course """
    external_provider: str | Unset = UNSET
    """ The name of the provider if any """
    total_cost: int | Unset = UNSET
    total_cost_decimal: str | Unset = UNSET
    category_ids: list[int] | Unset = UNSET
    """ List of ids of training categories """
    status: TrainingsTrainingStatus | Unset = UNSET
    """ Training status. Can be one of the following values """
    valid_for: int | Unset = UNSET
    """ Number of years this course is valid for """
    objectives: str | Unset = UNSET
    """ Objectives of the course """
    number_of_expired_participants: int | Unset = UNSET
    """ Number of participants that have the course expired or about to expire in the next 3 months. Only applicable
    to trainings with validity period. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        author_id = self.author_id

        name = self.name

        description = self.description

        external = self.external

        fundae_subsidized = self.fundae_subsidized

        subsidized = self.subsidized

        cost = self.cost

        subsidized_cost = self.subsidized_cost

        cost_decimal = self.cost_decimal

        subsidized_cost_decimal = self.subsidized_cost_decimal

        year = self.year

        catalog = self.catalog

        competency_ids = self.competency_ids

        total_training_cost = self.total_training_cost

        total_training_indirect_cost = self.total_training_indirect_cost

        total_training_salary_cost = self.total_training_salary_cost

        total_training_subsidized_cost = self.total_training_subsidized_cost

        total_participants = self.total_participants

        training_attendance_status = self.training_attendance_status.value

        code = self.code

        created_at = self.created_at

        updated_at = self.updated_at

        external_provider = self.external_provider

        total_cost = self.total_cost

        total_cost_decimal = self.total_cost_decimal

        category_ids: list[int] | Unset = UNSET
        if not isinstance(self.category_ids, Unset):
            category_ids = self.category_ids

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        valid_for = self.valid_for

        objectives = self.objectives

        number_of_expired_participants = self.number_of_expired_participants

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "author_id": author_id,
                "name": name,
                "description": description,
                "external": external,
                "fundae_subsidized": fundae_subsidized,
                "subsidized": subsidized,
                "cost": cost,
                "subsidized_cost": subsidized_cost,
                "cost_decimal": cost_decimal,
                "subsidized_cost_decimal": subsidized_cost_decimal,
                "year": year,
                "catalog": catalog,
                "competency_ids": competency_ids,
                "total_training_cost": total_training_cost,
                "total_training_indirect_cost": total_training_indirect_cost,
                "total_training_salary_cost": total_training_salary_cost,
                "total_training_subsidized_cost": total_training_subsidized_cost,
                "total_participants": total_participants,
                "training_attendance_status": training_attendance_status,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if external_provider is not UNSET:
            field_dict["external_provider"] = external_provider
        if total_cost is not UNSET:
            field_dict["total_cost"] = total_cost
        if total_cost_decimal is not UNSET:
            field_dict["total_cost_decimal"] = total_cost_decimal
        if category_ids is not UNSET:
            field_dict["category_ids"] = category_ids
        if status is not UNSET:
            field_dict["status"] = status
        if valid_for is not UNSET:
            field_dict["valid_for"] = valid_for
        if objectives is not UNSET:
            field_dict["objectives"] = objectives
        if number_of_expired_participants is not UNSET:
            field_dict["number_of_expired_participants"] = number_of_expired_participants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        author_id = d.pop("author_id")

        name = d.pop("name")

        description = d.pop("description")

        external = d.pop("external")

        fundae_subsidized = d.pop("fundae_subsidized")

        subsidized = d.pop("subsidized")

        cost = d.pop("cost")

        subsidized_cost = d.pop("subsidized_cost")

        cost_decimal = d.pop("cost_decimal")

        subsidized_cost_decimal = d.pop("subsidized_cost_decimal")

        year = d.pop("year")

        catalog = d.pop("catalog")

        competency_ids = cast(list[int], d.pop("competency_ids"))

        total_training_cost = d.pop("total_training_cost")

        total_training_indirect_cost = d.pop("total_training_indirect_cost")

        total_training_salary_cost = d.pop("total_training_salary_cost")

        total_training_subsidized_cost = d.pop("total_training_subsidized_cost")

        total_participants = d.pop("total_participants")

        training_attendance_status = TrainingsTrainingTrainingAttendanceStatus(
            d.pop("training_attendance_status")
        )

        code = d.pop("code", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        external_provider = d.pop("external_provider", UNSET)

        total_cost = d.pop("total_cost", UNSET)

        total_cost_decimal = d.pop("total_cost_decimal", UNSET)

        category_ids = cast(list[int], d.pop("category_ids", UNSET))

        _status = d.pop("status", UNSET)
        status: TrainingsTrainingStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TrainingsTrainingStatus(_status) if _status is not None else None

        valid_for = d.pop("valid_for", UNSET)

        objectives = d.pop("objectives", UNSET)

        number_of_expired_participants = d.pop("number_of_expired_participants", UNSET)

        trainings_training = cls(
            id=id,
            company_id=company_id,
            author_id=author_id,
            name=name,
            description=description,
            external=external,
            fundae_subsidized=fundae_subsidized,
            subsidized=subsidized,
            cost=cost,
            subsidized_cost=subsidized_cost,
            cost_decimal=cost_decimal,
            subsidized_cost_decimal=subsidized_cost_decimal,
            year=year,
            catalog=catalog,
            competency_ids=competency_ids,
            total_training_cost=total_training_cost,
            total_training_indirect_cost=total_training_indirect_cost,
            total_training_salary_cost=total_training_salary_cost,
            total_training_subsidized_cost=total_training_subsidized_cost,
            total_participants=total_participants,
            training_attendance_status=training_attendance_status,
            code=code,
            created_at=created_at,
            updated_at=updated_at,
            external_provider=external_provider,
            total_cost=total_cost,
            total_cost_decimal=total_cost_decimal,
            category_ids=category_ids,
            status=status,
            valid_for=valid_for,
            objectives=objectives,
            number_of_expired_participants=number_of_expired_participants,
        )

        trainings_training.additional_properties = d
        return trainings_training

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
