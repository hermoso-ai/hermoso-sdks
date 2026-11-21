from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="BestTimeSlotsItem")


@_attrs_define
class BestTimeSlotsItem:
    """
    Attributes:
        platform (str | Unset):
        day_of_week (int | Unset):
        hour (int | Unset):
        avg_engagement (float | None | Unset):
        post_count (int | Unset):
        lift (float | None | Unset):
    """

    platform: str | Unset = UNSET
    day_of_week: int | Unset = UNSET
    hour: int | Unset = UNSET
    avg_engagement: float | None | Unset = UNSET
    post_count: int | Unset = UNSET
    lift: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform

        day_of_week = self.day_of_week

        hour = self.hour

        avg_engagement: float | None | Unset
        if isinstance(self.avg_engagement, Unset):
            avg_engagement = UNSET
        else:
            avg_engagement = self.avg_engagement

        post_count = self.post_count

        lift: float | None | Unset
        if isinstance(self.lift, Unset):
            lift = UNSET
        else:
            lift = self.lift

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform is not UNSET:
            field_dict["platform"] = platform
        if day_of_week is not UNSET:
            field_dict["day_of_week"] = day_of_week
        if hour is not UNSET:
            field_dict["hour"] = hour
        if avg_engagement is not UNSET:
            field_dict["avg_engagement"] = avg_engagement
        if post_count is not UNSET:
            field_dict["post_count"] = post_count
        if lift is not UNSET:
            field_dict["lift"] = lift

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform = d.pop("platform", UNSET)

        day_of_week = d.pop("day_of_week", UNSET)

        hour = d.pop("hour", UNSET)

        def _parse_avg_engagement(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_engagement = _parse_avg_engagement(d.pop("avg_engagement", UNSET))

        post_count = d.pop("post_count", UNSET)

        def _parse_lift(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lift = _parse_lift(d.pop("lift", UNSET))

        best_time_slots_item = cls(
            platform=platform,
            day_of_week=day_of_week,
            hour=hour,
            avg_engagement=avg_engagement,
            post_count=post_count,
            lift=lift,
        )

        best_time_slots_item.additional_properties = d
        return best_time_slots_item

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
