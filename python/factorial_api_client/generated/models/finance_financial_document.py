from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.finance_financial_document_document_type import FinanceFinancialDocumentDocumentType
from ..models.finance_financial_document_status import FinanceFinancialDocumentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finance_financial_document_file import FinanceFinancialDocumentFile


T = TypeVar("T", bound="FinanceFinancialDocument")


@_attrs_define
class FinanceFinancialDocument:
    id: str
    """ Factorial unique identifier. """
    status: FinanceFinancialDocumentStatus
    """ Current status. """
    updated_at: str
    """ Updation date. """
    taxes: list[Any]
    """ Taxes. """
    document_type: FinanceFinancialDocumentDocumentType
    """ Type of the financial document. Using "invoice" as default. """
    net_amount_cents: int | Unset = UNSET
    """ Net amount in cents. """
    total_amount_cents: int | Unset = UNSET
    """ Total amount in cents. """
    document_number: str | Unset = UNSET
    """ Document number. """
    currency: str | Unset = UNSET
    """ Document currency. """
    due_date: str | Unset = UNSET
    """ Due date. """
    document_date: str | Unset = UNSET
    """ Document date. """
    legal_entity_id: str | Unset = UNSET
    """ Factorial unique identifier for the legal entity of the financial document. """
    vendor_id: str | Unset = UNSET
    """ Factorial unique identifier for the vendor of the financial document. """
    file: FinanceFinancialDocumentFile | Unset = UNSET
    """ File attached. """
    fully_reconciled_at: str | Unset = UNSET
    """ Date when was fully reconciled. """
    recorded_at: str | Unset = UNSET
    """ Date when was recorded. """
    duplicate_financial_document_id: str | Unset = UNSET
    """ Factorial unique identifier for the duplicate financial document. """
    validated_at: str | Unset = UNSET
    """ Date when was validated. """
    validated_by_id: str | Unset = UNSET
    """ Factorial unique identifier for the user who validated the financial document. """
    parent_financial_document_id: str | Unset = UNSET
    """ Factorial unique identifier for the parent financial document of the financial document. """
    taxes_total_amount_cents: int | Unset = UNSET
    """ Taxes total amount in cents. """
    issuer_name: str | Unset = UNSET
    """ Name of the entity issuing the financial document. """
    issuer_address_line_1: str | Unset = UNSET
    """ First line of the issuer's address. """
    issuer_address_line_2: str | Unset = UNSET
    """ Second line of the issuer's address. """
    issuer_city: str | Unset = UNSET
    """ City of the issuer's address. """
    issuer_postal_code: str | Unset = UNSET
    """ Postal code of the issuer's address. """
    issuer_state: str | Unset = UNSET
    """ State or province of the issuer's address. """
    issuer_country_code: str | Unset = UNSET
    """ Country code of the issuer's address. """
    issuer_tax_id: str | Unset = UNSET
    """ Tax identification number of the issuer. """
    recipient_name: str | Unset = UNSET
    """ Name of the entity receiving the financial document. """
    recipient_address_line_1: str | Unset = UNSET
    """ First line of the recipient's address. """
    recipient_address_line_2: str | Unset = UNSET
    """ Second line of the recipient's address. """
    recipient_city: str | Unset = UNSET
    """ City of the recipient's address. """
    recipient_postal_code: str | Unset = UNSET
    """ Postal code of the recipient's address. """
    recipient_state: str | Unset = UNSET
    """ State or province of the recipient's address. """
    recipient_country_code: str | Unset = UNSET
    """ Country code of the recipient's address. """
    recipient_tax_id: str | Unset = UNSET
    """ Tax identification number of the recipient. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        updated_at = self.updated_at

        taxes = self.taxes

        document_type = self.document_type.value

        net_amount_cents = self.net_amount_cents

        total_amount_cents = self.total_amount_cents

        document_number = self.document_number

        currency = self.currency

        due_date = self.due_date

        document_date = self.document_date

        legal_entity_id = self.legal_entity_id

        vendor_id = self.vendor_id

        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        fully_reconciled_at = self.fully_reconciled_at

        recorded_at = self.recorded_at

        duplicate_financial_document_id = self.duplicate_financial_document_id

        validated_at = self.validated_at

        validated_by_id = self.validated_by_id

        parent_financial_document_id = self.parent_financial_document_id

        taxes_total_amount_cents = self.taxes_total_amount_cents

        issuer_name = self.issuer_name

        issuer_address_line_1 = self.issuer_address_line_1

        issuer_address_line_2 = self.issuer_address_line_2

        issuer_city = self.issuer_city

        issuer_postal_code = self.issuer_postal_code

        issuer_state = self.issuer_state

        issuer_country_code = self.issuer_country_code

        issuer_tax_id = self.issuer_tax_id

        recipient_name = self.recipient_name

        recipient_address_line_1 = self.recipient_address_line_1

        recipient_address_line_2 = self.recipient_address_line_2

        recipient_city = self.recipient_city

        recipient_postal_code = self.recipient_postal_code

        recipient_state = self.recipient_state

        recipient_country_code = self.recipient_country_code

        recipient_tax_id = self.recipient_tax_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "updated_at": updated_at,
                "taxes": taxes,
                "document_type": document_type,
            }
        )
        if net_amount_cents is not UNSET:
            field_dict["net_amount_cents"] = net_amount_cents
        if total_amount_cents is not UNSET:
            field_dict["total_amount_cents"] = total_amount_cents
        if document_number is not UNSET:
            field_dict["document_number"] = document_number
        if currency is not UNSET:
            field_dict["currency"] = currency
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if document_date is not UNSET:
            field_dict["document_date"] = document_date
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if vendor_id is not UNSET:
            field_dict["vendor_id"] = vendor_id
        if file is not UNSET:
            field_dict["file"] = file
        if fully_reconciled_at is not UNSET:
            field_dict["fully_reconciled_at"] = fully_reconciled_at
        if recorded_at is not UNSET:
            field_dict["recorded_at"] = recorded_at
        if duplicate_financial_document_id is not UNSET:
            field_dict["duplicate_financial_document_id"] = duplicate_financial_document_id
        if validated_at is not UNSET:
            field_dict["validated_at"] = validated_at
        if validated_by_id is not UNSET:
            field_dict["validated_by_id"] = validated_by_id
        if parent_financial_document_id is not UNSET:
            field_dict["parent_financial_document_id"] = parent_financial_document_id
        if taxes_total_amount_cents is not UNSET:
            field_dict["taxes_total_amount_cents"] = taxes_total_amount_cents
        if issuer_name is not UNSET:
            field_dict["issuer_name"] = issuer_name
        if issuer_address_line_1 is not UNSET:
            field_dict["issuer_address_line_1"] = issuer_address_line_1
        if issuer_address_line_2 is not UNSET:
            field_dict["issuer_address_line_2"] = issuer_address_line_2
        if issuer_city is not UNSET:
            field_dict["issuer_city"] = issuer_city
        if issuer_postal_code is not UNSET:
            field_dict["issuer_postal_code"] = issuer_postal_code
        if issuer_state is not UNSET:
            field_dict["issuer_state"] = issuer_state
        if issuer_country_code is not UNSET:
            field_dict["issuer_country_code"] = issuer_country_code
        if issuer_tax_id is not UNSET:
            field_dict["issuer_tax_id"] = issuer_tax_id
        if recipient_name is not UNSET:
            field_dict["recipient_name"] = recipient_name
        if recipient_address_line_1 is not UNSET:
            field_dict["recipient_address_line_1"] = recipient_address_line_1
        if recipient_address_line_2 is not UNSET:
            field_dict["recipient_address_line_2"] = recipient_address_line_2
        if recipient_city is not UNSET:
            field_dict["recipient_city"] = recipient_city
        if recipient_postal_code is not UNSET:
            field_dict["recipient_postal_code"] = recipient_postal_code
        if recipient_state is not UNSET:
            field_dict["recipient_state"] = recipient_state
        if recipient_country_code is not UNSET:
            field_dict["recipient_country_code"] = recipient_country_code
        if recipient_tax_id is not UNSET:
            field_dict["recipient_tax_id"] = recipient_tax_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.finance_financial_document_file import FinanceFinancialDocumentFile

        d = dict(src_dict)
        id = d.pop("id")

        status = FinanceFinancialDocumentStatus(d.pop("status"))

        updated_at = d.pop("updated_at")

        taxes = cast(list[Any], d.pop("taxes"))

        document_type = FinanceFinancialDocumentDocumentType(d.pop("document_type"))

        net_amount_cents = d.pop("net_amount_cents", UNSET)

        total_amount_cents = d.pop("total_amount_cents", UNSET)

        document_number = d.pop("document_number", UNSET)

        currency = d.pop("currency", UNSET)

        due_date = d.pop("due_date", UNSET)

        document_date = d.pop("document_date", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        vendor_id = d.pop("vendor_id", UNSET)

        _file = d.pop("file", UNSET)
        file: FinanceFinancialDocumentFile | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = FinanceFinancialDocumentFile.from_dict(_file)

        fully_reconciled_at = d.pop("fully_reconciled_at", UNSET)

        recorded_at = d.pop("recorded_at", UNSET)

        duplicate_financial_document_id = d.pop("duplicate_financial_document_id", UNSET)

        validated_at = d.pop("validated_at", UNSET)

        validated_by_id = d.pop("validated_by_id", UNSET)

        parent_financial_document_id = d.pop("parent_financial_document_id", UNSET)

        taxes_total_amount_cents = d.pop("taxes_total_amount_cents", UNSET)

        issuer_name = d.pop("issuer_name", UNSET)

        issuer_address_line_1 = d.pop("issuer_address_line_1", UNSET)

        issuer_address_line_2 = d.pop("issuer_address_line_2", UNSET)

        issuer_city = d.pop("issuer_city", UNSET)

        issuer_postal_code = d.pop("issuer_postal_code", UNSET)

        issuer_state = d.pop("issuer_state", UNSET)

        issuer_country_code = d.pop("issuer_country_code", UNSET)

        issuer_tax_id = d.pop("issuer_tax_id", UNSET)

        recipient_name = d.pop("recipient_name", UNSET)

        recipient_address_line_1 = d.pop("recipient_address_line_1", UNSET)

        recipient_address_line_2 = d.pop("recipient_address_line_2", UNSET)

        recipient_city = d.pop("recipient_city", UNSET)

        recipient_postal_code = d.pop("recipient_postal_code", UNSET)

        recipient_state = d.pop("recipient_state", UNSET)

        recipient_country_code = d.pop("recipient_country_code", UNSET)

        recipient_tax_id = d.pop("recipient_tax_id", UNSET)

        finance_financial_document = cls(
            id=id,
            status=status,
            updated_at=updated_at,
            taxes=taxes,
            document_type=document_type,
            net_amount_cents=net_amount_cents,
            total_amount_cents=total_amount_cents,
            document_number=document_number,
            currency=currency,
            due_date=due_date,
            document_date=document_date,
            legal_entity_id=legal_entity_id,
            vendor_id=vendor_id,
            file=file,
            fully_reconciled_at=fully_reconciled_at,
            recorded_at=recorded_at,
            duplicate_financial_document_id=duplicate_financial_document_id,
            validated_at=validated_at,
            validated_by_id=validated_by_id,
            parent_financial_document_id=parent_financial_document_id,
            taxes_total_amount_cents=taxes_total_amount_cents,
            issuer_name=issuer_name,
            issuer_address_line_1=issuer_address_line_1,
            issuer_address_line_2=issuer_address_line_2,
            issuer_city=issuer_city,
            issuer_postal_code=issuer_postal_code,
            issuer_state=issuer_state,
            issuer_country_code=issuer_country_code,
            issuer_tax_id=issuer_tax_id,
            recipient_name=recipient_name,
            recipient_address_line_1=recipient_address_line_1,
            recipient_address_line_2=recipient_address_line_2,
            recipient_city=recipient_city,
            recipient_postal_code=recipient_postal_code,
            recipient_state=recipient_state,
            recipient_country_code=recipient_country_code,
            recipient_tax_id=recipient_tax_id,
        )

        finance_financial_document.additional_properties = d
        return finance_financial_document

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
