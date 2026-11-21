from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="PostingFrequencyFrequencyItem")


@_attrs_define
class PostingFrequencyFrequencyItem:
    """
    Attributes:
        platform (str | Unset):
        posts_per_week (int | Unset):
        weeks_count (int | Unset):
        avg_engagement (float | None | Unset):
        avg_engagement_rate (float | None | Unset):
        avg_follower_change (float | None | Unset):
    """

    platform: str | Unset = UNSET
    posts_per_week: int | Unset = UNSET
    weeks_count: int | Unset = UNSET
    avg_engagement: float | None | Unset = UNSET
    avg_engagement_rate: float | None | Unset = UNSET
    avg_follower_change: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform

        posts_per_week = self.posts_per_week

        weeks_count = self.weeks_count

        avg_engagement: float | None | Unset
        if isinstance(self.avg_engagement, Unset):
            avg_engagement = UNSET
        else:
            avg_engagement = self.avg_engagement

        avg_engagement_rate: float | None | Unset
        if isinstance(self.avg_engagement_rate, Unset):
            avg_engagement_rate = UNSET
        else:
            avg_engagement_rate = self.avg_engagement_rate

        avg_follower_change: float | None | Unset
        if isinstance(self.avg_follower_change, Unset):
            avg_follower_change = UNSET
        else:
            avg_follower_change = self.avg_follower_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform is not UNSET:
            field_dict["platform"] = platform
        if posts_per_week is not UNSET:
            field_dict["posts_per_week"] = posts_per_week
        if weeks_count is not UNSET:
            field_dict["weeks_count"] = weeks_count
        if avg_engagement is not UNSET:
            field_dict["avg_engagement"] = avg_engagement
        if avg_engagement_rate is not UNSET:
            field_dict["avg_engagement_rate"] = avg_engagement_rate
        if avg_follower_change is not UNSET:
            field_dict["avg_follower_change"] = avg_follower_change

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform = d.pop("platform", UNSET)

        posts_per_week = d.pop("posts_per_week", UNSET)

        weeks_count = d.pop("weeks_count", UNSET)

        def _parse_avg_engagement(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_engagement = _parse_avg_engagement(d.pop("avg_engagement", UNSET))

        def _parse_avg_engagement_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_engagement_rate = _parse_avg_engagement_rate(
            d.pop("avg_engagement_rate", UNSET)
        )

        def _parse_avg_follower_change(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_follower_change = _parse_avg_follower_change(
            d.pop("avg_follower_change", UNSET)
        )

        posting_frequency_frequency_item = cls(
            platform=platform,
            posts_per_week=posts_per_week,
            weeks_count=weeks_count,
            avg_engagement=avg_engagement,
            avg_engagement_rate=avg_engagement_rate,
            avg_follower_change=avg_follower_change,
        )

        posting_frequency_frequency_item.additional_properties = d
        return posting_frequency_frequency_item

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
