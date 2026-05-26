from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPublicWebhookSubscription")


@_attrs_define
class ApiPublicWebhookSubscription:
    id: int
    """ Identifier of the webhook subscription """
    target_url: str
    """ URL where the webhook payload will be sent """
    type_: str
    """ Type of the webhook subscription """
    enabled: bool
    """ Boolean to enable/disable the subscription """
    api_version: str
    """ API version of the webhook subscription that determines the schema of the payload """
    company_id: int | Unset = UNSET
    """ Company identifier of the webhook subscription """
    name: str | Unset = UNSET
    """ Name of the webhook subscription """
    challenge: str | Unset = UNSET
    """ String to verify the subscription """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        target_url = self.target_url

        type_ = self.type_

        enabled = self.enabled

        api_version = self.api_version

        company_id = self.company_id

        name = self.name

        challenge = self.challenge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "target_url": target_url,
                "type": type_,
                "enabled": enabled,
                "api_version": api_version,
            }
        )
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if name is not UNSET:
            field_dict["name"] = name
        if challenge is not UNSET:
            field_dict["challenge"] = challenge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        target_url = d.pop("target_url")

        type_ = d.pop("type")

        enabled = d.pop("enabled")

        api_version = d.pop("api_version")

        company_id = d.pop("company_id", UNSET)

        name = d.pop("name", UNSET)

        challenge = d.pop("challenge", UNSET)

        api_public_webhook_subscription = cls(
            id=id,
            target_url=target_url,
            type_=type_,
            enabled=enabled,
            api_version=api_version,
            company_id=company_id,
            name=name,
            challenge=challenge,
        )

        api_public_webhook_subscription.additional_properties = d
        return api_public_webhook_subscription

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
