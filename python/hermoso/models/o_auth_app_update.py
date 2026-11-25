from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="OAuthAppUpdate")


@_attrs_define
class OAuthAppUpdate:
    """
    Attributes:
        label (str | Unset):
        client_secret (str | Unset):
        config_id (str | Unset):
    """

    label: str | Unset = UNSET
    client_secret: str | Unset = UNSET
    config_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        client_secret = self.client_secret

        config_id = self.config_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if config_id is not UNSET:
            field_dict["config_id"] = config_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        config_id = d.pop("config_id", UNSET)

        o_auth_app_update = cls(
            label=label,
            client_secret=client_secret,
            config_id=config_id,
        )

        o_auth_app_update.additional_properties = d
        return o_auth_app_update

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
