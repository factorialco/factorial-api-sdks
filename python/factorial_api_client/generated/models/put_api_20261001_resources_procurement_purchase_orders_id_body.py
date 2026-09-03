from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_20261001_resources_procurement_purchase_orders_id_body_preferred_payment_method import (
    PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyPreferredPaymentMethod,
)
from ..models.put_api_20261001_resources_procurement_purchase_orders_id_body_status import (
    PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_20261001_resources_procurement_purchase_orders_id_body_cost import (
        PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyCost,
    )
    from ..models.put_api_20261001_resources_procurement_purchase_orders_id_body_header_field_values_by_key_item import (
        PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyHeaderFieldValuesByKeyItem,
    )
    from ..models.put_api_20261001_resources_procurement_purchase_orders_id_body_line_items_by_key_item import (
        PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyLineItemsByKeyItem,
    )


T = TypeVar("T", bound="PutApi20261001ResourcesProcurementPurchaseOrdersIdBody")


@_attrs_define
class PutApi20261001ResourcesProcurementPurchaseOrdersIdBody:
    id: str
    """ Identifier of the purchase order to update. """
    company_id: str
    """ Company identifier, as returned by the credentials endpoint (`/resources/api_public/credentials`). """
    formatted_po_number: str
    """ Formatted purchase order number with prefix, as returned by the read endpoint — send back the value you
    read. """
    description: str
    """ Description or notes about the purchase order. """
    legal_entity_id: str
    """ Identifier of the legal entity that owns the purchase order. Must belong to the company. """
    cost: PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyCost
    """ Total cost of the purchase order, as returned by the read endpoint — send back what you read. The currency
    is applied as sent; on template-versioned purchase orders the amounts are owned by the line items and recomputed
    server-side. """
    preferred_payment_method: (
        PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyPreferredPaymentMethod | Unset
    ) = UNSET
    """ Preferred payment method for this purchase order. Send null to clear it. """
    status: PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyStatus | Unset = UNSET
    """ Status of the purchase order. Omitted or null keeps the current status; send a new one to transition. Once
    closed, the purchase order becomes immutable. """
    vendor_id: str | Unset = UNSET
    """ Identifier of the vendor (Finance contact) by internal Factorial id. Null clears the vendor on template-
    versioned purchase orders. """
    date: str | Unset = UNSET
    """ Purchase order date. Omit or send null to keep the current one. """
    deadline: str | Unset = UNSET
    """ Deadline date for the purchase order delivery or completion. Omitted or null keeps the current deadline
    (clearing a deadline through this endpoint is not supported). """
    header_field_values_by_key: (
        list[PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyHeaderFieldValuesByKeyItem]
        | Unset
    ) = UNSET
    """ Header field values of the purchase order's template version, as an array of `{field_key, value}` pairs —
    the same shape the read returns. Replaced as sent: send the complete set; an empty array deletes all custom
    header values, and omitting the field leaves them untouched. Only custom field keys are accepted; predefined
    fields (vendor, order_date, currency, due_date, payment_method, legal_entity) come from the corresponding top-
    level parameters. Reference fields take the referenced id as the value. If a field_key appears more than once,
    the last occurrence wins. """
    line_items_by_key: (
        list[PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyLineItemsByKeyItem] | Unset
    ) = UNSET
    """ Line items of the purchase order, replaced as sent — the same shape the read returns. Rows with an id update
    the matching line item, rows without an id create new ones, and persisted rows missing from the set are deleted.
    Send an empty array to remove all line items, or omit the field to leave them untouched. Values travel as
    `{field_key, value}` pairs; computed keys (subtotal, tax_amount, total, discount_amount) are derived server-side
    and rejected as input. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        formatted_po_number = self.formatted_po_number

        description = self.description

        legal_entity_id = self.legal_entity_id

        cost = self.cost.to_dict()

        preferred_payment_method: str | Unset = UNSET
        if not isinstance(self.preferred_payment_method, Unset):
            preferred_payment_method = self.preferred_payment_method.value if self.preferred_payment_method is not None else None

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status is not None else None

        vendor_id = self.vendor_id

        date = self.date

        deadline = self.deadline

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
                "company_id": company_id,
                "formatted_po_number": formatted_po_number,
                "description": description,
                "legal_entity_id": legal_entity_id,
                "cost": cost,
            }
        )
        if preferred_payment_method is not UNSET:
            field_dict["preferred_payment_method"] = preferred_payment_method
        if status is not UNSET:
            field_dict["status"] = status
        if vendor_id is not UNSET:
            field_dict["vendor_id"] = vendor_id
        if date is not UNSET:
            field_dict["date"] = date
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if header_field_values_by_key is not UNSET:
            field_dict["header_field_values_by_key"] = header_field_values_by_key
        if line_items_by_key is not UNSET:
            field_dict["line_items_by_key"] = line_items_by_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_api_20261001_resources_procurement_purchase_orders_id_body_cost import (
            PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyCost,
        )
        from ..models.put_api_20261001_resources_procurement_purchase_orders_id_body_header_field_values_by_key_item import (
            PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyHeaderFieldValuesByKeyItem,
        )
        from ..models.put_api_20261001_resources_procurement_purchase_orders_id_body_line_items_by_key_item import (
            PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyLineItemsByKeyItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        formatted_po_number = d.pop("formatted_po_number")

        description = d.pop("description")

        legal_entity_id = d.pop("legal_entity_id")

        cost = PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyCost.from_dict(d.pop("cost"))

        _preferred_payment_method = d.pop("preferred_payment_method", UNSET)
        preferred_payment_method: (
            PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyPreferredPaymentMethod | Unset
        )
        if isinstance(_preferred_payment_method, Unset):
            preferred_payment_method = UNSET
        else:
            preferred_payment_method = (
                PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyPreferredPaymentMethod(
                    _preferred_payment_method
                ) if _preferred_payment_method is not None else None
            )

        _status = d.pop("status", UNSET)
        status: PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyStatus(_status) if _status is not None else None

        vendor_id = d.pop("vendor_id", UNSET)

        date = d.pop("date", UNSET)

        deadline = d.pop("deadline", UNSET)

        _header_field_values_by_key = d.pop("header_field_values_by_key", UNSET)
        header_field_values_by_key: (
            list[PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyHeaderFieldValuesByKeyItem]
            | Unset
        ) = UNSET
        if _header_field_values_by_key is not UNSET:
            header_field_values_by_key = []
            for header_field_values_by_key_item_data in _header_field_values_by_key:
                header_field_values_by_key_item = PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyHeaderFieldValuesByKeyItem.from_dict(
                    header_field_values_by_key_item_data
                )

                header_field_values_by_key.append(header_field_values_by_key_item)

        _line_items_by_key = d.pop("line_items_by_key", UNSET)
        line_items_by_key: (
            list[PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyLineItemsByKeyItem] | Unset
        ) = UNSET
        if _line_items_by_key is not UNSET:
            line_items_by_key = []
            for line_items_by_key_item_data in _line_items_by_key:
                line_items_by_key_item = PutApi20261001ResourcesProcurementPurchaseOrdersIdBodyLineItemsByKeyItem.from_dict(
                    line_items_by_key_item_data
                )

                line_items_by_key.append(line_items_by_key_item)

        put_api_20261001_resources_procurement_purchase_orders_id_body = cls(
            id=id,
            company_id=company_id,
            formatted_po_number=formatted_po_number,
            description=description,
            legal_entity_id=legal_entity_id,
            cost=cost,
            preferred_payment_method=preferred_payment_method,
            status=status,
            vendor_id=vendor_id,
            date=date,
            deadline=deadline,
            header_field_values_by_key=header_field_values_by_key,
            line_items_by_key=line_items_by_key,
        )

        put_api_20261001_resources_procurement_purchase_orders_id_body.additional_properties = d
        return put_api_20261001_resources_procurement_purchase_orders_id_body

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
