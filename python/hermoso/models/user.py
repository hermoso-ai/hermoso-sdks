from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.user_object import UserObject
from ..models.user_role import UserRole
from typing import cast


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        object_ (UserObject | Unset):
        email (None | str | Unset):
        role (UserRole | Unset):
        role_label (str | Unset):
        disabled_areas (list[str] | Unset):
        access (str | Unset):
        status (str | Unset):
        accepted (bool | Unset):
        is_you (bool | Unset):
    """

    object_: UserObject | Unset = UNSET
    email: None | str | Unset = UNSET
    role: UserRole | Unset = UNSET
    role_label: str | Unset = UNSET
    disabled_areas: list[str] | Unset = UNSET
    access: str | Unset = UNSET
    status: str | Unset = UNSET
    accepted: bool | Unset = UNSET
    is_you: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        role_label = self.role_label

        disabled_areas: list[str] | Unset = UNSET
        if not isinstance(self.disabled_areas, Unset):
            disabled_areas = self.disabled_areas

        access = self.access

        status = self.status

        accepted = self.accepted

        is_you = self.is_you

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if email is not UNSET:
            field_dict["email"] = email
        if role is not UNSET:
            field_dict["role"] = role
        if role_label is not UNSET:
            field_dict["role_label"] = role_label
        if disabled_areas is not UNSET:
            field_dict["disabled_areas"] = disabled_areas
        if access is not UNSET:
            field_dict["access"] = access
        if status is not UNSET:
            field_dict["status"] = status
        if accepted is not UNSET:
            field_dict["accepted"] = accepted
        if is_you is not UNSET:
            field_dict["is_you"] = is_you

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: UserObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = UserObject(_object_)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        _role = d.pop("role", UNSET)
        role: UserRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = UserRole(_role)

        role_label = d.pop("role_label", UNSET)

        disabled_areas = cast(list[str], d.pop("disabled_areas", UNSET))

        access = d.pop("access", UNSET)

        status = d.pop("status", UNSET)

        accepted = d.pop("accepted", UNSET)

        is_you = d.pop("is_you", UNSET)

        user = cls(
            object_=object_,
            email=email,
            role=role,
            role_label=role_label,
            disabled_areas=disabled_areas,
            access=access,
            status=status,
            accepted=accepted,
            is_you=is_you,
        )

        user.additional_properties = d
        return user

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
