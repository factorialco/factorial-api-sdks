from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contracts_materialized_template_template_type import (
    ContractsMaterializedTemplateTemplateType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contracts_materialized_template_template_item import (
        ContractsMaterializedTemplateTemplateItem,
    )


T = TypeVar("T", bound="ContractsMaterializedTemplate")


@_attrs_define
class ContractsMaterializedTemplate:
    id: str
    """ Synthetic identifier for this materialized template, composed as
    {company_id}-{template_type}-{legal_entity_id}-{country_code}. Used as a stable cursor reference for pagination.
     """
    company_id: str
    """ Identifier of the company that owns this template. All templates are scoped to a company; use this to
    correlate templates across different levels (company, country, legal entity) for the same organization.
     """
    template_type: ContractsMaterializedTemplateTemplateType
    """ The level at which this template has been materialized. Templates follow a three-tier inheritance hierarchy:
    company (base defaults for the whole organization), country (overrides per country labor law), and legal_entity
    (final merged view per legal entity, combining all three levels). Use legal_entity when you need the definitive
    set of fields for a specific hiring context.
     """
    template: list[ContractsMaterializedTemplateTemplateItem]
    """ The ordered list of contract fields defined in this template after merging all inheritance levels and
    removing hidden fields. Each entry is a FragmentField describing a single configurable attribute of a contract
    (e.g. contract type, job title, salary). The list reflects the final effective set of fields an employee
    contract under this template will contain.
     """
    legal_entity_id: str | Unset = UNSET
    """ Identifier of the legal entity this template has been materialized for. Present only when template_type is
    legal_entity. Legal entity templates represent the final merged view of fields applicable to employees hired
    under that legal entity, combining company-level defaults with country-specific and legal-entity-specific
    overrides.
     """
    country_code: str | Unset = UNSET
    """ ISO 3166-1 alpha-2 country code identifying the country this template applies to. Present for country and
    legal_entity template types. Determines which country-specific fields and options are included (e.g. fields
    required by Spanish or French labor law).
     """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        template_type = self.template_type.value

        template = []
        for template_item_data in self.template:
            template_item = template_item_data.to_dict()
            template.append(template_item)

        legal_entity_id = self.legal_entity_id

        country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "template_type": template_type,
                "template": template,
            }
        )
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if country_code is not UNSET:
            field_dict["country_code"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contracts_materialized_template_template_item import (
            ContractsMaterializedTemplateTemplateItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        template_type = ContractsMaterializedTemplateTemplateType(d.pop("template_type"))

        template = []
        _template = d.pop("template")
        for template_item_data in _template:
            template_item = ContractsMaterializedTemplateTemplateItem.from_dict(template_item_data)

            template.append(template_item)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        country_code = d.pop("country_code", UNSET)

        contracts_materialized_template = cls(
            id=id,
            company_id=company_id,
            template_type=template_type,
            template=template,
            legal_entity_id=legal_entity_id,
            country_code=country_code,
        )

        contracts_materialized_template.additional_properties = d
        return contracts_materialized_template

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
