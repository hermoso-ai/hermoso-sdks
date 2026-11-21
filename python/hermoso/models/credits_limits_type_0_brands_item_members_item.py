from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="CreditsLimitsType0BrandsItemMembersItem")


@_attrs_define
class CreditsLimitsType0BrandsItemMembersItem:
    """
    Attributes:
        email (str | Unset):
        role (None | str | Unset):
        limit (int | None | Unset):
        used (float | Unset):
        remaining (float | None | Unset):
    """

    email: str | Unset = UNSET
    role: None | str | Unset = UNSET
    limit: int | None | Unset = UNSET
    used: float | Unset = UNSET
    remaining: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        used = self.used

        remaining: float | None | Unset
        if isinstance(self.remaining, Unset):
            remaining = UNSET
        else:
            remaining = self.remaining

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if role is not UNSET:
            field_dict["role"] = role
        if limit is not UNSET:
            field_dict["limit"] = limit
        if used is not UNSET:
            field_dict["used"] = used
        if remaining is not UNSET:
            field_dict["remaining"] = remaining

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        used = d.pop("used", UNSET)

        def _parse_remaining(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        remaining = _parse_remaining(d.pop("remaining", UNSET))

        credits_limits_type_0_brands_item_members_item = cls(
            email=email,
            role=role,
            limit=limit,
            used=used,
            remaining=remaining,
        )

        credits_limits_type_0_brands_item_members_item.additional_properties = d
        return credits_limits_type_0_brands_item_members_item

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
