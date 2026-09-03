from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integrations_syncable_item_sync_payload_cost_center_ids_item import (
        IntegrationsSyncableItemSyncPayloadCostCenterIdsItem,
    )
    from ..models.integrations_syncable_item_sync_payload_files_item import (
        IntegrationsSyncableItemSyncPayloadFilesItem,
    )
    from ..models.integrations_syncable_item_sync_payload_taxes_item import (
        IntegrationsSyncableItemSyncPayloadTaxesItem,
    )


T = TypeVar("T", bound="IntegrationsSyncableItemSyncPayload")


@_attrs_define
class IntegrationsSyncableItemSyncPayload:
    """data of the item to be synced

    Example:
        {'employee_id': 1, 'payroll_concept_id': 1, 'legal_entity_id': 1, 'amount': 7500, 'unit': 'money',
            'effective_on': '2028-03-31', 'employee_company_identifier': '123456'}

    """

    id: str | Unset = UNSET
    employee_id: str | Unset = UNSET
    payroll_concept_id: str | Unset = UNSET
    legal_entity_id: str | Unset = UNSET
    company_id: str | Unset = UNSET
    category_id: str | Unset = UNSET
    subcategory_id: str | Unset = UNSET
    ledger_account_id: str | Unset = UNSET
    leave_type_id: str | Unset = UNSET
    leave_type_name: str | Unset = UNSET
    translated_leave_type_name: str | Unset = UNSET
    employee_full_name: str | Unset = UNSET
    legal_entity_name: str | Unset = UNSET
    start_time: str | Unset = UNSET
    days_taken: float | Unset = UNSET
    created_at: str | Unset = UNSET
    contract_working_hours: int | Unset = UNSET
    contract_working_hours_frequency: str | Unset = UNSET
    contract_working_week_days: str | Unset = UNSET
    contract_fr_forfait_jours: bool | Unset = UNSET
    project_id: str | Unset = UNSET
    subproject_ids: list[str] | Unset = UNSET
    cost_center_ids: list[IntegrationsSyncableItemSyncPayloadCostCenterIdsItem] | Unset = UNSET
    files: list[IntegrationsSyncableItemSyncPayloadFilesItem] | Unset = UNSET
    taxes: list[IntegrationsSyncableItemSyncPayloadTaxesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        employee_id = self.employee_id

        payroll_concept_id = self.payroll_concept_id

        legal_entity_id = self.legal_entity_id

        company_id = self.company_id

        category_id = self.category_id

        subcategory_id = self.subcategory_id

        ledger_account_id = self.ledger_account_id

        leave_type_id = self.leave_type_id

        leave_type_name = self.leave_type_name

        translated_leave_type_name = self.translated_leave_type_name

        employee_full_name = self.employee_full_name

        legal_entity_name = self.legal_entity_name

        start_time = self.start_time

        days_taken = self.days_taken

        created_at = self.created_at

        contract_working_hours = self.contract_working_hours

        contract_working_hours_frequency = self.contract_working_hours_frequency

        contract_working_week_days = self.contract_working_week_days

        contract_fr_forfait_jours = self.contract_fr_forfait_jours

        project_id = self.project_id

        subproject_ids: list[str] | Unset = UNSET
        if not isinstance(self.subproject_ids, Unset):
            subproject_ids = self.subproject_ids

        cost_center_ids: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cost_center_ids, Unset):
            cost_center_ids = []
            for cost_center_ids_item_data in self.cost_center_ids:
                cost_center_ids_item = cost_center_ids_item_data.to_dict()
                cost_center_ids.append(cost_center_ids_item)

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        taxes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if employee_id is not UNSET:
            field_dict["employee_id"] = employee_id
        if payroll_concept_id is not UNSET:
            field_dict["payroll_concept_id"] = payroll_concept_id
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if subcategory_id is not UNSET:
            field_dict["subcategory_id"] = subcategory_id
        if ledger_account_id is not UNSET:
            field_dict["ledger_account_id"] = ledger_account_id
        if leave_type_id is not UNSET:
            field_dict["leave_type_id"] = leave_type_id
        if leave_type_name is not UNSET:
            field_dict["leave_type_name"] = leave_type_name
        if translated_leave_type_name is not UNSET:
            field_dict["translated_leave_type_name"] = translated_leave_type_name
        if employee_full_name is not UNSET:
            field_dict["employee_full_name"] = employee_full_name
        if legal_entity_name is not UNSET:
            field_dict["legal_entity_name"] = legal_entity_name
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if days_taken is not UNSET:
            field_dict["days_taken"] = days_taken
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if contract_working_hours is not UNSET:
            field_dict["contract_working_hours"] = contract_working_hours
        if contract_working_hours_frequency is not UNSET:
            field_dict["contract_working_hours_frequency"] = contract_working_hours_frequency
        if contract_working_week_days is not UNSET:
            field_dict["contract_working_week_days"] = contract_working_week_days
        if contract_fr_forfait_jours is not UNSET:
            field_dict["contract_fr_forfait_jours"] = contract_fr_forfait_jours
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if subproject_ids is not UNSET:
            field_dict["subproject_ids"] = subproject_ids
        if cost_center_ids is not UNSET:
            field_dict["cost_center_ids"] = cost_center_ids
        if files is not UNSET:
            field_dict["files"] = files
        if taxes is not UNSET:
            field_dict["taxes"] = taxes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integrations_syncable_item_sync_payload_cost_center_ids_item import (
            IntegrationsSyncableItemSyncPayloadCostCenterIdsItem,
        )
        from ..models.integrations_syncable_item_sync_payload_files_item import (
            IntegrationsSyncableItemSyncPayloadFilesItem,
        )
        from ..models.integrations_syncable_item_sync_payload_taxes_item import (
            IntegrationsSyncableItemSyncPayloadTaxesItem,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        employee_id = d.pop("employee_id", UNSET)

        payroll_concept_id = d.pop("payroll_concept_id", UNSET)

        legal_entity_id = d.pop("legal_entity_id", UNSET)

        company_id = d.pop("company_id", UNSET)

        category_id = d.pop("category_id", UNSET)

        subcategory_id = d.pop("subcategory_id", UNSET)

        ledger_account_id = d.pop("ledger_account_id", UNSET)

        leave_type_id = d.pop("leave_type_id", UNSET)

        leave_type_name = d.pop("leave_type_name", UNSET)

        translated_leave_type_name = d.pop("translated_leave_type_name", UNSET)

        employee_full_name = d.pop("employee_full_name", UNSET)

        legal_entity_name = d.pop("legal_entity_name", UNSET)

        start_time = d.pop("start_time", UNSET)

        days_taken = d.pop("days_taken", UNSET)

        created_at = d.pop("created_at", UNSET)

        contract_working_hours = d.pop("contract_working_hours", UNSET)

        contract_working_hours_frequency = d.pop("contract_working_hours_frequency", UNSET)

        contract_working_week_days = d.pop("contract_working_week_days", UNSET)

        contract_fr_forfait_jours = d.pop("contract_fr_forfait_jours", UNSET)

        project_id = d.pop("project_id", UNSET)

        subproject_ids = cast(list[str], d.pop("subproject_ids", UNSET))

        _cost_center_ids = d.pop("cost_center_ids", UNSET)
        cost_center_ids: list[IntegrationsSyncableItemSyncPayloadCostCenterIdsItem] | Unset = UNSET
        if _cost_center_ids is not UNSET:
            cost_center_ids = []
            for cost_center_ids_item_data in _cost_center_ids:
                cost_center_ids_item = (
                    IntegrationsSyncableItemSyncPayloadCostCenterIdsItem.from_dict(
                        cost_center_ids_item_data
                    )
                )

                cost_center_ids.append(cost_center_ids_item)

        _files = d.pop("files", UNSET)
        files: list[IntegrationsSyncableItemSyncPayloadFilesItem] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = IntegrationsSyncableItemSyncPayloadFilesItem.from_dict(files_item_data)

                files.append(files_item)

        _taxes = d.pop("taxes", UNSET)
        taxes: list[IntegrationsSyncableItemSyncPayloadTaxesItem] | Unset = UNSET
        if _taxes is not UNSET:
            taxes = []
            for taxes_item_data in _taxes:
                taxes_item = IntegrationsSyncableItemSyncPayloadTaxesItem.from_dict(taxes_item_data)

                taxes.append(taxes_item)

        integrations_syncable_item_sync_payload = cls(
            id=id,
            employee_id=employee_id,
            payroll_concept_id=payroll_concept_id,
            legal_entity_id=legal_entity_id,
            company_id=company_id,
            category_id=category_id,
            subcategory_id=subcategory_id,
            ledger_account_id=ledger_account_id,
            leave_type_id=leave_type_id,
            leave_type_name=leave_type_name,
            translated_leave_type_name=translated_leave_type_name,
            employee_full_name=employee_full_name,
            legal_entity_name=legal_entity_name,
            start_time=start_time,
            days_taken=days_taken,
            created_at=created_at,
            contract_working_hours=contract_working_hours,
            contract_working_hours_frequency=contract_working_hours_frequency,
            contract_working_week_days=contract_working_week_days,
            contract_fr_forfait_jours=contract_fr_forfait_jours,
            project_id=project_id,
            subproject_ids=subproject_ids,
            cost_center_ids=cost_center_ids,
            files=files,
            taxes=taxes,
        )

        integrations_syncable_item_sync_payload.additional_properties = d
        return integrations_syncable_item_sync_payload

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
