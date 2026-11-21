from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connect_link_object import ConnectLinkObject
from ..models.connect_link_status import ConnectLinkStatus
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.connect_link_account_type_0 import ConnectLinkAccountType0
    from ..models.connect_link_error_type_0 import ConnectLinkErrorType0


T = TypeVar("T", bound="ConnectLink")


@_attrs_define
class ConnectLink:
    """
    Attributes:
        object_ (ConnectLinkObject | Unset):
        id (str | Unset):
        url (str | Unset): Returned when the link is created. Hand it to your customer; it is a bearer link, so treat it
            like a password until it is used or expires.
        provider (str | Unset):
        brand (str | Unset):
        status (ConnectLinkStatus | Unset):
        redirect_url (None | str | Unset):
        state (None | str | Unset):
        created_at (datetime.datetime | Unset):
        expires_at (datetime.datetime | Unset):
        connected_at (datetime.datetime | None | Unset):
        account (ConnectLinkAccountType0 | None | Unset):
        account_selection_required (bool | None | Unset): True for Facebook/Instagram (meta) and LinkedIn: choose which
            Pages the brand may use with list_connector_accounts + set_connector_accounts before posting.
        error (ConnectLinkErrorType0 | None | Unset):
    """

    object_: ConnectLinkObject | Unset = UNSET
    id: str | Unset = UNSET
    url: str | Unset = UNSET
    provider: str | Unset = UNSET
    brand: str | Unset = UNSET
    status: ConnectLinkStatus | Unset = UNSET
    redirect_url: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    connected_at: datetime.datetime | None | Unset = UNSET
    account: ConnectLinkAccountType0 | None | Unset = UNSET
    account_selection_required: bool | None | Unset = UNSET
    error: ConnectLinkErrorType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.connect_link_account_type_0 import ConnectLinkAccountType0  # noqa: PLC0415
        from ..models.connect_link_error_type_0 import ConnectLinkErrorType0  # noqa: PLC0415

        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        url = self.url

        provider = self.provider

        brand = self.brand

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        redirect_url: None | str | Unset
        if isinstance(self.redirect_url, Unset):
            redirect_url = UNSET
        else:
            redirect_url = self.redirect_url

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        connected_at: None | str | Unset
        if isinstance(self.connected_at, Unset):
            connected_at = UNSET
        elif isinstance(self.connected_at, datetime.datetime):
            connected_at = self.connected_at.isoformat()
        else:
            connected_at = self.connected_at

        account: dict[str, Any] | None | Unset
        if isinstance(self.account, Unset):
            account = UNSET
        elif isinstance(self.account, ConnectLinkAccountType0):
            account = self.account.to_dict()
        else:
            account = self.account

        account_selection_required: bool | None | Unset
        if isinstance(self.account_selection_required, Unset):
            account_selection_required = UNSET
        else:
            account_selection_required = self.account_selection_required

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, ConnectLinkErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if provider is not UNSET:
            field_dict["provider"] = provider
        if brand is not UNSET:
            field_dict["brand"] = brand
        if status is not UNSET:
            field_dict["status"] = status
        if redirect_url is not UNSET:
            field_dict["redirect_url"] = redirect_url
        if state is not UNSET:
            field_dict["state"] = state
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if connected_at is not UNSET:
            field_dict["connected_at"] = connected_at
        if account is not UNSET:
            field_dict["account"] = account
        if account_selection_required is not UNSET:
            field_dict["account_selection_required"] = account_selection_required
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connect_link_account_type_0 import ConnectLinkAccountType0  # noqa: PLC0415
        from ..models.connect_link_error_type_0 import ConnectLinkErrorType0  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ConnectLinkObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ConnectLinkObject(_object_)

        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        provider = d.pop("provider", UNSET)

        brand = d.pop("brand", UNSET)

        _status = d.pop("status", UNSET)
        status: ConnectLinkStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ConnectLinkStatus(_status)

        def _parse_redirect_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        redirect_url = _parse_redirect_url(d.pop("redirect_url", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        def _parse_connected_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                connected_at_type_0 = datetime.datetime.fromisoformat(data)

                return connected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        connected_at = _parse_connected_at(d.pop("connected_at", UNSET))

        def _parse_account(data: object) -> ConnectLinkAccountType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                account_type_0 = ConnectLinkAccountType0.from_dict(data)

                return account_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectLinkAccountType0 | None | Unset, data)

        account = _parse_account(d.pop("account", UNSET))

        def _parse_account_selection_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        account_selection_required = _parse_account_selection_required(
            d.pop("account_selection_required", UNSET)
        )

        def _parse_error(data: object) -> ConnectLinkErrorType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = ConnectLinkErrorType0.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectLinkErrorType0 | None | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        connect_link = cls(
            object_=object_,
            id=id,
            url=url,
            provider=provider,
            brand=brand,
            status=status,
            redirect_url=redirect_url,
            state=state,
            created_at=created_at,
            expires_at=expires_at,
            connected_at=connected_at,
            account=account,
            account_selection_required=account_selection_required,
            error=error,
        )

        connect_link.additional_properties = d
        return connect_link

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
