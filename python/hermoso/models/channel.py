from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.channel_object import ChannelObject
from typing import cast

if TYPE_CHECKING:
    from ..models.channel_carousel_type_0 import ChannelCarouselType0


T = TypeVar("T", bound="Channel")


@_attrs_define
class Channel:
    """
    Attributes:
        object_ (ChannelObject | Unset):
        id (str | Unset):
        name (str | Unset):
        connector (str | Unset): The connection this channel is reached through. Several channels can share one —
            Facebook and Instagram both ride the Meta connection.
        available (bool | Unset): Whether this channel can be connected AT ALL on this deployment. False while a
            platform approval is outstanding — a different answer from "you have not connected it yet", and collapsing the
            two would send you to build a connect flow that cannot succeed.
        unavailable_reason (None | str | Unset): Why, when `available` is false.
        connected (bool | Unset):
        needs_reconnect (bool | Unset): A row exists but holds no usable credential. Reconnect in the app, or send the
            account holder a link from POST /v1/connect-links.
        account (None | str | Unset): Which account is connected, where the provider tells us.
        visibilities (list[str] | Unset):
        visibility_notes (None | str | Unset):
        carousel (ChannelCarouselType0 | None | Unset):
        carousel_unsupported_reason (None | str | Unset):
        caption_max (int | None | Unset):
        target_field (None | str | Unset): The key inside `targets` that names WHICH account on this channel to post to.
    """

    object_: ChannelObject | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    connector: str | Unset = UNSET
    available: bool | Unset = UNSET
    unavailable_reason: None | str | Unset = UNSET
    connected: bool | Unset = UNSET
    needs_reconnect: bool | Unset = UNSET
    account: None | str | Unset = UNSET
    visibilities: list[str] | Unset = UNSET
    visibility_notes: None | str | Unset = UNSET
    carousel: ChannelCarouselType0 | None | Unset = UNSET
    carousel_unsupported_reason: None | str | Unset = UNSET
    caption_max: int | None | Unset = UNSET
    target_field: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.channel_carousel_type_0 import ChannelCarouselType0  # noqa: PLC0415

        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        name = self.name

        connector = self.connector

        available = self.available

        unavailable_reason: None | str | Unset
        if isinstance(self.unavailable_reason, Unset):
            unavailable_reason = UNSET
        else:
            unavailable_reason = self.unavailable_reason

        connected = self.connected

        needs_reconnect = self.needs_reconnect

        account: None | str | Unset
        if isinstance(self.account, Unset):
            account = UNSET
        else:
            account = self.account

        visibilities: list[str] | Unset = UNSET
        if not isinstance(self.visibilities, Unset):
            visibilities = self.visibilities

        visibility_notes: None | str | Unset
        if isinstance(self.visibility_notes, Unset):
            visibility_notes = UNSET
        else:
            visibility_notes = self.visibility_notes

        carousel: dict[str, Any] | None | Unset
        if isinstance(self.carousel, Unset):
            carousel = UNSET
        elif isinstance(self.carousel, ChannelCarouselType0):
            carousel = self.carousel.to_dict()
        else:
            carousel = self.carousel

        carousel_unsupported_reason: None | str | Unset
        if isinstance(self.carousel_unsupported_reason, Unset):
            carousel_unsupported_reason = UNSET
        else:
            carousel_unsupported_reason = self.carousel_unsupported_reason

        caption_max: int | None | Unset
        if isinstance(self.caption_max, Unset):
            caption_max = UNSET
        else:
            caption_max = self.caption_max

        target_field: None | str | Unset
        if isinstance(self.target_field, Unset):
            target_field = UNSET
        else:
            target_field = self.target_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if connector is not UNSET:
            field_dict["connector"] = connector
        if available is not UNSET:
            field_dict["available"] = available
        if unavailable_reason is not UNSET:
            field_dict["unavailable_reason"] = unavailable_reason
        if connected is not UNSET:
            field_dict["connected"] = connected
        if needs_reconnect is not UNSET:
            field_dict["needs_reconnect"] = needs_reconnect
        if account is not UNSET:
            field_dict["account"] = account
        if visibilities is not UNSET:
            field_dict["visibilities"] = visibilities
        if visibility_notes is not UNSET:
            field_dict["visibility_notes"] = visibility_notes
        if carousel is not UNSET:
            field_dict["carousel"] = carousel
        if carousel_unsupported_reason is not UNSET:
            field_dict["carousel_unsupported_reason"] = carousel_unsupported_reason
        if caption_max is not UNSET:
            field_dict["caption_max"] = caption_max
        if target_field is not UNSET:
            field_dict["target_field"] = target_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_carousel_type_0 import ChannelCarouselType0  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ChannelObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ChannelObject(_object_)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        connector = d.pop("connector", UNSET)

        available = d.pop("available", UNSET)

        def _parse_unavailable_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unavailable_reason = _parse_unavailable_reason(
            d.pop("unavailable_reason", UNSET)
        )

        connected = d.pop("connected", UNSET)

        needs_reconnect = d.pop("needs_reconnect", UNSET)

        def _parse_account(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account = _parse_account(d.pop("account", UNSET))

        visibilities = cast(list[str], d.pop("visibilities", UNSET))

        def _parse_visibility_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visibility_notes = _parse_visibility_notes(d.pop("visibility_notes", UNSET))

        def _parse_carousel(data: object) -> ChannelCarouselType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                carousel_type_0 = ChannelCarouselType0.from_dict(data)

                return carousel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChannelCarouselType0 | None | Unset, data)

        carousel = _parse_carousel(d.pop("carousel", UNSET))

        def _parse_carousel_unsupported_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        carousel_unsupported_reason = _parse_carousel_unsupported_reason(
            d.pop("carousel_unsupported_reason", UNSET)
        )

        def _parse_caption_max(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        caption_max = _parse_caption_max(d.pop("caption_max", UNSET))

        def _parse_target_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_field = _parse_target_field(d.pop("target_field", UNSET))

        channel = cls(
            object_=object_,
            id=id,
            name=name,
            connector=connector,
            available=available,
            unavailable_reason=unavailable_reason,
            connected=connected,
            needs_reconnect=needs_reconnect,
            account=account,
            visibilities=visibilities,
            visibility_notes=visibility_notes,
            carousel=carousel,
            carousel_unsupported_reason=carousel_unsupported_reason,
            caption_max=caption_max,
            target_field=target_field,
        )

        channel.additional_properties = d
        return channel

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
