from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="ConnectLinkCreate")


@_attrs_define
class ConnectLinkCreate:
    """
    Attributes:
        provider (str): Which platform: meta (Facebook and Instagram), instagram (an Instagram account on its own
            login), tiktok, youtube, linkedin, linkedin_community (comments as a LinkedIn Page), x, pinterest, threads,
            google_business, and the ad platforms. An unsupported one is refused with the list.
        redirect_url (str | Unset): Where your customer lands afterwards. Must sit under a registered address (PUT
            /v1/connect-redirects). Omit to show them a plain “connected, you can close this window” page.
        state (str | Unset): Your own value, up to 500 characters, returned on the redirect and in the webhook so you
            can match the connection to your customer.
        expires_in_minutes (int | Unset): Default 60, at most 2880 (48 hours).
    """

    provider: str
    redirect_url: str | Unset = UNSET
    state: str | Unset = UNSET
    expires_in_minutes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        redirect_url = self.redirect_url

        state = self.state

        expires_in_minutes = self.expires_in_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if redirect_url is not UNSET:
            field_dict["redirect_url"] = redirect_url
        if state is not UNSET:
            field_dict["state"] = state
        if expires_in_minutes is not UNSET:
            field_dict["expires_in_minutes"] = expires_in_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = d.pop("provider")

        redirect_url = d.pop("redirect_url", UNSET)

        state = d.pop("state", UNSET)

        expires_in_minutes = d.pop("expires_in_minutes", UNSET)

        connect_link_create = cls(
            provider=provider,
            redirect_url=redirect_url,
            state=state,
            expires_in_minutes=expires_in_minutes,
        )

        connect_link_create.additional_properties = d
        return connect_link_create

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
