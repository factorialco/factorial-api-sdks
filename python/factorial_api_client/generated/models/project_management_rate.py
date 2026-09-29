from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_management_rate_resource_kind import ProjectManagementRateResourceKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectManagementRate")


@_attrs_define
class ProjectManagementRate:
    id: str
    """ The id of the rate """
    company_id: str
    """ The id of the company the rate belongs to """
    resource_id: str
    """ The id of the resource the rate applies to. Together with resource_kind it forms the resource's composite
    identity. """
    resource_kind: ProjectManagementRateResourceKind
    """ The kind of resource the rate applies to. Together with resource_id it forms the resource's composite
    identity. """
    starts_on: str
    """ The date from which the rate applies """
    charging_cost_cents: int
    """ The charging cost in cents """
    billing_rate_cents: int
    """ The billing rate in cents """
    markup_percentage_cents: int
    """ The markup-on-cost percentage in cents (e.g. 3000 = 30%) """
    margin_percentage_cents: int
    """ Computed profit margin on price in cents = (billing - charging) / billing * 10000. Returns 0 when billing
    equals charging, and -10000 when billing is zero. """
    currency: str
    """ The currency of the rate """
    unlinked: bool
    """ Whether the rate is custom """
    project_id: str | Unset = UNSET
    """ The id of the project the rate belongs to """
    quote_id: str | Unset = UNSET
    reference_rate_id: str | Unset = UNSET
    ends_on: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        resource_id = self.resource_id

        resource_kind = self.resource_kind.value

        starts_on = self.starts_on

        charging_cost_cents = self.charging_cost_cents

        billing_rate_cents = self.billing_rate_cents

        markup_percentage_cents = self.markup_percentage_cents

        margin_percentage_cents = self.margin_percentage_cents

        currency = self.currency

        unlinked = self.unlinked

        project_id = self.project_id

        quote_id = self.quote_id

        reference_rate_id = self.reference_rate_id

        ends_on = self.ends_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "resource_id": resource_id,
                "resource_kind": resource_kind,
                "starts_on": starts_on,
                "charging_cost_cents": charging_cost_cents,
                "billing_rate_cents": billing_rate_cents,
                "markup_percentage_cents": markup_percentage_cents,
                "margin_percentage_cents": margin_percentage_cents,
                "currency": currency,
                "unlinked": unlinked,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if quote_id is not UNSET:
            field_dict["quote_id"] = quote_id
        if reference_rate_id is not UNSET:
            field_dict["reference_rate_id"] = reference_rate_id
        if ends_on is not UNSET:
            field_dict["ends_on"] = ends_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        resource_id = d.pop("resource_id")

        resource_kind = ProjectManagementRateResourceKind(d.pop("resource_kind"))

        starts_on = d.pop("starts_on")

        charging_cost_cents = d.pop("charging_cost_cents")

        billing_rate_cents = d.pop("billing_rate_cents")

        markup_percentage_cents = d.pop("markup_percentage_cents")

        margin_percentage_cents = d.pop("margin_percentage_cents")

        currency = d.pop("currency")

        unlinked = d.pop("unlinked")

        project_id = d.pop("project_id", UNSET)

        quote_id = d.pop("quote_id", UNSET)

        reference_rate_id = d.pop("reference_rate_id", UNSET)

        ends_on = d.pop("ends_on", UNSET)

        project_management_rate = cls(
            id=id,
            company_id=company_id,
            resource_id=resource_id,
            resource_kind=resource_kind,
            starts_on=starts_on,
            charging_cost_cents=charging_cost_cents,
            billing_rate_cents=billing_rate_cents,
            markup_percentage_cents=markup_percentage_cents,
            margin_percentage_cents=margin_percentage_cents,
            currency=currency,
            unlinked=unlinked,
            project_id=project_id,
            quote_id=quote_id,
            reference_rate_id=reference_rate_id,
            ends_on=ends_on,
        )

        project_management_rate.additional_properties = d
        return project_management_rate

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
