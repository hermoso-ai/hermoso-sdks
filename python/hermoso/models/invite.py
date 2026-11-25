from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invite_object import InviteObject
from typing import cast


T = TypeVar("T", bound="Invite")


@_attrs_define
class Invite:
    """
    Attributes:
        object_ (InviteObject | Unset):
        email (str | Unset):
        invited (bool | Unset):
        already_member (bool | Unset):
        emailed (bool | Unset):
        invite_url (None | str | Unset):
        role (str | Unset):
        disabled_areas (list[str] | Unset):
        expires_in_days (int | Unset):
        message (str | Unset):
    """

    object_: InviteObject | Unset = UNSET
    email: str | Unset = UNSET
    invited: bool | Unset = UNSET
    already_member: bool | Unset = UNSET
    emailed: bool | Unset = UNSET
    invite_url: None | str | Unset = UNSET
    role: str | Unset = UNSET
    disabled_areas: list[str] | Unset = UNSET
    expires_in_days: int | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        email = self.email

        invited = self.invited

        already_member = self.already_member

        emailed = self.emailed

        invite_url: None | str | Unset
        if isinstance(self.invite_url, Unset):
            invite_url = UNSET
        else:
            invite_url = self.invite_url

        role = self.role

        disabled_areas: list[str] | Unset = UNSET
        if not isinstance(self.disabled_areas, Unset):
            disabled_areas = self.disabled_areas

        expires_in_days = self.expires_in_days

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if email is not UNSET:
            field_dict["email"] = email
        if invited is not UNSET:
            field_dict["invited"] = invited
        if already_member is not UNSET:
            field_dict["already_member"] = already_member
        if emailed is not UNSET:
            field_dict["emailed"] = emailed
        if invite_url is not UNSET:
            field_dict["invite_url"] = invite_url
        if role is not UNSET:
            field_dict["role"] = role
        if disabled_areas is not UNSET:
            field_dict["disabled_areas"] = disabled_areas
        if expires_in_days is not UNSET:
            field_dict["expires_in_days"] = expires_in_days
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: InviteObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = InviteObject(_object_)

        email = d.pop("email", UNSET)

        invited = d.pop("invited", UNSET)

        already_member = d.pop("already_member", UNSET)

        emailed = d.pop("emailed", UNSET)

        def _parse_invite_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invite_url = _parse_invite_url(d.pop("invite_url", UNSET))

        role = d.pop("role", UNSET)

        disabled_areas = cast(list[str], d.pop("disabled_areas", UNSET))

        expires_in_days = d.pop("expires_in_days", UNSET)

        message = d.pop("message", UNSET)

        invite = cls(
            object_=object_,
            email=email,
            invited=invited,
            already_member=already_member,
            emailed=emailed,
            invite_url=invite_url,
            role=role,
            disabled_areas=disabled_areas,
            expires_in_days=expires_in_days,
            message=message,
        )

        invite.additional_properties = d
        return invite

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
