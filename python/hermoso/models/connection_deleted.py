from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connection_deleted_object import ConnectionDeletedObject
from typing import cast


T = TypeVar("T", bound="ConnectionDeleted")


@_attrs_define
class ConnectionDeleted:
    """
    Attributes:
        object_ (ConnectionDeletedObject | Unset):
        provider (str | Unset):
        deleted (bool | Unset):
        account (None | str | Unset):
        note (str | Unset):
    """

    object_: ConnectionDeletedObject | Unset = UNSET
    provider: str | Unset = UNSET
    deleted: bool | Unset = UNSET
    account: None | str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        provider = self.provider

        deleted = self.deleted

        account: None | str | Unset
        if isinstance(self.account, Unset):
            account = UNSET
        else:
            account = self.account

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if provider is not UNSET:
            field_dict["provider"] = provider
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if account is not UNSET:
            field_dict["account"] = account
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ConnectionDeletedObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ConnectionDeletedObject(_object_)

        provider = d.pop("provider", UNSET)

        deleted = d.pop("deleted", UNSET)

        def _parse_account(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account = _parse_account(d.pop("account", UNSET))

        note = d.pop("note", UNSET)

        connection_deleted = cls(
            object_=object_,
            provider=provider,
            deleted=deleted,
            account=account,
            note=note,
        )

        connection_deleted.additional_properties = d
        return connection_deleted

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
