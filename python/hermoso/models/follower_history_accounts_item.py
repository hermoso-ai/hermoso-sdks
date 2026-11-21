from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.follower_history_accounts_item_points_item import (
        FollowerHistoryAccountsItemPointsItem,
    )


T = TypeVar("T", bound="FollowerHistoryAccountsItem")


@_attrs_define
class FollowerHistoryAccountsItem:
    """
    Attributes:
        channel (str | Unset):
        account (None | str | Unset):
        label (None | str | Unset):
        latest (int | None | Unset):
        growth (int | None | Unset):
        points (list[FollowerHistoryAccountsItemPointsItem] | Unset):
    """

    channel: str | Unset = UNSET
    account: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    latest: int | None | Unset = UNSET
    growth: int | None | Unset = UNSET
    points: list[FollowerHistoryAccountsItemPointsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        account: None | str | Unset
        if isinstance(self.account, Unset):
            account = UNSET
        else:
            account = self.account

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        latest: int | None | Unset
        if isinstance(self.latest, Unset):
            latest = UNSET
        else:
            latest = self.latest

        growth: int | None | Unset
        if isinstance(self.growth, Unset):
            growth = UNSET
        else:
            growth = self.growth

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if account is not UNSET:
            field_dict["account"] = account
        if label is not UNSET:
            field_dict["label"] = label
        if latest is not UNSET:
            field_dict["latest"] = latest
        if growth is not UNSET:
            field_dict["growth"] = growth
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.follower_history_accounts_item_points_item import (
            FollowerHistoryAccountsItemPointsItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        def _parse_account(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account = _parse_account(d.pop("account", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_latest(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latest = _parse_latest(d.pop("latest", UNSET))

        def _parse_growth(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        growth = _parse_growth(d.pop("growth", UNSET))

        _points = d.pop("points", UNSET)
        points: list[FollowerHistoryAccountsItemPointsItem] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = FollowerHistoryAccountsItemPointsItem.from_dict(
                    points_item_data
                )

                points.append(points_item)

        follower_history_accounts_item = cls(
            channel=channel,
            account=account,
            label=label,
            latest=latest,
            growth=growth,
            points=points,
        )

        follower_history_accounts_item.additional_properties = d
        return follower_history_accounts_item

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
