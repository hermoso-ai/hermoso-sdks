from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.transfer_object import TransferObject


T = TypeVar("T", bound="Transfer")


@_attrs_define
class Transfer:
    """
    Attributes:
        object_ (TransferObject | Unset):
        id (str | Unset):
        cents (int | Unset):
        currency (str | Unset):
        status (str | Unset):
        note (str | Unset):
    """

    object_: TransferObject | Unset = UNSET
    id: str | Unset = UNSET
    cents: int | Unset = UNSET
    currency: str | Unset = UNSET
    status: str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        cents = self.cents

        currency = self.currency

        status = self.status

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if cents is not UNSET:
            field_dict["cents"] = cents
        if currency is not UNSET:
            field_dict["currency"] = currency
        if status is not UNSET:
            field_dict["status"] = status
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: TransferObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = TransferObject(_object_)

        id = d.pop("id", UNSET)

        cents = d.pop("cents", UNSET)

        currency = d.pop("currency", UNSET)

        status = d.pop("status", UNSET)

        note = d.pop("note", UNSET)

        transfer = cls(
            object_=object_,
            id=id,
            cents=cents,
            currency=currency,
            status=status,
            note=note,
        )

        transfer.additional_properties = d
        return transfer

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
