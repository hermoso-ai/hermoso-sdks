from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="ContactEmail")


@_attrs_define
class ContactEmail:
    """
    Attributes:
        address (None | str | Unset):
        verified (bool | Unset):
        verified_at (None | str | Unset): ISO-8601, or null while unverified.
        note (str | Unset): What the state means, in one sentence.
    """

    address: None | str | Unset = UNSET
    verified: bool | Unset = UNSET
    verified_at: None | str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        verified = self.verified

        verified_at: None | str | Unset
        if isinstance(self.verified_at, Unset):
            verified_at = UNSET
        else:
            verified_at = self.verified_at

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if verified is not UNSET:
            field_dict["verified"] = verified
        if verified_at is not UNSET:
            field_dict["verified_at"] = verified_at
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        verified = d.pop("verified", UNSET)

        def _parse_verified_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        verified_at = _parse_verified_at(d.pop("verified_at", UNSET))

        note = d.pop("note", UNSET)

        contact_email = cls(
            address=address,
            verified=verified,
            verified_at=verified_at,
            note=note,
        )

        contact_email.additional_properties = d
        return contact_email

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
