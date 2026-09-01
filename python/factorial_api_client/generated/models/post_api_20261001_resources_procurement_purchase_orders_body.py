from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20261001_resources_procurement_purchase_orders_body_preferred_payment_method import (
    PostApi20261001ResourcesProcurementPurchaseOrdersBodyPreferredPaymentMethod,
)
from ..models.post_api_20261001_resources_procurement_purchase_orders_body_status import (
    PostApi20261001ResourcesProcurementPurchaseOrdersBodyStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_20261001_resources_procurement_purchase_orders_body_header_field_values_item import (
        PostApi20261001ResourcesProcurementPurchaseOrdersBodyHeaderFieldValuesItem,
    )
    from ..models.post_api_20261001_resources_procurement_purchase_orders_body_line_items_item import (
        PostApi20261001ResourcesProcurementPurchaseOrdersBodyLineItemsItem,
    )


T = TypeVar("T", bound="PostApi20261001ResourcesProcurementPurchaseOrdersBody")


@_attrs_define
class PostApi20261001ResourcesProcurementPurchaseOrdersBody:
    company_id: str
    """ Company identifier, refers to /api/me endpoint. """
    legal_entity_id: str
    """ Identifier of the legal entity that owns the purchase order. Must belong to the company. """
    currency: str
    """ Currency code in ISO 4217 format. """
    vendor_id: str | Unset = UNSET
    """ Identifier of the vendor (Finance contact) by internal Factorial id. Vendors synced from an external system
    must be resolved to their Factorial id first (e.g. via the vendors read endpoint). """
    date: str | Unset = UNSET
    """ Purchase order date. Defaults to today when omitted. """
    deadline: str | Unset = UNSET
    """ Deadline date for the purchase order delivery or completion. """
    status: PostApi20261001ResourcesProcurementPurchaseOrdersBodyStatus | Unset = UNSET
    """ Status of the purchase order. Defaults to `draft`. `processing` is an internal transient status and is
    rejected. """
    description: str | Unset = UNSET
    """ Description or notes about the purchase order. """
    preferred_payment_method: (
        PostApi20261001ResourcesProcurementPurchaseOrdersBodyPreferredPaymentMethod | Unset
    ) = UNSET
    """ Preferred payment method for this purchase order. """
    header_field_values: (
        list[PostApi20261001ResourcesProcurementPurchaseOrdersBodyHeaderFieldValuesItem] | Unset
    ) = UNSET
    """ Header field values of the ACTIVE purchase order template version, as an array of `{field_key, value}`
    pairs. Only custom (non-predefined, non-computed) field keys are accepted; predefined fields (vendor,
    order_date, currency, due_date, payment_method, legal_entity) are populated from the corresponding top-level
    parameters. Reference fields (employee, cost_center, project, tax_rate, team) take the referenced internal id as
    the value. If a field_key appears more than once, the last occurrence wins. """
    line_items: list[PostApi20261001ResourcesProcurementPurchaseOrdersBodyLineItemsItem] | Unset = (
        UNSET
    )
    """ Line items of the purchase order, each carrying its values as an array of `{field_key, value}` pairs
    addressed by the line-item field keys of the ACTIVE template version (e.g. concept, quantity, unit_price,
    tax_rate). Computed keys (subtotal, tax_amount, total, discount_amount) are derived server-side and rejected as
    input. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        legal_entity_id = self.legal_entity_id

        currency = self.currency

        vendor_id = self.vendor_id

        date = self.date

        deadline = self.deadline

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status is not None else None

        description = self.description

        preferred_payment_method: str | Unset = UNSET
        if not isinstance(self.preferred_payment_method, Unset):
            preferred_payment_method = self.preferred_payment_method.value if self.preferred_payment_method is not None else None

        header_field_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.header_field_values, Unset):
            header_field_values = []
            for header_field_values_item_data in self.header_field_values:
                header_field_values_item = header_field_values_item_data.to_dict()
                header_field_values.append(header_field_values_item)

        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_id": company_id,
                "legal_entity_id": legal_entity_id,
                "currency": currency,
            }
        )
        if vendor_id is not UNSET:
            field_dict["vendor_id"] = vendor_id
        if date is not UNSET:
            field_dict["date"] = date
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if preferred_payment_method is not UNSET:
            field_dict["preferred_payment_method"] = preferred_payment_method
        if header_field_values is not UNSET:
            field_dict["header_field_values"] = header_field_values
        if line_items is not UNSET:
            field_dict["line_items"] = line_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_20261001_resources_procurement_purchase_orders_body_header_field_values_item import (
            PostApi20261001ResourcesProcurementPurchaseOrdersBodyHeaderFieldValuesItem,
        )
        from ..models.post_api_20261001_resources_procurement_purchase_orders_body_line_items_item import (
            PostApi20261001ResourcesProcurementPurchaseOrdersBodyLineItemsItem,
        )

        d = dict(src_dict)
        company_id = d.pop("company_id")

        legal_entity_id = d.pop("legal_entity_id")

        currency = d.pop("currency")

        vendor_id = d.pop("vendor_id", UNSET)

        date = d.pop("date", UNSET)

        deadline = d.pop("deadline", UNSET)

        _status = d.pop("status", UNSET)
        status: PostApi20261001ResourcesProcurementPurchaseOrdersBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PostApi20261001ResourcesProcurementPurchaseOrdersBodyStatus(_status) if _status is not None else None

        description = d.pop("description", UNSET)

        _preferred_payment_method = d.pop("preferred_payment_method", UNSET)
        preferred_payment_method: (
            PostApi20261001ResourcesProcurementPurchaseOrdersBodyPreferredPaymentMethod | Unset
        )
        if isinstance(_preferred_payment_method, Unset):
            preferred_payment_method = UNSET
        else:
            preferred_payment_method = (
                PostApi20261001ResourcesProcurementPurchaseOrdersBodyPreferredPaymentMethod(
                    _preferred_payment_method
                ) if _preferred_payment_method is not None else None
            )

        _header_field_values = d.pop("header_field_values", UNSET)
        header_field_values: (
            list[PostApi20261001ResourcesProcurementPurchaseOrdersBodyHeaderFieldValuesItem] | Unset
        ) = UNSET
        if _header_field_values is not UNSET:
            header_field_values = []
            for header_field_values_item_data in _header_field_values:
                header_field_values_item = PostApi20261001ResourcesProcurementPurchaseOrdersBodyHeaderFieldValuesItem.from_dict(
                    header_field_values_item_data
                )

                header_field_values.append(header_field_values_item)

        _line_items = d.pop("line_items", UNSET)
        line_items: (
            list[PostApi20261001ResourcesProcurementPurchaseOrdersBodyLineItemsItem] | Unset
        ) = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = (
                    PostApi20261001ResourcesProcurementPurchaseOrdersBodyLineItemsItem.from_dict(
                        line_items_item_data
                    )
                )

                line_items.append(line_items_item)

        post_api_20261001_resources_procurement_purchase_orders_body = cls(
            company_id=company_id,
            legal_entity_id=legal_entity_id,
            currency=currency,
            vendor_id=vendor_id,
            date=date,
            deadline=deadline,
            status=status,
            description=description,
            preferred_payment_method=preferred_payment_method,
            header_field_values=header_field_values,
            line_items=line_items,
        )

        post_api_20261001_resources_procurement_purchase_orders_body.additional_properties = d
        return post_api_20261001_resources_procurement_purchase_orders_body

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
