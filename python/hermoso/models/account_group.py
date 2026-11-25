from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_group_object import AccountGroupObject

if TYPE_CHECKING:
    from ..models.account_group_members_item import AccountGroupMembersItem


T = TypeVar("T", bound="AccountGroup")


@_attrs_define
class AccountGroup:
    """
    Attributes:
        object_ (AccountGroupObject | Unset):
        id (str | Unset):
        name (str | Unset):
        members (list[AccountGroupMembersItem] | Unset):
        deleted (bool | Unset):
    """

    object_: AccountGroupObject | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    members: list[AccountGroupMembersItem] | Unset = UNSET
    deleted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        name = self.name

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if members is not UNSET:
            field_dict["members"] = members
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_group_members_item import AccountGroupMembersItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: AccountGroupObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = AccountGroupObject(_object_)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _members = d.pop("members", UNSET)
        members: list[AccountGroupMembersItem] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = AccountGroupMembersItem.from_dict(members_item_data)

                members.append(members_item)

        deleted = d.pop("deleted", UNSET)

        account_group = cls(
            object_=object_,
            id=id,
            name=name,
            members=members,
            deleted=deleted,
        )

        account_group.additional_properties = d
        return account_group

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
