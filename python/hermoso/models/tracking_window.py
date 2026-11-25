from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tracking_window_object import TrackingWindowObject
from ..models.tracking_window_source import TrackingWindowSource
from ..models.tracking_window_status import TrackingWindowStatus
from typing import cast

if TYPE_CHECKING:
    from ..models.tracking_window_latest_type_0 import TrackingWindowLatestType0
    from ..models.tracking_window_quote import TrackingWindowQuote


T = TypeVar("T", bound="TrackingWindow")


@_attrs_define
class TrackingWindow:
    """
    Attributes:
        object_ (TrackingWindowObject | Unset):
        id (str | Unset):
        status (TrackingWindowStatus | Unset):
        source (TrackingWindowSource | Unset):
        channel (None | str | Unset):
        post_id (None | str | Unset):
        url (None | str | Unset):
        tracking_days (int | Unset):
        readings (int | Unset):
        failed_readings (int | Unset):
        latest (None | TrackingWindowLatestType0 | Unset):
        needs_confirm (bool | Unset):
        quote (TrackingWindowQuote | Unset):
        existing (bool | Unset):
        text (str | Unset):
    """

    object_: TrackingWindowObject | Unset = UNSET
    id: str | Unset = UNSET
    status: TrackingWindowStatus | Unset = UNSET
    source: TrackingWindowSource | Unset = UNSET
    channel: None | str | Unset = UNSET
    post_id: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    tracking_days: int | Unset = UNSET
    readings: int | Unset = UNSET
    failed_readings: int | Unset = UNSET
    latest: None | TrackingWindowLatestType0 | Unset = UNSET
    needs_confirm: bool | Unset = UNSET
    quote: TrackingWindowQuote | Unset = UNSET
    existing: bool | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tracking_window_latest_type_0 import TrackingWindowLatestType0  # noqa: PLC0415

        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        channel: None | str | Unset
        if isinstance(self.channel, Unset):
            channel = UNSET
        else:
            channel = self.channel

        post_id: None | str | Unset
        if isinstance(self.post_id, Unset):
            post_id = UNSET
        else:
            post_id = self.post_id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        tracking_days = self.tracking_days

        readings = self.readings

        failed_readings = self.failed_readings

        latest: dict[str, Any] | None | Unset
        if isinstance(self.latest, Unset):
            latest = UNSET
        elif isinstance(self.latest, TrackingWindowLatestType0):
            latest = self.latest.to_dict()
        else:
            latest = self.latest

        needs_confirm = self.needs_confirm

        quote: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quote, Unset):
            quote = self.quote.to_dict()

        existing = self.existing

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if source is not UNSET:
            field_dict["source"] = source
        if channel is not UNSET:
            field_dict["channel"] = channel
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if url is not UNSET:
            field_dict["url"] = url
        if tracking_days is not UNSET:
            field_dict["tracking_days"] = tracking_days
        if readings is not UNSET:
            field_dict["readings"] = readings
        if failed_readings is not UNSET:
            field_dict["failed_readings"] = failed_readings
        if latest is not UNSET:
            field_dict["latest"] = latest
        if needs_confirm is not UNSET:
            field_dict["needs_confirm"] = needs_confirm
        if quote is not UNSET:
            field_dict["quote"] = quote
        if existing is not UNSET:
            field_dict["existing"] = existing
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tracking_window_latest_type_0 import TrackingWindowLatestType0  # noqa: PLC0415
        from ..models.tracking_window_quote import TrackingWindowQuote  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: TrackingWindowObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = TrackingWindowObject(_object_)

        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: TrackingWindowStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TrackingWindowStatus(_status)

        _source = d.pop("source", UNSET)
        source: TrackingWindowSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = TrackingWindowSource(_source)

        def _parse_channel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel = _parse_channel(d.pop("channel", UNSET))

        def _parse_post_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_id = _parse_post_id(d.pop("post_id", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        tracking_days = d.pop("tracking_days", UNSET)

        readings = d.pop("readings", UNSET)

        failed_readings = d.pop("failed_readings", UNSET)

        def _parse_latest(data: object) -> None | TrackingWindowLatestType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latest_type_0 = TrackingWindowLatestType0.from_dict(data)

                return latest_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TrackingWindowLatestType0 | Unset, data)

        latest = _parse_latest(d.pop("latest", UNSET))

        needs_confirm = d.pop("needs_confirm", UNSET)

        _quote = d.pop("quote", UNSET)
        quote: TrackingWindowQuote | Unset
        if isinstance(_quote, Unset):
            quote = UNSET
        else:
            quote = TrackingWindowQuote.from_dict(_quote)

        existing = d.pop("existing", UNSET)

        text = d.pop("text", UNSET)

        tracking_window = cls(
            object_=object_,
            id=id,
            status=status,
            source=source,
            channel=channel,
            post_id=post_id,
            url=url,
            tracking_days=tracking_days,
            readings=readings,
            failed_readings=failed_readings,
            latest=latest,
            needs_confirm=needs_confirm,
            quote=quote,
            existing=existing,
            text=text,
        )

        tracking_window.additional_properties = d
        return tracking_window

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
