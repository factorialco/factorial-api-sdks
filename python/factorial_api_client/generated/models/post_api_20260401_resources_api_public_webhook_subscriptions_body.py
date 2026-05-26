from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_20260401_resources_api_public_webhook_subscriptions_body_api_version import (
    PostApi20260401ResourcesApiPublicWebhookSubscriptionsBodyApiVersion,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20260401ResourcesApiPublicWebhookSubscriptionsBody")


@_attrs_define
class PostApi20260401ResourcesApiPublicWebhookSubscriptionsBody:
    subscription_type: str
    """ Type of the webhook subscription """
    target_url: str
    """ URL where the webhook payload will be sent """
    company_id: int
    """ Company identifier of the webhook subscription """
    name: str | Unset = UNSET
    """ Name of the webhook subscription """
    challenge: str | Unset = UNSET
    """ String to verify the subscription """
    enabled: bool | Unset = UNSET
    """ Boolean to enable/disable the subscription """
    api_version: PostApi20260401ResourcesApiPublicWebhookSubscriptionsBodyApiVersion | Unset = UNSET
    """ API version of the webhook subscription that determines the schema of the payload """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_type = self.subscription_type

        target_url = self.target_url

        company_id = self.company_id

        name = self.name

        challenge = self.challenge

        enabled = self.enabled

        api_version: str | Unset = UNSET
        if not isinstance(self.api_version, Unset):
            api_version = self.api_version.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscription_type": subscription_type,
                "target_url": target_url,
                "company_id": company_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if challenge is not UNSET:
            field_dict["challenge"] = challenge
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if api_version is not UNSET:
            field_dict["api_version"] = api_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subscription_type = d.pop("subscription_type")

        target_url = d.pop("target_url")

        company_id = d.pop("company_id")

        name = d.pop("name", UNSET)

        challenge = d.pop("challenge", UNSET)

        enabled = d.pop("enabled", UNSET)

        _api_version = d.pop("api_version", UNSET)
        api_version: PostApi20260401ResourcesApiPublicWebhookSubscriptionsBodyApiVersion | Unset
        if isinstance(_api_version, Unset):
            api_version = UNSET
        else:
            api_version = PostApi20260401ResourcesApiPublicWebhookSubscriptionsBodyApiVersion(
                _api_version
            )

        post_api_20260401_resources_api_public_webhook_subscriptions_body = cls(
            subscription_type=subscription_type,
            target_url=target_url,
            company_id=company_id,
            name=name,
            challenge=challenge,
            enabled=enabled,
            api_version=api_version,
        )

        post_api_20260401_resources_api_public_webhook_subscriptions_body.additional_properties = d
        return post_api_20260401_resources_api_public_webhook_subscriptions_body

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
