from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.inbox_stats_object import InboxStatsObject

if TYPE_CHECKING:
    from ..models.inbox_stats_by_platform_item import InboxStatsByPlatformItem
    from ..models.inbox_stats_conversations import InboxStatsConversations
    from ..models.inbox_stats_coverage import InboxStatsCoverage
    from ..models.inbox_stats_heatmap import InboxStatsHeatmap
    from ..models.inbox_stats_response_time import InboxStatsResponseTime
    from ..models.inbox_stats_summary import InboxStatsSummary
    from ..models.inbox_stats_timeseries_item import InboxStatsTimeseriesItem
    from ..models.inbox_stats_top_accounts_item import InboxStatsTopAccountsItem
    from ..models.inbox_stats_waiting import InboxStatsWaiting


T = TypeVar("T", bound="InboxStats")


@_attrs_define
class InboxStats:
    """
    Attributes:
        object_ (InboxStatsObject | Unset):
        from_ (str | Unset):
        to (str | Unset):
        zone (str | Unset):
        summary (InboxStatsSummary | Unset):
        timeseries (list[InboxStatsTimeseriesItem] | Unset):
        by_platform (list[InboxStatsByPlatformItem] | Unset):
        heatmap (InboxStatsHeatmap | Unset):
        response_time (InboxStatsResponseTime | Unset):
        top_accounts (list[InboxStatsTopAccountsItem] | Unset):
        conversations (InboxStatsConversations | Unset):
        waiting (InboxStatsWaiting | Unset):
        coverage (InboxStatsCoverage | Unset):
        text (str | Unset):
    """

    object_: InboxStatsObject | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    zone: str | Unset = UNSET
    summary: InboxStatsSummary | Unset = UNSET
    timeseries: list[InboxStatsTimeseriesItem] | Unset = UNSET
    by_platform: list[InboxStatsByPlatformItem] | Unset = UNSET
    heatmap: InboxStatsHeatmap | Unset = UNSET
    response_time: InboxStatsResponseTime | Unset = UNSET
    top_accounts: list[InboxStatsTopAccountsItem] | Unset = UNSET
    conversations: InboxStatsConversations | Unset = UNSET
    waiting: InboxStatsWaiting | Unset = UNSET
    coverage: InboxStatsCoverage | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        from_ = self.from_

        to = self.to

        zone = self.zone

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        timeseries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.timeseries, Unset):
            timeseries = []
            for timeseries_item_data in self.timeseries:
                timeseries_item = timeseries_item_data.to_dict()
                timeseries.append(timeseries_item)

        by_platform: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_platform, Unset):
            by_platform = []
            for by_platform_item_data in self.by_platform:
                by_platform_item = by_platform_item_data.to_dict()
                by_platform.append(by_platform_item)

        heatmap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.heatmap, Unset):
            heatmap = self.heatmap.to_dict()

        response_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_time, Unset):
            response_time = self.response_time.to_dict()

        top_accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_accounts, Unset):
            top_accounts = []
            for top_accounts_item_data in self.top_accounts:
                top_accounts_item = top_accounts_item_data.to_dict()
                top_accounts.append(top_accounts_item)

        conversations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conversations, Unset):
            conversations = self.conversations.to_dict()

        waiting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.waiting, Unset):
            waiting = self.waiting.to_dict()

        coverage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coverage, Unset):
            coverage = self.coverage.to_dict()

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if zone is not UNSET:
            field_dict["zone"] = zone
        if summary is not UNSET:
            field_dict["summary"] = summary
        if timeseries is not UNSET:
            field_dict["timeseries"] = timeseries
        if by_platform is not UNSET:
            field_dict["byPlatform"] = by_platform
        if heatmap is not UNSET:
            field_dict["heatmap"] = heatmap
        if response_time is not UNSET:
            field_dict["responseTime"] = response_time
        if top_accounts is not UNSET:
            field_dict["topAccounts"] = top_accounts
        if conversations is not UNSET:
            field_dict["conversations"] = conversations
        if waiting is not UNSET:
            field_dict["waiting"] = waiting
        if coverage is not UNSET:
            field_dict["coverage"] = coverage
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inbox_stats_by_platform_item import InboxStatsByPlatformItem  # noqa: PLC0415
        from ..models.inbox_stats_conversations import InboxStatsConversations  # noqa: PLC0415
        from ..models.inbox_stats_coverage import InboxStatsCoverage  # noqa: PLC0415
        from ..models.inbox_stats_heatmap import InboxStatsHeatmap  # noqa: PLC0415
        from ..models.inbox_stats_response_time import InboxStatsResponseTime  # noqa: PLC0415
        from ..models.inbox_stats_summary import InboxStatsSummary  # noqa: PLC0415
        from ..models.inbox_stats_timeseries_item import InboxStatsTimeseriesItem  # noqa: PLC0415
        from ..models.inbox_stats_top_accounts_item import InboxStatsTopAccountsItem  # noqa: PLC0415
        from ..models.inbox_stats_waiting import InboxStatsWaiting  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: InboxStatsObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = InboxStatsObject(_object_)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        zone = d.pop("zone", UNSET)

        _summary = d.pop("summary", UNSET)
        summary: InboxStatsSummary | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = InboxStatsSummary.from_dict(_summary)

        _timeseries = d.pop("timeseries", UNSET)
        timeseries: list[InboxStatsTimeseriesItem] | Unset = UNSET
        if _timeseries is not UNSET:
            timeseries = []
            for timeseries_item_data in _timeseries:
                timeseries_item = InboxStatsTimeseriesItem.from_dict(
                    timeseries_item_data
                )

                timeseries.append(timeseries_item)

        _by_platform = d.pop("byPlatform", UNSET)
        by_platform: list[InboxStatsByPlatformItem] | Unset = UNSET
        if _by_platform is not UNSET:
            by_platform = []
            for by_platform_item_data in _by_platform:
                by_platform_item = InboxStatsByPlatformItem.from_dict(
                    by_platform_item_data
                )

                by_platform.append(by_platform_item)

        _heatmap = d.pop("heatmap", UNSET)
        heatmap: InboxStatsHeatmap | Unset
        if isinstance(_heatmap, Unset):
            heatmap = UNSET
        else:
            heatmap = InboxStatsHeatmap.from_dict(_heatmap)

        _response_time = d.pop("responseTime", UNSET)
        response_time: InboxStatsResponseTime | Unset
        if isinstance(_response_time, Unset):
            response_time = UNSET
        else:
            response_time = InboxStatsResponseTime.from_dict(_response_time)

        _top_accounts = d.pop("topAccounts", UNSET)
        top_accounts: list[InboxStatsTopAccountsItem] | Unset = UNSET
        if _top_accounts is not UNSET:
            top_accounts = []
            for top_accounts_item_data in _top_accounts:
                top_accounts_item = InboxStatsTopAccountsItem.from_dict(
                    top_accounts_item_data
                )

                top_accounts.append(top_accounts_item)

        _conversations = d.pop("conversations", UNSET)
        conversations: InboxStatsConversations | Unset
        if isinstance(_conversations, Unset):
            conversations = UNSET
        else:
            conversations = InboxStatsConversations.from_dict(_conversations)

        _waiting = d.pop("waiting", UNSET)
        waiting: InboxStatsWaiting | Unset
        if isinstance(_waiting, Unset):
            waiting = UNSET
        else:
            waiting = InboxStatsWaiting.from_dict(_waiting)

        _coverage = d.pop("coverage", UNSET)
        coverage: InboxStatsCoverage | Unset
        if isinstance(_coverage, Unset):
            coverage = UNSET
        else:
            coverage = InboxStatsCoverage.from_dict(_coverage)

        text = d.pop("text", UNSET)

        inbox_stats = cls(
            object_=object_,
            from_=from_,
            to=to,
            zone=zone,
            summary=summary,
            timeseries=timeseries,
            by_platform=by_platform,
            heatmap=heatmap,
            response_time=response_time,
            top_accounts=top_accounts,
            conversations=conversations,
            waiting=waiting,
            coverage=coverage,
            text=text,
        )

        inbox_stats.additional_properties = d
        return inbox_stats

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
