from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.credits_limits_type_0_timezone import CreditsLimitsType0Timezone

if TYPE_CHECKING:
    from ..models.credits_limits_type_0_brands_item import CreditsLimitsType0BrandsItem


T = TypeVar("T", bound="CreditsLimitsType0")


@_attrs_define
class CreditsLimitsType0:
    """The monthly credit limits on the brand this key acts on (or the brand named by `?brand=`). The account owner can cap
    what a brand, or one member of a shared brand, spends in a UTC calendar month; when one would be passed, paid calls
    answer `429` with `error.code` `credit_limit` (and `Retry-After` until the reset). `limit: null` means no limit.
    Null here (with `limits_error`) means the read failed, never that there are no limits.

        Attributes:
            month (str | Unset): The UTC calendar month the usage covers, `YYYY-MM`.
            reset_at (str | Unset): When every limit’s month resets (00:00 UTC on the 1st).
            timezone (CreditsLimitsType0Timezone | Unset):
            can_edit (bool | Unset): True only for the account owner. Set a limit with the `set_credit_limit` tool (`POST
                /v1/tools/set_credit_limit`).
            brands (list[CreditsLimitsType0BrandsItem] | Unset):
    """

    month: str | Unset = UNSET
    reset_at: str | Unset = UNSET
    timezone: CreditsLimitsType0Timezone | Unset = UNSET
    can_edit: bool | Unset = UNSET
    brands: list[CreditsLimitsType0BrandsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        reset_at = self.reset_at

        timezone: str | Unset = UNSET
        if not isinstance(self.timezone, Unset):
            timezone = self.timezone.value

        can_edit = self.can_edit

        brands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.brands, Unset):
            brands = []
            for brands_item_data in self.brands:
                brands_item = brands_item_data.to_dict()
                brands.append(brands_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if month is not UNSET:
            field_dict["month"] = month
        if reset_at is not UNSET:
            field_dict["reset_at"] = reset_at
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if can_edit is not UNSET:
            field_dict["can_edit"] = can_edit
        if brands is not UNSET:
            field_dict["brands"] = brands

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credits_limits_type_0_brands_item import (
            CreditsLimitsType0BrandsItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        month = d.pop("month", UNSET)

        reset_at = d.pop("reset_at", UNSET)

        _timezone = d.pop("timezone", UNSET)
        timezone: CreditsLimitsType0Timezone | Unset
        if isinstance(_timezone, Unset):
            timezone = UNSET
        else:
            timezone = CreditsLimitsType0Timezone(_timezone)

        can_edit = d.pop("can_edit", UNSET)

        _brands = d.pop("brands", UNSET)
        brands: list[CreditsLimitsType0BrandsItem] | Unset = UNSET
        if _brands is not UNSET:
            brands = []
            for brands_item_data in _brands:
                brands_item = CreditsLimitsType0BrandsItem.from_dict(brands_item_data)

                brands.append(brands_item)

        credits_limits_type_0 = cls(
            month=month,
            reset_at=reset_at,
            timezone=timezone,
            can_edit=can_edit,
            brands=brands,
        )

        credits_limits_type_0.additional_properties = d
        return credits_limits_type_0

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
