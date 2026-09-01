from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.procurement_purchase_order_preferred_payment_method import (
    ProcurementPurchaseOrderPreferredPaymentMethod,
)
from ..models.procurement_purchase_order_status import ProcurementPurchaseOrderStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.procurement_purchase_order_cost import ProcurementPurchaseOrderCost
    from ..models.procurement_purchase_order_header_field_values_by_key_item import (
        ProcurementPurchaseOrderHeaderFieldValuesByKeyItem,
    )
    from ..models.procurement_purchase_order_line_items_by_key_item import (
        ProcurementPurchaseOrderLineItemsByKeyItem,
    )


T = TypeVar("T", bound="ProcurementPurchaseOrder")


@_attrs_define
class ProcurementPurchaseOrder:
    id: str
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
    legal_entity_id: str
    """ Identifier of the legal entity that owns this purchase order """
    company_id: str
    """ Identifier of the company that owns this purchase order """
    formatted_po_number: str
    """ Formatted purchase order number with prefix (e.g., PO-00001) """
    deadline: str | Unset = UNSET
    """ Deadline date for the purchase order delivery or completion. Writable through the update endpoint (omitted
    or null keeps it); readable here so the GET -> modify -> PUT roundtrip is complete. """
    vendor_id: str | Unset = UNSET
    """ Identifier of the vendor (contact) associated with this purchase order """
    purchase_request_id: str | Unset = UNSET
    """ Identifier of the purchase request that generated this purchase order, if any. Externally-created purchase
    orders (e.g. synced from an ERP) have no purchase request. """
    preferred_payment_method: ProcurementPurchaseOrderPreferredPaymentMethod | Unset = UNSET
    """ Preferred payment method for this purchase order """
    po_template_version_id: str | Unset = UNSET
    """ Identifier of the pinned PO template version this purchase order uses. Fetch that version (and its field
    definitions) to interpret the purchase order's header and line-item field keys. Null for legacy purchase orders
    created without a template. """
    header_field_values_by_key: list[ProcurementPurchaseOrderHeaderFieldValuesByKeyItem] | Unset = (
        UNSET
    )
    """ Custom header field values, addressed by the field_key of the purchase order's PINNED template version, as
    an array of `{field_key, value}` pairs — exactly the shape the update endpoint accepts, so a GET -> modify ->
    PUT roundtrip works verbatim. Predefined fields (vendor, order_date, currency, due_date, payment_method,
    legal_entity) surface as top-level parameters instead, and computed or hidden values never appear (they are
    preserved server-side on update). Null for purchase orders without a template version. """
    line_items_by_key: list[ProcurementPurchaseOrderLineItemsByKeyItem] | Unset = UNSET
    """ Line items with their field values addressed by the field_key of the purchase order's PINNED template
    version — the same shape the update endpoint accepts: modify and send the whole set back. Rows are addressed by
    id (rows without an id are created, persisted rows missing from the set are deleted). Null for purchase orders
    without a template version. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        po_number = self.po_number

        description = self.description

        status = self.status.value

        cost = self.cost.to_dict()

        date = self.date

        legal_entity_id = self.legal_entity_id

        company_id = self.company_id

        formatted_po_number = self.formatted_po_number

        deadline = self.deadline

        vendor_id = self.vendor_id

        purchase_request_id = self.purchase_request_id

        preferred_payment_method: str | Unset = UNSET
        if not isinstance(self.preferred_payment_method, Unset):
            preferred_payment_method = self.preferred_payment_method.value if self.preferred_payment_method is not None else None

        po_template_version_id = self.po_template_version_id

        header_field_values_by_key: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.header_field_values_by_key, Unset):
            header_field_values_by_key = []
            for header_field_values_by_key_item_data in self.header_field_values_by_key:
                header_field_values_by_key_item = header_field_values_by_key_item_data.to_dict()
                header_field_values_by_key.append(header_field_values_by_key_item)

        line_items_by_key: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items_by_key, Unset):
            line_items_by_key = []
            for line_items_by_key_item_data in self.line_items_by_key:
                line_items_by_key_item = line_items_by_key_item_data.to_dict()
                line_items_by_key.append(line_items_by_key_item)

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
                "legal_entity_id": legal_entity_id,
                "company_id": company_id,
                "formatted_po_number": formatted_po_number,
            }
        )
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if vendor_id is not UNSET:
            field_dict["vendor_id"] = vendor_id
        if purchase_request_id is not UNSET:
            field_dict["purchase_request_id"] = purchase_request_id
        if preferred_payment_method is not UNSET:
            field_dict["preferred_payment_method"] = preferred_payment_method
        if po_template_version_id is not UNSET:
            field_dict["po_template_version_id"] = po_template_version_id
        if header_field_values_by_key is not UNSET:
            field_dict["header_field_values_by_key"] = header_field_values_by_key
        if line_items_by_key is not UNSET:
            field_dict["line_items_by_key"] = line_items_by_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.procurement_purchase_order_cost import ProcurementPurchaseOrderCost
        from ..models.procurement_purchase_order_header_field_values_by_key_item import (
            ProcurementPurchaseOrderHeaderFieldValuesByKeyItem,
        )
        from ..models.procurement_purchase_order_line_items_by_key_item import (
            ProcurementPurchaseOrderLineItemsByKeyItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        po_number = d.pop("po_number")

        description = d.pop("description")

        status = ProcurementPurchaseOrderStatus(d.pop("status"))

        cost = ProcurementPurchaseOrderCost.from_dict(d.pop("cost"))

        date = d.pop("date")

        legal_entity_id = d.pop("legal_entity_id")

        company_id = d.pop("company_id")

        formatted_po_number = d.pop("formatted_po_number")

        deadline = d.pop("deadline", UNSET)

        vendor_id = d.pop("vendor_id", UNSET)

        purchase_request_id = d.pop("purchase_request_id", UNSET)

        _preferred_payment_method = d.pop("preferred_payment_method", UNSET)
        preferred_payment_method: ProcurementPurchaseOrderPreferredPaymentMethod | Unset
        if isinstance(_preferred_payment_method, Unset):
            preferred_payment_method = UNSET
        else:
            preferred_payment_method = ProcurementPurchaseOrderPreferredPaymentMethod(
                _preferred_payment_method
            ) if _preferred_payment_method is not None else None

        po_template_version_id = d.pop("po_template_version_id", UNSET)

        _header_field_values_by_key = d.pop("header_field_values_by_key", UNSET)
        header_field_values_by_key: (
            list[ProcurementPurchaseOrderHeaderFieldValuesByKeyItem] | Unset
        ) = UNSET
        if _header_field_values_by_key is not UNSET:
            header_field_values_by_key = []
            for header_field_values_by_key_item_data in _header_field_values_by_key:
                header_field_values_by_key_item = (
                    ProcurementPurchaseOrderHeaderFieldValuesByKeyItem.from_dict(
                        header_field_values_by_key_item_data
                    )
                )

                header_field_values_by_key.append(header_field_values_by_key_item)

        _line_items_by_key = d.pop("line_items_by_key", UNSET)
        line_items_by_key: list[ProcurementPurchaseOrderLineItemsByKeyItem] | Unset = UNSET
        if _line_items_by_key is not UNSET:
            line_items_by_key = []
            for line_items_by_key_item_data in _line_items_by_key:
                line_items_by_key_item = ProcurementPurchaseOrderLineItemsByKeyItem.from_dict(
                    line_items_by_key_item_data
                )

                line_items_by_key.append(line_items_by_key_item)

        procurement_purchase_order = cls(
            id=id,
            po_number=po_number,
            description=description,
            status=status,
            cost=cost,
            date=date,
            legal_entity_id=legal_entity_id,
            company_id=company_id,
            formatted_po_number=formatted_po_number,
            deadline=deadline,
            vendor_id=vendor_id,
            purchase_request_id=purchase_request_id,
            preferred_payment_method=preferred_payment_method,
            po_template_version_id=po_template_version_id,
            header_field_values_by_key=header_field_values_by_key,
            line_items_by_key=line_items_by_key,
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
