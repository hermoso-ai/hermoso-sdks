from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.content_decay_object import ContentDecayObject

if TYPE_CHECKING:
    from ..models.content_decay_buckets_item import ContentDecayBucketsItem
    from ..models.content_decay_channels_item import ContentDecayChannelsItem


T = TypeVar("T", bound="ContentDecay")


@_attrs_define
class ContentDecay:
    """
    Attributes:
        object_ (ContentDecayObject | Unset):
        buckets (list[ContentDecayBucketsItem] | Unset):
        channels (list[ContentDecayChannelsItem] | Unset):
        text (str | Unset):
    """

    object_: ContentDecayObject | Unset = UNSET
    buckets: list[ContentDecayBucketsItem] | Unset = UNSET
    channels: list[ContentDecayChannelsItem] | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        buckets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()
                buckets.append(buckets_item)

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
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if channels is not UNSET:
            field_dict["channels"] = channels
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_decay_buckets_item import ContentDecayBucketsItem  # noqa: PLC0415
        from ..models.content_decay_channels_item import ContentDecayChannelsItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ContentDecayObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ContentDecayObject(_object_)

        _buckets = d.pop("buckets", UNSET)
        buckets: list[ContentDecayBucketsItem] | Unset = UNSET
        if _buckets is not UNSET:
            buckets = []
            for buckets_item_data in _buckets:
                buckets_item = ContentDecayBucketsItem.from_dict(buckets_item_data)

                buckets.append(buckets_item)

        _channels = d.pop("channels", UNSET)
        channels: list[ContentDecayChannelsItem] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = ContentDecayChannelsItem.from_dict(channels_item_data)

                channels.append(channels_item)

        text = d.pop("text", UNSET)

        content_decay = cls(
            object_=object_,
            buckets=buckets,
            channels=channels,
            text=text,
        )

        content_decay.additional_properties = d
        return content_decay

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
