from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.procurement_purchase_request_status import ProcurementPurchaseRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.procurement_purchase_request_cost import ProcurementPurchaseRequestCost


T = TypeVar("T", bound="ProcurementPurchaseRequest")


@_attrs_define
class ProcurementPurchaseRequest:
    id: str
    """ Unique identifier of the purchase request """
    description: str
    """ Description or notes about the purchase request """
    type_id: str
    """ The id of the referred type """
    cost: ProcurementPurchaseRequestCost
    """ Total cost of the purchase request """
    date: str
    """ Date when the purchase request was created """
    requester_employee_id: str
    """ Identifier of the employee who requested this purchase """
    status: ProcurementPurchaseRequestStatus
    """ Current status of the purchase request """
    company_id: str | Unset = UNSET
    """ Identifier of the company that owns this purchase request """
    vendor_id: str | Unset = UNSET
    """ Identifier of the vendor (contact) associated with this purchase request """
    url: str | Unset = UNSET
    """ URL related to the purchase request (e.g., product link) """
    additional_information: str | Unset = UNSET
    """ Additional information or notes about the purchase request """
    deadline: str | Unset = UNSET
    """ Deadline date for the purchase request """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        description = self.description

        type_id = self.type_id

        cost = self.cost.to_dict()

        date = self.date

        requester_employee_id = self.requester_employee_id

        status = self.status.value

        company_id = self.company_id

        vendor_id = self.vendor_id

        url = self.url

        additional_information = self.additional_information

        deadline = self.deadline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "description": description,
                "type_id": type_id,
                "cost": cost,
                "date": date,
                "requester_employee_id": requester_employee_id,
                "status": status,
            }
        )
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if vendor_id is not UNSET:
            field_dict["vendor_id"] = vendor_id
        if url is not UNSET:
            field_dict["url"] = url
        if additional_information is not UNSET:
            field_dict["additional_information"] = additional_information
        if deadline is not UNSET:
            field_dict["deadline"] = deadline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.procurement_purchase_request_cost import ProcurementPurchaseRequestCost

        d = dict(src_dict)
        id = d.pop("id")

        description = d.pop("description")

        type_id = d.pop("type_id")

        cost = ProcurementPurchaseRequestCost.from_dict(d.pop("cost"))

        date = d.pop("date")

        requester_employee_id = d.pop("requester_employee_id")

        status = ProcurementPurchaseRequestStatus(d.pop("status"))

        company_id = d.pop("company_id", UNSET)

        vendor_id = d.pop("vendor_id", UNSET)

        url = d.pop("url", UNSET)

        additional_information = d.pop("additional_information", UNSET)

        deadline = d.pop("deadline", UNSET)

        procurement_purchase_request = cls(
            id=id,
            description=description,
            type_id=type_id,
            cost=cost,
            date=date,
            requester_employee_id=requester_employee_id,
            status=status,
            company_id=company_id,
            vendor_id=vendor_id,
            url=url,
            additional_information=additional_information,
            deadline=deadline,
        )

        procurement_purchase_request.additional_properties = d
        return procurement_purchase_request

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
