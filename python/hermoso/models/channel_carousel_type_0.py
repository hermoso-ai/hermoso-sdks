from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="ChannelCarouselType0")


@_attrs_define
class ChannelCarouselType0:
    """
    Attributes:
        min_ (int | Unset):
        max_ (int | None | Unset): The vendor’s own cap. null means the vendor publishes no number — render that as "no
            documented limit", never as unlimited and never as an invented cap.
        effective_max (int | Unset):
        video (bool | Unset):
    """

    min_: int | Unset = UNSET
    max_: int | None | Unset = UNSET
    effective_max: int | Unset = UNSET
    video: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_ = self.min_

        max_: int | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        effective_max = self.effective_max

        video = self.video

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if effective_max is not UNSET:
            field_dict["effective_max"] = effective_max
        if video is not UNSET:
            field_dict["video"] = video

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_ = d.pop("min", UNSET)

        def _parse_max_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        effective_max = d.pop("effective_max", UNSET)

        video = d.pop("video", UNSET)

        channel_carousel_type_0 = cls(
            min_=min_,
            max_=max_,
            effective_max=effective_max,
            video=video,
        )

        channel_carousel_type_0.additional_properties = d
        return channel_carousel_type_0

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
