from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.conversion_events_send_events_item import (
        ConversionEventsSendEventsItem,
    )


T = TypeVar("T", bound="ConversionEventsSend")


@_attrs_define
class ConversionEventsSend:
    """
    Attributes:
        events (list[ConversionEventsSendEventsItem]):
        destinations (list[Any] | Unset): Saved destination ids or destination objects, instead of the saved list.
        validate_only (bool | Unset):
        test_code (str | Unset):
        forward (bool | Unset):
        carry_click_ids (bool | Unset):
        source (str | Unset):
    """

    events: list[ConversionEventsSendEventsItem]
    destinations: list[Any] | Unset = UNSET
    validate_only: bool | Unset = UNSET
    test_code: str | Unset = UNSET
    forward: bool | Unset = UNSET
    carry_click_ids: bool | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        destinations: list[Any] | Unset = UNSET
        if not isinstance(self.destinations, Unset):
            destinations = self.destinations

        validate_only = self.validate_only

        test_code = self.test_code

        forward = self.forward

        carry_click_ids = self.carry_click_ids

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
            }
        )
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if validate_only is not UNSET:
            field_dict["validate_only"] = validate_only
        if test_code is not UNSET:
            field_dict["test_code"] = test_code
        if forward is not UNSET:
            field_dict["forward"] = forward
        if carry_click_ids is not UNSET:
            field_dict["carry_click_ids"] = carry_click_ids
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_events_send_events_item import (
            ConversionEventsSendEventsItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = ConversionEventsSendEventsItem.from_dict(events_item_data)

            events.append(events_item)

        destinations = cast(list[Any], d.pop("destinations", UNSET))

        validate_only = d.pop("validate_only", UNSET)

        test_code = d.pop("test_code", UNSET)

        forward = d.pop("forward", UNSET)

        carry_click_ids = d.pop("carry_click_ids", UNSET)

        source = d.pop("source", UNSET)

        conversion_events_send = cls(
            events=events,
            destinations=destinations,
            validate_only=validate_only,
            test_code=test_code,
            forward=forward,
            carry_click_ids=carry_click_ids,
            source=source,
        )

        conversion_events_send.additional_properties = d
        return conversion_events_send

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
