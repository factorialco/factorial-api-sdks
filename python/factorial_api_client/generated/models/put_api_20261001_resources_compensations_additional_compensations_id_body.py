from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20261001_resources_compensations_additional_compensations_id_body_amount_strategy_type import (
    PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBodyAmountStrategyType,
)
from ..models.put_api_20261001_resources_compensations_additional_compensations_id_body_recurrence import (
    PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBodyRecurrence,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_20261001_resources_compensations_additional_compensations_id_body_per_worked_day_definition import (
        PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBodyPerWorkedDayDefinition,
    )


T = TypeVar("T", bound="PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBody")


@_attrs_define
class PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBody:
    id: str
    """ Additional compensation id """
    per_worked_day_definition: (
        PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBodyPerWorkedDayDefinition
    )
    """ Definition object for PerWorkedDay strategies. Same shape as on create — replaces the previous definition
    when supplied. """
    amount_strategy_type: (
        PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBodyAmountStrategyType | Unset
    ) = UNSET
    """ Amount strategy discriminator """
    amount: int | Unset = UNSET
    """ Updated amount value (Fixed and PerWorkedDay strategies) """
    upper_limit: int | Unset = UNSET
    """ Updated upper limit (Variable strategy only) """
    description: str | Unset = UNSET
    """ Free-text description """
    recurrence: (
        PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBodyRecurrence | Unset
    ) = UNSET
    """ Recurrence label. Same enum as on create. """
    first_payment_on: str | Unset = UNSET
    """ Date of the first payment """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        per_worked_day_definition = self.per_worked_day_definition.to_dict()

        amount_strategy_type: str | Unset = UNSET
        if not isinstance(self.amount_strategy_type, Unset):
            amount_strategy_type = self.amount_strategy_type.value if self.amount_strategy_type is not None else None

        amount = self.amount

        upper_limit = self.upper_limit

        description = self.description

        recurrence: str | Unset = UNSET
        if not isinstance(self.recurrence, Unset):
            recurrence = self.recurrence.value if self.recurrence is not None else None

        first_payment_on = self.first_payment_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "per_worked_day_definition": per_worked_day_definition,
            }
        )
        if amount_strategy_type is not UNSET:
            field_dict["amount_strategy_type"] = amount_strategy_type
        if amount is not UNSET:
            field_dict["amount"] = amount
        if upper_limit is not UNSET:
            field_dict["upper_limit"] = upper_limit
        if description is not UNSET:
            field_dict["description"] = description
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if first_payment_on is not UNSET:
            field_dict["first_payment_on"] = first_payment_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_api_20261001_resources_compensations_additional_compensations_id_body_per_worked_day_definition import (
            PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBodyPerWorkedDayDefinition,
        )

        d = dict(src_dict)
        id = d.pop("id")

        per_worked_day_definition = PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBodyPerWorkedDayDefinition.from_dict(
            d.pop("per_worked_day_definition")
        )

        _amount_strategy_type = d.pop("amount_strategy_type", UNSET)
        amount_strategy_type: (
            PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBodyAmountStrategyType
            | Unset
        )
        if isinstance(_amount_strategy_type, Unset):
            amount_strategy_type = UNSET
        else:
            amount_strategy_type = (
                PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBodyAmountStrategyType(
                    _amount_strategy_type
                )
            )

        amount = d.pop("amount", UNSET)

        upper_limit = d.pop("upper_limit", UNSET)

        description = d.pop("description", UNSET)

        _recurrence = d.pop("recurrence", UNSET)
        recurrence: (
            PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBodyRecurrence | Unset
        )
        if isinstance(_recurrence, Unset):
            recurrence = UNSET
        else:
            recurrence = (
                PutApi20261001ResourcesCompensationsAdditionalCompensationsIdBodyRecurrence(
                    _recurrence
                ) if _recurrence is not None else None
            )

        first_payment_on = d.pop("first_payment_on", UNSET)

        put_api_20261001_resources_compensations_additional_compensations_id_body = cls(
            id=id,
            per_worked_day_definition=per_worked_day_definition,
            amount_strategy_type=amount_strategy_type,
            amount=amount,
            upper_limit=upper_limit,
            description=description,
            recurrence=recurrence,
            first_payment_on=first_payment_on,
        )

        put_api_20261001_resources_compensations_additional_compensations_id_body.additional_properties = d
        return put_api_20261001_resources_compensations_additional_compensations_id_body

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
