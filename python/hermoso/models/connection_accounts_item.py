from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="ConnectionAccountsItem")


@_attrs_define
class ConnectionAccountsItem:
    """
    Attributes:
        id (str | Unset):
        label (None | str | Unset):
        handle (None | str | Unset):
    """

    id: str | Unset = UNSET
    label: None | str | Unset = UNSET
    handle: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        handle: None | str | Unset
        if isinstance(self.handle, Unset):
            handle = UNSET
        else:
            handle = self.handle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if handle is not UNSET:
            field_dict["handle"] = handle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_handle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        handle = _parse_handle(d.pop("handle", UNSET))

        connection_accounts_item = cls(
            id=id,
            label=label,
            handle=handle,
        )

        connection_accounts_item.additional_properties = d
        return connection_accounts_item

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
