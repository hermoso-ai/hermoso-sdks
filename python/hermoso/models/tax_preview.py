from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tax_preview_object import TaxPreviewObject


T = TypeVar("T", bound="TaxPreview")


@_attrs_define
class TaxPreview:
    """
    Attributes:
        object_ (TaxPreviewObject | Unset):
        subtotal_usd (float | Unset):
        tax_usd (float | Unset):
        total_usd (float | Unset):
        currency (str | Unset):
        note (str | Unset):
    """

    object_: TaxPreviewObject | Unset = UNSET
    subtotal_usd: float | Unset = UNSET
    tax_usd: float | Unset = UNSET
    total_usd: float | Unset = UNSET
    currency: str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        subtotal_usd = self.subtotal_usd

        tax_usd = self.tax_usd

        total_usd = self.total_usd

        currency = self.currency

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if subtotal_usd is not UNSET:
            field_dict["subtotal_usd"] = subtotal_usd
        if tax_usd is not UNSET:
            field_dict["tax_usd"] = tax_usd
        if total_usd is not UNSET:
            field_dict["total_usd"] = total_usd
        if currency is not UNSET:
            field_dict["currency"] = currency
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: TaxPreviewObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = TaxPreviewObject(_object_)

        subtotal_usd = d.pop("subtotal_usd", UNSET)

        tax_usd = d.pop("tax_usd", UNSET)

        total_usd = d.pop("total_usd", UNSET)

        currency = d.pop("currency", UNSET)

        note = d.pop("note", UNSET)

        tax_preview = cls(
            object_=object_,
            subtotal_usd=subtotal_usd,
            tax_usd=tax_usd,
            total_usd=total_usd,
            currency=currency,
            note=note,
        )

        tax_preview.additional_properties = d
        return tax_preview

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
