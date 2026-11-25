from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.user_removal_object import UserRemovalObject

if TYPE_CHECKING:
    from ..models.user_removal_connections_disconnected_item import (
        UserRemovalConnectionsDisconnectedItem,
    )


T = TypeVar("T", bound="UserRemoval")


@_attrs_define
class UserRemoval:
    """
    Attributes:
        object_ (UserRemovalObject | Unset):
        email (str | Unset):
        removed (bool | Unset):
        connections_disconnected (list[UserRemovalConnectionsDisconnectedItem] | Unset):
        scheduled_posts_not_going_out (int | Unset):
        message (str | Unset):
    """

    object_: UserRemovalObject | Unset = UNSET
    email: str | Unset = UNSET
    removed: bool | Unset = UNSET
    connections_disconnected: list[UserRemovalConnectionsDisconnectedItem] | Unset = (
        UNSET
    )
    scheduled_posts_not_going_out: int | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        email = self.email

        removed = self.removed

        connections_disconnected: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connections_disconnected, Unset):
            connections_disconnected = []
            for connections_disconnected_item_data in self.connections_disconnected:
                connections_disconnected_item = (
                    connections_disconnected_item_data.to_dict()
                )
                connections_disconnected.append(connections_disconnected_item)

        scheduled_posts_not_going_out = self.scheduled_posts_not_going_out

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if email is not UNSET:
            field_dict["email"] = email
        if removed is not UNSET:
            field_dict["removed"] = removed
        if connections_disconnected is not UNSET:
            field_dict["connections_disconnected"] = connections_disconnected
        if scheduled_posts_not_going_out is not UNSET:
            field_dict["scheduled_posts_not_going_out"] = scheduled_posts_not_going_out
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_removal_connections_disconnected_item import (
            UserRemovalConnectionsDisconnectedItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: UserRemovalObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = UserRemovalObject(_object_)

        email = d.pop("email", UNSET)

        removed = d.pop("removed", UNSET)

        _connections_disconnected = d.pop("connections_disconnected", UNSET)
        connections_disconnected: (
            list[UserRemovalConnectionsDisconnectedItem] | Unset
        ) = UNSET
        if _connections_disconnected is not UNSET:
            connections_disconnected = []
            for connections_disconnected_item_data in _connections_disconnected:
                connections_disconnected_item = (
                    UserRemovalConnectionsDisconnectedItem.from_dict(
                        connections_disconnected_item_data
                    )
                )

                connections_disconnected.append(connections_disconnected_item)

        scheduled_posts_not_going_out = d.pop("scheduled_posts_not_going_out", UNSET)

        message = d.pop("message", UNSET)

        user_removal = cls(
            object_=object_,
            email=email,
            removed=removed,
            connections_disconnected=connections_disconnected,
            scheduled_posts_not_going_out=scheduled_posts_not_going_out,
            message=message,
        )

        user_removal.additional_properties = d
        return user_removal

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
