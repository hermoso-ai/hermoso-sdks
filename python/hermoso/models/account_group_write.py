from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.account_group_write_members_item import AccountGroupWriteMembersItem


T = TypeVar("T", bound="AccountGroupWrite")


@_attrs_define
class AccountGroupWrite:
    """
    Attributes:
        name (str | Unset):
        members (list[AccountGroupWriteMembersItem] | Unset):
    """

    name: str | Unset = UNSET
    members: list[AccountGroupWriteMembersItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_group_write_members_item import (
            AccountGroupWriteMembersItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _members = d.pop("members", UNSET)
        members: list[AccountGroupWriteMembersItem] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = AccountGroupWriteMembersItem.from_dict(members_item_data)

                members.append(members_item)

        account_group_write = cls(
            name=name,
            members=members,
        )

        account_group_write.additional_properties = d
        return account_group_write

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
