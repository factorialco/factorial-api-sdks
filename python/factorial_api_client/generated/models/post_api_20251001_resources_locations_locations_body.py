from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApi20251001ResourcesLocationsLocationsBody")


@_attrs_define
class PostApi20251001ResourcesLocationsLocationsBody:
    name: str
    """ name of the location """
    country: str
    """ country code of the location """
    timezone: str
    """ timezone of the location """
    company_id: int
    """ company identifier """
    main: bool | Unset = UNSET
    """ whether the location is the main one """
    city: str | Unset = UNSET
    """ City of the location """
    state: str | Unset = UNSET
    """ State of the location """
    phone_number: str | Unset = UNSET
    """ phone number of the location """
    postal_code: str | Unset = UNSET
    """ Postal code of the location """
    address_line_one: str | Unset = UNSET
    """ Address line 1 of the location """
    address_line_two: str | Unset = UNSET
    """ Address line 2 of the location """
    latitude: float | Unset = UNSET
    """ latitude of the location """
    longitude: float | Unset = UNSET
    """ longitude of the location """
    radius: float | Unset = UNSET
    """ radius of the location """
    siret: str | Unset = UNSET
    """ siret of the location (only for France) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        country = self.country

        timezone = self.timezone

        company_id = self.company_id

        main = self.main

        city = self.city

        state = self.state

        phone_number = self.phone_number

        postal_code = self.postal_code

        address_line_one = self.address_line_one

        address_line_two = self.address_line_two

        latitude = self.latitude

        longitude = self.longitude

        radius = self.radius

        siret = self.siret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "country": country,
                "timezone": timezone,
                "company_id": company_id,
            }
        )
        if main is not UNSET:
            field_dict["main"] = main
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if address_line_one is not UNSET:
            field_dict["address_line_one"] = address_line_one
        if address_line_two is not UNSET:
            field_dict["address_line_two"] = address_line_two
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if radius is not UNSET:
            field_dict["radius"] = radius
        if siret is not UNSET:
            field_dict["siret"] = siret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        country = d.pop("country")

        timezone = d.pop("timezone")

        company_id = d.pop("company_id")

        main = d.pop("main", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        address_line_one = d.pop("address_line_one", UNSET)

        address_line_two = d.pop("address_line_two", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        radius = d.pop("radius", UNSET)

        siret = d.pop("siret", UNSET)

        post_api_20251001_resources_locations_locations_body = cls(
            name=name,
            country=country,
            timezone=timezone,
            company_id=company_id,
            main=main,
            city=city,
            state=state,
            phone_number=phone_number,
            postal_code=postal_code,
            address_line_one=address_line_one,
            address_line_two=address_line_two,
            latitude=latitude,
            longitude=longitude,
            radius=radius,
            siret=siret,
        )

        post_api_20251001_resources_locations_locations_body.additional_properties = d
        return post_api_20251001_resources_locations_locations_body

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
