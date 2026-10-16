from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_response_errors_item_code import ErrorResponseErrorsItemCode

T = TypeVar("T", bound="ErrorResponseErrorsItem")


@_attrs_define
class ErrorResponseErrorsItem:
    code: ErrorResponseErrorsItemCode
    """ What went wrong, stable across releases and safe to branch on. `unknown_error` means the failure carries no
    classification yet. """
    message: str
    """ The failure in words, for a human reader. Wording can change at any time, so do not match on it. """
    field: None | str
    """ The request field the failure belongs to, or null when the failure belongs to the request as a whole. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        field: None | str
        field = self.field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
                "field": field,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = ErrorResponseErrorsItemCode(d.pop("code"))

        message = d.pop("message")

        def _parse_field(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        field = _parse_field(d.pop("field"))

        error_response_errors_item = cls(
            code=code,
            message=message,
            field=field,
        )

        error_response_errors_item.additional_properties = d
        return error_response_errors_item

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
