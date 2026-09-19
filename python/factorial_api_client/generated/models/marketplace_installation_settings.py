from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.marketplace_installation_settings_leave_types_item import (
        MarketplaceInstallationSettingsLeaveTypesItem,
    )
    from ..models.marketplace_installation_settings_legal_entities_item import (
        MarketplaceInstallationSettingsLegalEntitiesItem,
    )
    from ..models.marketplace_installation_settings_locations_item import (
        MarketplaceInstallationSettingsLocationsItem,
    )
    from ..models.marketplace_installation_settings_payroll_concept_codes_item import (
        MarketplaceInstallationSettingsPayrollConceptCodesItem,
    )
    from ..models.marketplace_installation_settings_timeoff_allowance_code_item import (
        MarketplaceInstallationSettingsTimeoffAllowanceCodeItem,
    )


T = TypeVar("T", bound="MarketplaceInstallationSettings")


@_attrs_define
class MarketplaceInstallationSettings:
    leave_types: list[MarketplaceInstallationSettingsLeaveTypesItem]
    """ Leave types codes """
    timeoff_allowance_code: list[MarketplaceInstallationSettingsTimeoffAllowanceCodeItem]
    """ Timeoff allowance codes """
    legal_entities: list[MarketplaceInstallationSettingsLegalEntitiesItem]
    """ Legal entity codes (id is the legal entity id) """
    locations: list[MarketplaceInstallationSettingsLocationsItem]
    """ Workplace codes (id is the location id) """
    payroll_concept_codes: list[MarketplaceInstallationSettingsPayrollConceptCodesItem]
    """ Payroll concept codes per legal entity (id is the payroll concept id) """
    company_code: str | Unset = UNSET
    """ Company-level code """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        leave_types = []
        for leave_types_item_data in self.leave_types:
            leave_types_item = leave_types_item_data.to_dict()
            leave_types.append(leave_types_item)

        timeoff_allowance_code = []
        for timeoff_allowance_code_item_data in self.timeoff_allowance_code:
            timeoff_allowance_code_item = timeoff_allowance_code_item_data.to_dict()
            timeoff_allowance_code.append(timeoff_allowance_code_item)

        legal_entities = []
        for legal_entities_item_data in self.legal_entities:
            legal_entities_item = legal_entities_item_data.to_dict()
            legal_entities.append(legal_entities_item)

        locations = []
        for locations_item_data in self.locations:
            locations_item = locations_item_data.to_dict()
            locations.append(locations_item)

        payroll_concept_codes = []
        for payroll_concept_codes_item_data in self.payroll_concept_codes:
            payroll_concept_codes_item = payroll_concept_codes_item_data.to_dict()
            payroll_concept_codes.append(payroll_concept_codes_item)

        company_code = self.company_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "leave_types": leave_types,
                "timeoff_allowance_code": timeoff_allowance_code,
                "legal_entities": legal_entities,
                "locations": locations,
                "payroll_concept_codes": payroll_concept_codes,
            }
        )
        if company_code is not UNSET:
            field_dict["company_code"] = company_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketplace_installation_settings_leave_types_item import (
            MarketplaceInstallationSettingsLeaveTypesItem,
        )
        from ..models.marketplace_installation_settings_legal_entities_item import (
            MarketplaceInstallationSettingsLegalEntitiesItem,
        )
        from ..models.marketplace_installation_settings_locations_item import (
            MarketplaceInstallationSettingsLocationsItem,
        )
        from ..models.marketplace_installation_settings_payroll_concept_codes_item import (
            MarketplaceInstallationSettingsPayrollConceptCodesItem,
        )
        from ..models.marketplace_installation_settings_timeoff_allowance_code_item import (
            MarketplaceInstallationSettingsTimeoffAllowanceCodeItem,
        )

        d = dict(src_dict)
        leave_types = []
        _leave_types = d.pop("leave_types")
        for leave_types_item_data in _leave_types:
            leave_types_item = MarketplaceInstallationSettingsLeaveTypesItem.from_dict(
                leave_types_item_data
            )

            leave_types.append(leave_types_item)

        timeoff_allowance_code = []
        _timeoff_allowance_code = d.pop("timeoff_allowance_code")
        for timeoff_allowance_code_item_data in _timeoff_allowance_code:
            timeoff_allowance_code_item = (
                MarketplaceInstallationSettingsTimeoffAllowanceCodeItem.from_dict(
                    timeoff_allowance_code_item_data
                )
            )

            timeoff_allowance_code.append(timeoff_allowance_code_item)

        legal_entities = []
        _legal_entities = d.pop("legal_entities")
        for legal_entities_item_data in _legal_entities:
            legal_entities_item = MarketplaceInstallationSettingsLegalEntitiesItem.from_dict(
                legal_entities_item_data
            )

            legal_entities.append(legal_entities_item)

        locations = []
        _locations = d.pop("locations")
        for locations_item_data in _locations:
            locations_item = MarketplaceInstallationSettingsLocationsItem.from_dict(
                locations_item_data
            )

            locations.append(locations_item)

        payroll_concept_codes = []
        _payroll_concept_codes = d.pop("payroll_concept_codes")
        for payroll_concept_codes_item_data in _payroll_concept_codes:
            payroll_concept_codes_item = (
                MarketplaceInstallationSettingsPayrollConceptCodesItem.from_dict(
                    payroll_concept_codes_item_data
                )
            )

            payroll_concept_codes.append(payroll_concept_codes_item)

        company_code = d.pop("company_code", UNSET)

        marketplace_installation_settings = cls(
            leave_types=leave_types,
            timeoff_allowance_code=timeoff_allowance_code,
            legal_entities=legal_entities,
            locations=locations,
            payroll_concept_codes=payroll_concept_codes,
            company_code=company_code,
        )

        marketplace_installation_settings.additional_properties = d
        return marketplace_installation_settings

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
