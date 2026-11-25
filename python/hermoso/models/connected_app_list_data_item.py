from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="ConnectedAppListDataItem")


@_attrs_define
class ConnectedAppListDataItem:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        host (None | str | Unset):
        authorized_at (None | str | Unset):
        last_used_at (None | str | Unset):
        token_count (int | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    host: None | str | Unset = UNSET
    authorized_at: None | str | Unset = UNSET
    last_used_at: None | str | Unset = UNSET
    token_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        host: None | str | Unset
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        authorized_at: None | str | Unset
        if isinstance(self.authorized_at, Unset):
            authorized_at = UNSET
        else:
            authorized_at = self.authorized_at

        last_used_at: None | str | Unset
        if isinstance(self.last_used_at, Unset):
            last_used_at = UNSET
        else:
            last_used_at = self.last_used_at

        token_count = self.token_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if host is not UNSET:
            field_dict["host"] = host
        if authorized_at is not UNSET:
            field_dict["authorized_at"] = authorized_at
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if token_count is not UNSET:
            field_dict["token_count"] = token_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_authorized_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authorized_at = _parse_authorized_at(d.pop("authorized_at", UNSET))

        def _parse_last_used_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at", UNSET))

        token_count = d.pop("token_count", UNSET)

        connected_app_list_data_item = cls(
            id=id,
            name=name,
            host=host,
            authorized_at=authorized_at,
            last_used_at=last_used_at,
            token_count=token_count,
        )

        connected_app_list_data_item.additional_properties = d
        return connected_app_list_data_item

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
