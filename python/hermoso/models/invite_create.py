from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invite_create_disabled_areas_item import InviteCreateDisabledAreasItem
from ..models.invite_create_role import InviteCreateRole


T = TypeVar("T", bound="InviteCreate")


@_attrs_define
class InviteCreate:
    """
    Attributes:
        email (str):
        role (InviteCreateRole | Unset): Default member.
        disabled_areas (list[InviteCreateDisabledAreasItem] | Unset): Areas they may not use. Ignored for admin.
        send_email (bool | Unset): false = return invite_url instead of emailing it.
    """

    email: str
    role: InviteCreateRole | Unset = UNSET
    disabled_areas: list[InviteCreateDisabledAreasItem] | Unset = UNSET
    send_email: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        disabled_areas: list[str] | Unset = UNSET
        if not isinstance(self.disabled_areas, Unset):
            disabled_areas = []
            for disabled_areas_item_data in self.disabled_areas:
                disabled_areas_item = disabled_areas_item_data.value
                disabled_areas.append(disabled_areas_item)

        send_email = self.send_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if disabled_areas is not UNSET:
            field_dict["disabled_areas"] = disabled_areas
        if send_email is not UNSET:
            field_dict["send_email"] = send_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        _role = d.pop("role", UNSET)
        role: InviteCreateRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = InviteCreateRole(_role)

        _disabled_areas = d.pop("disabled_areas", UNSET)
        disabled_areas: list[InviteCreateDisabledAreasItem] | Unset = UNSET
        if _disabled_areas is not UNSET:
            disabled_areas = []
            for disabled_areas_item_data in _disabled_areas:
                disabled_areas_item = InviteCreateDisabledAreasItem(
                    disabled_areas_item_data
                )

                disabled_areas.append(disabled_areas_item)

        send_email = d.pop("send_email", UNSET)

        invite_create = cls(
            email=email,
            role=role,
            disabled_areas=disabled_areas,
            send_email=send_email,
        )

        invite_create.additional_properties = d
        return invite_create

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
