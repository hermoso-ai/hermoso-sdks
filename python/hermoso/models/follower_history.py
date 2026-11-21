from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.follower_history_object import FollowerHistoryObject

if TYPE_CHECKING:
    from ..models.follower_history_accounts_item import FollowerHistoryAccountsItem
    from ..models.follower_history_date_range import FollowerHistoryDateRange


T = TypeVar("T", bound="FollowerHistory")


@_attrs_define
class FollowerHistory:
    """
    Attributes:
        object_ (FollowerHistoryObject | Unset):
        granularity (str | Unset):
        date_range (FollowerHistoryDateRange | Unset):
        accounts (list[FollowerHistoryAccountsItem] | Unset):
        warning (str | Unset):
        text (str | Unset):
    """

    object_: FollowerHistoryObject | Unset = UNSET
    granularity: str | Unset = UNSET
    date_range: FollowerHistoryDateRange | Unset = UNSET
    accounts: list[FollowerHistoryAccountsItem] | Unset = UNSET
    warning: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        granularity = self.granularity

        date_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_range, Unset):
            date_range = self.date_range.to_dict()

        accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)

        warning = self.warning

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if granularity is not UNSET:
            field_dict["granularity"] = granularity
        if date_range is not UNSET:
            field_dict["dateRange"] = date_range
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if warning is not UNSET:
            field_dict["warning"] = warning
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.follower_history_accounts_item import FollowerHistoryAccountsItem  # noqa: PLC0415
        from ..models.follower_history_date_range import FollowerHistoryDateRange  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: FollowerHistoryObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = FollowerHistoryObject(_object_)

        granularity = d.pop("granularity", UNSET)

        _date_range = d.pop("dateRange", UNSET)
        date_range: FollowerHistoryDateRange | Unset
        if isinstance(_date_range, Unset):
            date_range = UNSET
        else:
            date_range = FollowerHistoryDateRange.from_dict(_date_range)

        _accounts = d.pop("accounts", UNSET)
        accounts: list[FollowerHistoryAccountsItem] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for accounts_item_data in _accounts:
                accounts_item = FollowerHistoryAccountsItem.from_dict(
                    accounts_item_data
                )

                accounts.append(accounts_item)

        warning = d.pop("warning", UNSET)

        text = d.pop("text", UNSET)

        follower_history = cls(
            object_=object_,
            granularity=granularity,
            date_range=date_range,
            accounts=accounts,
            warning=warning,
            text=text,
        )

        follower_history.additional_properties = d
        return follower_history

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
