from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.credits_limits_type_0_brands_item_members_item import (
        CreditsLimitsType0BrandsItemMembersItem,
    )


T = TypeVar("T", bound="CreditsLimitsType0BrandsItem")


@_attrs_define
class CreditsLimitsType0BrandsItem:
    """
    Attributes:
        brand (str | Unset):
        name (None | str | Unset):
        limit (int | None | Unset):
        used (float | Unset):
        held (float | Unset): Credits held for work still running, which count against the limit.
        remaining (float | None | Unset):
        members (list[CreditsLimitsType0BrandsItemMembersItem] | Unset): Present for the owner and a brand admin (a
            member sees only their own row).
    """

    brand: str | Unset = UNSET
    name: None | str | Unset = UNSET
    limit: int | None | Unset = UNSET
    used: float | Unset = UNSET
    held: float | Unset = UNSET
    remaining: float | None | Unset = UNSET
    members: list[CreditsLimitsType0BrandsItemMembersItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand = self.brand

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        used = self.used

        held = self.held

        remaining: float | None | Unset
        if isinstance(self.remaining, Unset):
            remaining = UNSET
        else:
            remaining = self.remaining

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brand is not UNSET:
            field_dict["brand"] = brand
        if name is not UNSET:
            field_dict["name"] = name
        if limit is not UNSET:
            field_dict["limit"] = limit
        if used is not UNSET:
            field_dict["used"] = used
        if held is not UNSET:
            field_dict["held"] = held
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credits_limits_type_0_brands_item_members_item import (
            CreditsLimitsType0BrandsItemMembersItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        brand = d.pop("brand", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        used = d.pop("used", UNSET)

        held = d.pop("held", UNSET)

        def _parse_remaining(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        remaining = _parse_remaining(d.pop("remaining", UNSET))

        _members = d.pop("members", UNSET)
        members: list[CreditsLimitsType0BrandsItemMembersItem] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = CreditsLimitsType0BrandsItemMembersItem.from_dict(
                    members_item_data
                )

                members.append(members_item)

        credits_limits_type_0_brands_item = cls(
            brand=brand,
            name=name,
            limit=limit,
            used=used,
            held=held,
            remaining=remaining,
            members=members,
        )

        credits_limits_type_0_brands_item.additional_properties = d
        return credits_limits_type_0_brands_item

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
