from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connection_object import ConnectionObject
from typing import cast

if TYPE_CHECKING:
    from ..models.connection_accounts_item import ConnectionAccountsItem


T = TypeVar("T", bound="Connection")


@_attrs_define
class Connection:
    """
    Attributes:
        object_ (ConnectionObject | Unset):
        provider (str | Unset):
        name (str | Unset):
        account (None | str | Unset):
        accounts (list[ConnectionAccountsItem] | Unset): On a channel that holds several accounts (TikTok, X, YouTube,
            Threads, Pinterest, Reddit, Bluesky, Telegram), each one.
        needs_reconnect (bool | Unset):
        account_selection_required (bool | Unset): This provider needs Pages chosen for the brand
            (list_connector_accounts / set_connector_accounts).
    """

    object_: ConnectionObject | Unset = UNSET
    provider: str | Unset = UNSET
    name: str | Unset = UNSET
    account: None | str | Unset = UNSET
    accounts: list[ConnectionAccountsItem] | Unset = UNSET
    needs_reconnect: bool | Unset = UNSET
    account_selection_required: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        provider = self.provider

        name = self.name

        account: None | str | Unset
        if isinstance(self.account, Unset):
            account = UNSET
        else:
            account = self.account

        accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)

        needs_reconnect = self.needs_reconnect

        account_selection_required = self.account_selection_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if provider is not UNSET:
            field_dict["provider"] = provider
        if name is not UNSET:
            field_dict["name"] = name
        if account is not UNSET:
            field_dict["account"] = account
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if needs_reconnect is not UNSET:
            field_dict["needs_reconnect"] = needs_reconnect
        if account_selection_required is not UNSET:
            field_dict["account_selection_required"] = account_selection_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_accounts_item import ConnectionAccountsItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ConnectionObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ConnectionObject(_object_)

        provider = d.pop("provider", UNSET)

        name = d.pop("name", UNSET)

        def _parse_account(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account = _parse_account(d.pop("account", UNSET))

        _accounts = d.pop("accounts", UNSET)
        accounts: list[ConnectionAccountsItem] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for accounts_item_data in _accounts:
                accounts_item = ConnectionAccountsItem.from_dict(accounts_item_data)

                accounts.append(accounts_item)

        needs_reconnect = d.pop("needs_reconnect", UNSET)

        account_selection_required = d.pop("account_selection_required", UNSET)

        connection = cls(
            object_=object_,
            provider=provider,
            name=name,
            account=account,
            accounts=accounts,
            needs_reconnect=needs_reconnect,
            account_selection_required=account_selection_required,
        )

        connection.additional_properties = d
        return connection

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
