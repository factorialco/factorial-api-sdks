from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationsLocation")


@_attrs_define
class LocationsLocation:
    id: str
    """ identifier of the location """
    company_id: str
    """ company identifier """
    name: str
    """ name of the location """
    main: bool
    """ whether the location is the main one """
    timezone: str | Unset = UNSET
    """ timezone of the location """
    country: str | Unset = UNSET
    """ country code of the location """
    state: str | Unset = UNSET
    """ State of the location """
    city: str | Unset = UNSET
    """ City of the location """
    address_line_1: str | Unset = UNSET
    """ Address line 1 of the location """
    address_line_2: str | Unset = UNSET
    """ Address line 2 of the location """
    postal_code: str | Unset = UNSET
    """ Postal code of the location """
    phone_number: str | Unset = UNSET
    """ phone number of the location """
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
        id = self.id

        company_id = self.company_id

        name = self.name

        main = self.main

        timezone = self.timezone

        country = self.country

        state = self.state

        city = self.city

        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        postal_code = self.postal_code

        phone_number = self.phone_number

        latitude = self.latitude

        longitude = self.longitude

        radius = self.radius

        siret = self.siret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "name": name,
                "main": main,
            }
        )
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if country is not UNSET:
            field_dict["country"] = country
        if state is not UNSET:
            field_dict["state"] = state
        if city is not UNSET:
            field_dict["city"] = city
        if address_line_1 is not UNSET:
            field_dict["address_line_1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["address_line_2"] = address_line_2
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
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
        id = d.pop("id")

        company_id = d.pop("company_id")

        name = d.pop("name")

        main = d.pop("main")

        timezone = d.pop("timezone", UNSET)

        country = d.pop("country", UNSET)

        state = d.pop("state", UNSET)

        city = d.pop("city", UNSET)

        address_line_1 = d.pop("address_line_1", UNSET)

        address_line_2 = d.pop("address_line_2", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        radius = d.pop("radius", UNSET)

        siret = d.pop("siret", UNSET)

        locations_location = cls(
            id=id,
            company_id=company_id,
            name=name,
            main=main,
            timezone=timezone,
            country=country,
            state=state,
            city=city,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            postal_code=postal_code,
            phone_number=phone_number,
            latitude=latitude,
            longitude=longitude,
            radius=radius,
            siret=siret,
        )

        locations_location.additional_properties = d
        return locations_location

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
