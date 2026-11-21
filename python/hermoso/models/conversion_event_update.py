from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="ConversionEventUpdate")


@_attrs_define
class ConversionEventUpdate:
    """
    Attributes:
        value (float):
        currency (str | Unset):
        event_name (str | Unset):
    """

    value: float
    currency: str | Unset = UNSET
    event_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        currency = self.currency

        event_name = self.event_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if event_name is not UNSET:
            field_dict["event_name"] = event_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        currency = d.pop("currency", UNSET)

        event_name = d.pop("event_name", UNSET)

        conversion_event_update = cls(
            value=value,
            currency=currency,
            event_name=event_name,
        )

        conversion_event_update.additional_properties = d
        return conversion_event_update

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
