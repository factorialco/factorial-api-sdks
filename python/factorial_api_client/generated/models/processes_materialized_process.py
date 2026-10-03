from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessesMaterializedProcess")


@_attrs_define
class ProcessesMaterializedProcess:
    id: str
    """ identifier of the workflow run. """
    process_id: str
    """ identifier of the workflow this run follows. Refers to the /processes/processes endpoint. """
    status: str
    """ state of the run: `running` while the person is going through it, `finalized` once every step is done,
    `archived` when it was cancelled. """
    finalized_at: str | Unset = UNSET
    """ when the run finished. Null while it is still running. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        process_id = self.process_id

        status = self.status

        finalized_at = self.finalized_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "process_id": process_id,
                "status": status,
            }
        )
        if finalized_at is not UNSET:
            field_dict["finalized_at"] = finalized_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        process_id = d.pop("process_id")

        status = d.pop("status")

        finalized_at = d.pop("finalized_at", UNSET)

        processes_materialized_process = cls(
            id=id,
            process_id=process_id,
            status=status,
            finalized_at=finalized_at,
        )

        processes_materialized_process.additional_properties = d
        return processes_materialized_process

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
