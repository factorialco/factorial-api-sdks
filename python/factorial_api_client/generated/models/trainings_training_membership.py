from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trainings_training_membership_status import TrainingsTrainingMembershipStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingsTrainingMembership")


@_attrs_define
class TrainingsTrainingMembership:
    id: int
    """ Unique identifier for the training membership. """
    access_id: int
    """ Access_id associated to the employee, refers to employees/employees endpoint. """
    employee_id: int
    """ Employee_id associated to the employee, refers to employees/employees endpoint. """
    training_id: int
    """ This field is used to filter those trainings memberships that belongs to this training. """
    status: TrainingsTrainingMembershipStatus
    """ This field is used to filter those trainings memberships whose attendance status is the given. """
    training_due_date: str | Unset = UNSET
    """ This field is used for those trainings with an expiry date. """
    training_completed_at: str | Unset = UNSET
    """ This field is used to record the date a training was completed for trainings that have an expiry date. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        access_id = self.access_id

        employee_id = self.employee_id

        training_id = self.training_id

        status = self.status.value

        training_due_date = self.training_due_date

        training_completed_at = self.training_completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "access_id": access_id,
                "employee_id": employee_id,
                "training_id": training_id,
                "status": status,
            }
        )
        if training_due_date is not UNSET:
            field_dict["training_due_date"] = training_due_date
        if training_completed_at is not UNSET:
            field_dict["training_completed_at"] = training_completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        access_id = d.pop("access_id")

        employee_id = d.pop("employee_id")

        training_id = d.pop("training_id")

        status = TrainingsTrainingMembershipStatus(d.pop("status"))

        training_due_date = d.pop("training_due_date", UNSET)

        training_completed_at = d.pop("training_completed_at", UNSET)

        trainings_training_membership = cls(
            id=id,
            access_id=access_id,
            employee_id=employee_id,
            training_id=training_id,
            status=status,
            training_due_date=training_due_date,
            training_completed_at=training_completed_at,
        )

        trainings_training_membership.additional_properties = d
        return trainings_training_membership

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
