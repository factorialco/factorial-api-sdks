from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integrations_sync_run_status import IntegrationsSyncRunStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integrations_sync_run_context import IntegrationsSyncRunContext


T = TypeVar("T", bound="IntegrationsSyncRun")


@_attrs_define
class IntegrationsSyncRun:
    id: str
    """ Identifier of the sync run """
    status: IntegrationsSyncRunStatus
    """ Status of the sync run """
    started_at: str
    """ Timestamp when the sync run started """
    context: IntegrationsSyncRunContext
    """ Scope of this sync run. Holds `from` and `to`, the inclusive ISO-8601 dates of the period it covers; either
    key is absent when unknown, and the object is empty when the run is not date-scoped. """
    company_id: str
    """ Identifier of the company """
    integration_uuid: str
    """ UUID of the marketplace integration """
    finished_at: str | Unset = UNSET
    """ Timestamp when the sync run finished """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        started_at = self.started_at

        context = self.context.to_dict()

        company_id = self.company_id

        integration_uuid = self.integration_uuid

        finished_at = self.finished_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "started_at": started_at,
                "context": context,
                "company_id": company_id,
                "integration_uuid": integration_uuid,
            }
        )
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integrations_sync_run_context import IntegrationsSyncRunContext

        d = dict(src_dict)
        id = d.pop("id")

        status = IntegrationsSyncRunStatus(d.pop("status"))

        started_at = d.pop("started_at")

        context = IntegrationsSyncRunContext.from_dict(d.pop("context"))

        company_id = d.pop("company_id")

        integration_uuid = d.pop("integration_uuid")

        finished_at = d.pop("finished_at", UNSET)

        integrations_sync_run = cls(
            id=id,
            status=status,
            started_at=started_at,
            context=context,
            company_id=company_id,
            integration_uuid=integration_uuid,
            finished_at=finished_at,
        )

        integrations_sync_run.additional_properties = d
        return integrations_sync_run

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
