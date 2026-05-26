from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApi20260401ResourcesTrainingsTrainingsIdBody")


@_attrs_define
class PutApi20260401ResourcesTrainingsTrainingsIdBody:
    id: int
    name: str
    description: str
    external: bool
    year: int
    code: str | Unset = UNSET
    external_provider: str | Unset = UNSET
    category_ids: list[int] | Unset = UNSET
    competency_ids: list[int] | Unset = UNSET
    cost: int | Unset = UNSET
    subsidized_cost: int | Unset = UNSET
    cost_decimal: str | Unset = UNSET
    subsidized_cost_decimal: str | Unset = UNSET
    valid_for: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        external = self.external

        year = self.year

        code = self.code

        external_provider = self.external_provider

        category_ids: list[int] | Unset = UNSET
        if not isinstance(self.category_ids, Unset):
            category_ids = self.category_ids

        competency_ids: list[int] | Unset = UNSET
        if not isinstance(self.competency_ids, Unset):
            competency_ids = self.competency_ids

        cost = self.cost

        subsidized_cost = self.subsidized_cost

        cost_decimal = self.cost_decimal

        subsidized_cost_decimal = self.subsidized_cost_decimal

        valid_for = self.valid_for

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "external": external,
                "year": year,
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
        if cost is not UNSET:
            field_dict["cost"] = cost
        if subsidized_cost is not UNSET:
            field_dict["subsidized_cost"] = subsidized_cost
        if cost_decimal is not UNSET:
            field_dict["cost_decimal"] = cost_decimal
        if subsidized_cost_decimal is not UNSET:
            field_dict["subsidized_cost_decimal"] = subsidized_cost_decimal
        if valid_for is not UNSET:
            field_dict["valid_for"] = valid_for

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        external = d.pop("external")

        year = d.pop("year")

        code = d.pop("code", UNSET)

        external_provider = d.pop("external_provider", UNSET)

        category_ids = cast(list[int], d.pop("category_ids", UNSET))

        competency_ids = cast(list[int], d.pop("competency_ids", UNSET))

        cost = d.pop("cost", UNSET)

        subsidized_cost = d.pop("subsidized_cost", UNSET)

        cost_decimal = d.pop("cost_decimal", UNSET)

        subsidized_cost_decimal = d.pop("subsidized_cost_decimal", UNSET)

        valid_for = d.pop("valid_for", UNSET)

        put_api_20260401_resources_trainings_trainings_id_body = cls(
            id=id,
            name=name,
            description=description,
            external=external,
            year=year,
            code=code,
            external_provider=external_provider,
            category_ids=category_ids,
            competency_ids=competency_ids,
            cost=cost,
            subsidized_cost=subsidized_cost,
            cost_decimal=cost_decimal,
            subsidized_cost_decimal=subsidized_cost_decimal,
            valid_for=valid_for,
        )

        put_api_20260401_resources_trainings_trainings_id_body.additional_properties = d
        return put_api_20260401_resources_trainings_trainings_id_body

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
