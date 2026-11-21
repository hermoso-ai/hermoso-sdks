from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conversion_send_result_destinations_item_mode import (
    ConversionSendResultDestinationsItemMode,
)
from typing import cast

if TYPE_CHECKING:
    from ..models.conversion_send_result_destinations_item_failures_item import (
        ConversionSendResultDestinationsItemFailuresItem,
    )
    from ..models.conversion_send_result_destinations_item_skipped_item import (
        ConversionSendResultDestinationsItemSkippedItem,
    )


T = TypeVar("T", bound="ConversionSendResultDestinationsItem")


@_attrs_define
class ConversionSendResultDestinationsItem:
    """
    Attributes:
        destination_id (str | Unset):
        platform (str | Unset):
        mode (ConversionSendResultDestinationsItemMode | Unset):
        events_sent (int | Unset):
        events_accepted (int | None | Unset):
        events_skipped (int | Unset):
        failures (list[ConversionSendResultDestinationsItemFailuresItem] | Unset):
        skipped (list[ConversionSendResultDestinationsItemSkippedItem] | Unset):
        error (str | Unset):
        trace_id (None | str | Unset):
        note (str | Unset):
    """

    destination_id: str | Unset = UNSET
    platform: str | Unset = UNSET
    mode: ConversionSendResultDestinationsItemMode | Unset = UNSET
    events_sent: int | Unset = UNSET
    events_accepted: int | None | Unset = UNSET
    events_skipped: int | Unset = UNSET
    failures: list[ConversionSendResultDestinationsItemFailuresItem] | Unset = UNSET
    skipped: list[ConversionSendResultDestinationsItemSkippedItem] | Unset = UNSET
    error: str | Unset = UNSET
    trace_id: None | str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_id = self.destination_id

        platform = self.platform

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        events_sent = self.events_sent

        events_accepted: int | None | Unset
        if isinstance(self.events_accepted, Unset):
            events_accepted = UNSET
        else:
            events_accepted = self.events_accepted

        events_skipped = self.events_skipped

        failures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failures, Unset):
            failures = []
            for failures_item_data in self.failures:
                failures_item = failures_item_data.to_dict()
                failures.append(failures_item)

        skipped: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skipped, Unset):
            skipped = []
            for skipped_item_data in self.skipped:
                skipped_item = skipped_item_data.to_dict()
                skipped.append(skipped_item)

        error = self.error

        trace_id: None | str | Unset
        if isinstance(self.trace_id, Unset):
            trace_id = UNSET
        else:
            trace_id = self.trace_id

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_id is not UNSET:
            field_dict["destination_id"] = destination_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if mode is not UNSET:
            field_dict["mode"] = mode
        if events_sent is not UNSET:
            field_dict["events_sent"] = events_sent
        if events_accepted is not UNSET:
            field_dict["events_accepted"] = events_accepted
        if events_skipped is not UNSET:
            field_dict["events_skipped"] = events_skipped
        if failures is not UNSET:
            field_dict["failures"] = failures
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if error is not UNSET:
            field_dict["error"] = error
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_send_result_destinations_item_failures_item import (
            ConversionSendResultDestinationsItemFailuresItem,
        )  # noqa: PLC0415
        from ..models.conversion_send_result_destinations_item_skipped_item import (
            ConversionSendResultDestinationsItemSkippedItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        destination_id = d.pop("destination_id", UNSET)

        platform = d.pop("platform", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: ConversionSendResultDestinationsItemMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = ConversionSendResultDestinationsItemMode(_mode)

        events_sent = d.pop("events_sent", UNSET)

        def _parse_events_accepted(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        events_accepted = _parse_events_accepted(d.pop("events_accepted", UNSET))

        events_skipped = d.pop("events_skipped", UNSET)

        _failures = d.pop("failures", UNSET)
        failures: list[ConversionSendResultDestinationsItemFailuresItem] | Unset = UNSET
        if _failures is not UNSET:
            failures = []
            for failures_item_data in _failures:
                failures_item = (
                    ConversionSendResultDestinationsItemFailuresItem.from_dict(
                        failures_item_data
                    )
                )

                failures.append(failures_item)

        _skipped = d.pop("skipped", UNSET)
        skipped: list[ConversionSendResultDestinationsItemSkippedItem] | Unset = UNSET
        if _skipped is not UNSET:
            skipped = []
            for skipped_item_data in _skipped:
                skipped_item = (
                    ConversionSendResultDestinationsItemSkippedItem.from_dict(
                        skipped_item_data
                    )
                )

                skipped.append(skipped_item)

        error = d.pop("error", UNSET)

        def _parse_trace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trace_id = _parse_trace_id(d.pop("trace_id", UNSET))

        note = d.pop("note", UNSET)

        conversion_send_result_destinations_item = cls(
            destination_id=destination_id,
            platform=platform,
            mode=mode,
            events_sent=events_sent,
            events_accepted=events_accepted,
            events_skipped=events_skipped,
            failures=failures,
            skipped=skipped,
            error=error,
            trace_id=trace_id,
            note=note,
        )

        conversion_send_result_destinations_item.additional_properties = d
        return conversion_send_result_destinations_item

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
