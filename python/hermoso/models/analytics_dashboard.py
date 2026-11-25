from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.analytics_dashboard_object import AnalyticsDashboardObject
from typing import cast

if TYPE_CHECKING:
    from ..models.analytics_dashboard_channels_item import (
        AnalyticsDashboardChannelsItem,
    )
    from ..models.analytics_dashboard_current import AnalyticsDashboardCurrent
    from ..models.analytics_dashboard_daily_item import AnalyticsDashboardDailyItem
    from ..models.analytics_dashboard_previous import AnalyticsDashboardPrevious
    from ..models.analytics_dashboard_recent_posts_item import (
        AnalyticsDashboardRecentPostsItem,
    )
    from ..models.analytics_dashboard_top_posts_item import (
        AnalyticsDashboardTopPostsItem,
    )
    from ..models.analytics_dashboard_totals import AnalyticsDashboardTotals


T = TypeVar("T", bound="AnalyticsDashboard")


@_attrs_define
class AnalyticsDashboard:
    """
    Attributes:
        object_ (AnalyticsDashboardObject | Unset):
        current (AnalyticsDashboardCurrent | Unset):
        previous (AnalyticsDashboardPrevious | Unset):
        totals (AnalyticsDashboardTotals | Unset):
        channels (list[AnalyticsDashboardChannelsItem] | Unset):
        daily (list[AnalyticsDashboardDailyItem] | Unset):
        top_posts (list[AnalyticsDashboardTopPostsItem] | Unset):
        recent_posts (list[AnalyticsDashboardRecentPostsItem] | Unset):
        notes (list[str] | Unset):
        text (str | Unset):
    """

    object_: AnalyticsDashboardObject | Unset = UNSET
    current: AnalyticsDashboardCurrent | Unset = UNSET
    previous: AnalyticsDashboardPrevious | Unset = UNSET
    totals: AnalyticsDashboardTotals | Unset = UNSET
    channels: list[AnalyticsDashboardChannelsItem] | Unset = UNSET
    daily: list[AnalyticsDashboardDailyItem] | Unset = UNSET
    top_posts: list[AnalyticsDashboardTopPostsItem] | Unset = UNSET
    recent_posts: list[AnalyticsDashboardRecentPostsItem] | Unset = UNSET
    notes: list[str] | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        current: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current, Unset):
            current = self.current.to_dict()

        previous: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous, Unset):
            previous = self.previous.to_dict()

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        daily: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.daily, Unset):
            daily = []
            for daily_item_data in self.daily:
                daily_item = daily_item_data.to_dict()
                daily.append(daily_item)

        top_posts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_posts, Unset):
            top_posts = []
            for top_posts_item_data in self.top_posts:
                top_posts_item = top_posts_item_data.to_dict()
                top_posts.append(top_posts_item)

        recent_posts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recent_posts, Unset):
            recent_posts = []
            for recent_posts_item_data in self.recent_posts:
                recent_posts_item = recent_posts_item_data.to_dict()
                recent_posts.append(recent_posts_item)

        notes: list[str] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if current is not UNSET:
            field_dict["current"] = current
        if previous is not UNSET:
            field_dict["previous"] = previous
        if totals is not UNSET:
            field_dict["totals"] = totals
        if channels is not UNSET:
            field_dict["channels"] = channels
        if daily is not UNSET:
            field_dict["daily"] = daily
        if top_posts is not UNSET:
            field_dict["top_posts"] = top_posts
        if recent_posts is not UNSET:
            field_dict["recent_posts"] = recent_posts
        if notes is not UNSET:
            field_dict["notes"] = notes
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_dashboard_channels_item import (
            AnalyticsDashboardChannelsItem,
        )  # noqa: PLC0415
        from ..models.analytics_dashboard_current import AnalyticsDashboardCurrent  # noqa: PLC0415
        from ..models.analytics_dashboard_daily_item import AnalyticsDashboardDailyItem  # noqa: PLC0415
        from ..models.analytics_dashboard_previous import AnalyticsDashboardPrevious  # noqa: PLC0415
        from ..models.analytics_dashboard_recent_posts_item import (
            AnalyticsDashboardRecentPostsItem,
        )  # noqa: PLC0415
        from ..models.analytics_dashboard_top_posts_item import (
            AnalyticsDashboardTopPostsItem,
        )  # noqa: PLC0415
        from ..models.analytics_dashboard_totals import AnalyticsDashboardTotals  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: AnalyticsDashboardObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = AnalyticsDashboardObject(_object_)

        _current = d.pop("current", UNSET)
        current: AnalyticsDashboardCurrent | Unset
        if isinstance(_current, Unset):
            current = UNSET
        else:
            current = AnalyticsDashboardCurrent.from_dict(_current)

        _previous = d.pop("previous", UNSET)
        previous: AnalyticsDashboardPrevious | Unset
        if isinstance(_previous, Unset):
            previous = UNSET
        else:
            previous = AnalyticsDashboardPrevious.from_dict(_previous)

        _totals = d.pop("totals", UNSET)
        totals: AnalyticsDashboardTotals | Unset
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = AnalyticsDashboardTotals.from_dict(_totals)

        _channels = d.pop("channels", UNSET)
        channels: list[AnalyticsDashboardChannelsItem] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = AnalyticsDashboardChannelsItem.from_dict(
                    channels_item_data
                )

                channels.append(channels_item)

        _daily = d.pop("daily", UNSET)
        daily: list[AnalyticsDashboardDailyItem] | Unset = UNSET
        if _daily is not UNSET:
            daily = []
            for daily_item_data in _daily:
                daily_item = AnalyticsDashboardDailyItem.from_dict(daily_item_data)

                daily.append(daily_item)

        _top_posts = d.pop("top_posts", UNSET)
        top_posts: list[AnalyticsDashboardTopPostsItem] | Unset = UNSET
        if _top_posts is not UNSET:
            top_posts = []
            for top_posts_item_data in _top_posts:
                top_posts_item = AnalyticsDashboardTopPostsItem.from_dict(
                    top_posts_item_data
                )

                top_posts.append(top_posts_item)

        _recent_posts = d.pop("recent_posts", UNSET)
        recent_posts: list[AnalyticsDashboardRecentPostsItem] | Unset = UNSET
        if _recent_posts is not UNSET:
            recent_posts = []
            for recent_posts_item_data in _recent_posts:
                recent_posts_item = AnalyticsDashboardRecentPostsItem.from_dict(
                    recent_posts_item_data
                )

                recent_posts.append(recent_posts_item)

        notes = cast(list[str], d.pop("notes", UNSET))

        text = d.pop("text", UNSET)

        analytics_dashboard = cls(
            object_=object_,
            current=current,
            previous=previous,
            totals=totals,
            channels=channels,
            daily=daily,
            top_posts=top_posts,
            recent_posts=recent_posts,
            notes=notes,
            text=text,
        )

        analytics_dashboard.additional_properties = d
        return analytics_dashboard

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
