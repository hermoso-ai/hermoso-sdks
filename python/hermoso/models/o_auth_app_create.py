from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="OAuthAppCreate")


@_attrs_define
class OAuthAppCreate:
    """
    Attributes:
        platform (str): facebook, instagram, google, tiktok, linkedin, x, pinterest, microsoft, … (GET
            /v1/connect/oauth-apps lists them)
        label (str):
        client_id (str):
        client_secret (str): Stored encrypted; never returned.
        config_id (str | Unset): Facebook app only: its WhatsApp Embedded Signup configuration id.
        confirm (bool | Unset):
    """

    platform: str
    label: str
    client_id: str
    client_secret: str
    config_id: str | Unset = UNSET
    confirm: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform

        label = self.label

        client_id = self.client_id

        client_secret = self.client_secret

        config_id = self.config_id

        confirm = self.confirm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "label": label,
                "client_id": client_id,
                "client_secret": client_secret,
            }
        )
        if config_id is not UNSET:
            field_dict["config_id"] = config_id
        if confirm is not UNSET:
            field_dict["confirm"] = confirm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform = d.pop("platform")

        label = d.pop("label")

        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        config_id = d.pop("config_id", UNSET)

        confirm = d.pop("confirm", UNSET)

        o_auth_app_create = cls(
            platform=platform,
            label=label,
            client_id=client_id,
            client_secret=client_secret,
            config_id=config_id,
            confirm=confirm,
        )

        o_auth_app_create.additional_properties = d
        return o_auth_app_create

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
