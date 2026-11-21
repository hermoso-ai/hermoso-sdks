from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.posting_frequency_object import PostingFrequencyObject

if TYPE_CHECKING:
    from ..models.posting_frequency_channels_item import PostingFrequencyChannelsItem
    from ..models.posting_frequency_frequency_item import PostingFrequencyFrequencyItem


T = TypeVar("T", bound="PostingFrequency")


@_attrs_define
class PostingFrequency:
    """
    Attributes:
        object_ (PostingFrequencyObject | Unset):
        zone (str | Unset):
        days (int | Unset):
        frequency (list[PostingFrequencyFrequencyItem] | Unset):
        channels (list[PostingFrequencyChannelsItem] | Unset):
        text (str | Unset):
    """

    object_: PostingFrequencyObject | Unset = UNSET
    zone: str | Unset = UNSET
    days: int | Unset = UNSET
    frequency: list[PostingFrequencyFrequencyItem] | Unset = UNSET
    channels: list[PostingFrequencyChannelsItem] | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        zone = self.zone

        days = self.days

        frequency: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = []
            for frequency_item_data in self.frequency:
                frequency_item = frequency_item_data.to_dict()
                frequency.append(frequency_item)

        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if zone is not UNSET:
            field_dict["zone"] = zone
        if days is not UNSET:
            field_dict["days"] = days
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if channels is not UNSET:
            field_dict["channels"] = channels
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.posting_frequency_channels_item import (
            PostingFrequencyChannelsItem,
        )  # noqa: PLC0415
        from ..models.posting_frequency_frequency_item import (
            PostingFrequencyFrequencyItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: PostingFrequencyObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = PostingFrequencyObject(_object_)

        zone = d.pop("zone", UNSET)

        days = d.pop("days", UNSET)

        _frequency = d.pop("frequency", UNSET)
        frequency: list[PostingFrequencyFrequencyItem] | Unset = UNSET
        if _frequency is not UNSET:
            frequency = []
            for frequency_item_data in _frequency:
                frequency_item = PostingFrequencyFrequencyItem.from_dict(
                    frequency_item_data
                )

                frequency.append(frequency_item)

        _channels = d.pop("channels", UNSET)
        channels: list[PostingFrequencyChannelsItem] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = PostingFrequencyChannelsItem.from_dict(
                    channels_item_data
                )

                channels.append(channels_item)

        text = d.pop("text", UNSET)

        posting_frequency = cls(
            object_=object_,
            zone=zone,
            days=days,
            frequency=frequency,
            channels=channels,
            text=text,
        )

        posting_frequency.additional_properties = d
        return posting_frequency

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
