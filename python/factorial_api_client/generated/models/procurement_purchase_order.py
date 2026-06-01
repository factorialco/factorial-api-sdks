from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.procurement_purchase_order_status import ProcurementPurchaseOrderStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.procurement_purchase_order_cost import ProcurementPurchaseOrderCost


T = TypeVar("T", bound="ProcurementPurchaseOrder")


@_attrs_define
class ProcurementPurchaseOrder:
    id: int
    """ Unique identifier of the purchase order """
    po_number: int
    """ Purchase order number assigned to this order """
    description: str
    """ Description or notes about the purchase order """
    status: ProcurementPurchaseOrderStatus
    """ Current status of the purchase order """
    cost: ProcurementPurchaseOrderCost
    """ Total cost of the purchase order """
    date: str
    """ Date when the purchase order was created """
    purchase_request_id: int
    """ Identifier of the purchase request that generated this purchase order """
    legal_entity_id: int
    """ Identifier of the legal entity that owns this purchase order """
    company_id: int
    """ Identifier of the company that owns this purchase order """
    formatted_po_number: str
    """ Formatted purchase order number with prefix (e.g., PO-00001) """
    vendor_id: int | Unset = UNSET
    """ Identifier of the vendor (contact) associated with this purchase order """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        po_number = self.po_number

        description = self.description

        status = self.status.value

        cost = self.cost.to_dict()

        date = self.date

        purchase_request_id = self.purchase_request_id

        legal_entity_id = self.legal_entity_id

        company_id = self.company_id

        formatted_po_number = self.formatted_po_number

        vendor_id = self.vendor_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "po_number": po_number,
                "description": description,
                "status": status,
                "cost": cost,
                "date": date,
                "purchase_request_id": purchase_request_id,
                "legal_entity_id": legal_entity_id,
                "company_id": company_id,
                "formatted_po_number": formatted_po_number,
            }
        )
        if vendor_id is not UNSET:
            field_dict["vendor_id"] = vendor_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.procurement_purchase_order_cost import ProcurementPurchaseOrderCost

        d = dict(src_dict)
        id = d.pop("id")

        po_number = d.pop("po_number")

        description = d.pop("description")

        status = ProcurementPurchaseOrderStatus(d.pop("status"))

        cost = ProcurementPurchaseOrderCost.from_dict(d.pop("cost"))

        date = d.pop("date")

        purchase_request_id = d.pop("purchase_request_id")

        legal_entity_id = d.pop("legal_entity_id")

        company_id = d.pop("company_id")

        formatted_po_number = d.pop("formatted_po_number")

        vendor_id = d.pop("vendor_id", UNSET)

        procurement_purchase_order = cls(
            id=id,
            po_number=po_number,
            description=description,
            status=status,
            cost=cost,
            date=date,
            purchase_request_id=purchase_request_id,
            legal_entity_id=legal_entity_id,
            company_id=company_id,
            formatted_po_number=formatted_po_number,
            vendor_id=vendor_id,
        )

        procurement_purchase_order.additional_properties = d
        return procurement_purchase_order

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
