from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payroll_integrations_base_code_integration import (
    PayrollIntegrationsBaseCodeIntegration,
)

T = TypeVar("T", bound="PayrollIntegrationsBaseCode")


@_attrs_define
class PayrollIntegrationsBaseCode:
    id: str
    """ Code identifier """
    company_id: str
    """ Company ID where the code belongs to """
    code: str
    """ Code value """
    codeable_id: str
    """ Related object ID. Used together with codeable_type """
    codeable_type: str
    """ Related object type. Used together with codeable_id """
    integration: PayrollIntegrationsBaseCodeIntegration
    """ Integration name """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        code = self.code

        codeable_id = self.codeable_id

        codeable_type = self.codeable_type

        integration = self.integration.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "code": code,
                "codeable_id": codeable_id,
                "codeable_type": codeable_type,
                "integration": integration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("company_id")

        code = d.pop("code")

        codeable_id = d.pop("codeable_id")

        codeable_type = d.pop("codeable_type")

        integration = PayrollIntegrationsBaseCodeIntegration(d.pop("integration"))

        payroll_integrations_base_code = cls(
            id=id,
            company_id=company_id,
            code=code,
            codeable_id=codeable_id,
            codeable_type=codeable_type,
            integration=integration,
        )

        payroll_integrations_base_code.additional_properties = d
        return payroll_integrations_base_code

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
