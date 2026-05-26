from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesTrainingsTrainingsBody")


@_attrs_define
class PostApi20251001ResourcesTrainingsTrainingsBody:
    name: str
    """ Name of the training """
    description: str
    """ Description of the training """
    external: bool
    """ External training """
    year: int
    """ Year of the training """
    attachments: list[Any]
    """ Attachments of the training """
    code: str | Unset = UNSET
    """ Code of the training """
    external_provider: str | Unset = UNSET
    """ External provider of the training """
    category_ids: list[int] | Unset = UNSET
    competency_ids: list[int] | Unset = UNSET
    """ Competency ids of the training """
    author_id: int | Unset = UNSET
    """ The person that creates the training """
    employee_id: int | Unset = UNSET
    cost: int | Unset = UNSET
    subsidized_cost: int | Unset = UNSET
    cost_decimal: str | Unset = UNSET
    subsidized_cost_decimal: str | Unset = UNSET
    company_id: int | Unset = UNSET
    """ Company identifier of the training """
    valid_for: int | Unset = UNSET
    """ The training validity period in years """
    objectives: str | Unset = UNSET
    """ Objectives of the course """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        external = self.external

        year = self.year

        attachments = self.attachments

        code = self.code

        external_provider = self.external_provider

        category_ids: list[int] | Unset = UNSET
        if not isinstance(self.category_ids, Unset):
            category_ids = self.category_ids

        competency_ids: list[int] | Unset = UNSET
        if not isinstance(self.competency_ids, Unset):
            competency_ids = self.competency_ids

        author_id = self.author_id

        employee_id = self.employee_id

        cost = self.cost

        subsidized_cost = self.subsidized_cost

        cost_decimal = self.cost_decimal

        subsidized_cost_decimal = self.subsidized_cost_decimal

        company_id = self.company_id

        valid_for = self.valid_for

        objectives = self.objectives

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "external": external,
                "year": year,
                "attachments": attachments,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if external_provider is not UNSET:
            field_dict["external_provider"] = external_provider
        if category_ids is not UNSET:
            field_dict["category_ids"] = category_ids
        if competency_ids is not UNSET:
            field_dict["competency_ids"] = competency_ids
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if cost is not UNSET:
            field_dict["cost"] = cost
        if subsidized_cost is not UNSET:
            field_dict["subsidized_cost"] = subsidized_cost
        if cost_decimal is not UNSET:
            field_dict["cost_decimal"] = cost_decimal
        if subsidized_cost_decimal is not UNSET:
            field_dict["subsidized_cost_decimal"] = subsidized_cost_decimal
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if valid_for is not UNSET:
            field_dict["valid_for"] = valid_for
        if objectives is not UNSET:
            field_dict["objectives"] = objectives

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        external = d.pop("external")

        year = d.pop("year")

        attachments = cast(list[Any], d.pop("attachments"))

        code = d.pop("code", UNSET)

        external_provider = d.pop("external_provider", UNSET)

        category_ids = cast(list[int], d.pop("category_ids", UNSET))

        competency_ids = cast(list[int], d.pop("competency_ids", UNSET))

        author_id = d.pop("author_id", UNSET)

        employee_id = d.pop("employee_id", UNSET)

        cost = d.pop("cost", UNSET)

        subsidized_cost = d.pop("subsidized_cost", UNSET)

        cost_decimal = d.pop("cost_decimal", UNSET)

        subsidized_cost_decimal = d.pop("subsidized_cost_decimal", UNSET)

        company_id = d.pop("company_id", UNSET)

        valid_for = d.pop("valid_for", UNSET)

        objectives = d.pop("objectives", UNSET)

        post_api_20251001_resources_trainings_trainings_body = cls(
            name=name,
            description=description,
            external=external,
            year=year,
            attachments=attachments,
            code=code,
            external_provider=external_provider,
            category_ids=category_ids,
            competency_ids=competency_ids,
            author_id=author_id,
            employee_id=employee_id,
            cost=cost,
            subsidized_cost=subsidized_cost,
            cost_decimal=cost_decimal,
            subsidized_cost_decimal=subsidized_cost_decimal,
            company_id=company_id,
            valid_for=valid_for,
            objectives=objectives,
        )

        post_api_20251001_resources_trainings_trainings_body.additional_properties = d
        return post_api_20251001_resources_trainings_trainings_body

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
