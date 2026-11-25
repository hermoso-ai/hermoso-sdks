from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connected_app_revocation_object import ConnectedAppRevocationObject


T = TypeVar("T", bound="ConnectedAppRevocation")


@_attrs_define
class ConnectedAppRevocation:
    """
    Attributes:
        object_ (ConnectedAppRevocationObject | Unset):
        id (str | Unset):
        revoked (bool | Unset):
        tokens_revoked (int | Unset):
        message (str | Unset):
    """

    object_: ConnectedAppRevocationObject | Unset = UNSET
    id: str | Unset = UNSET
    revoked: bool | Unset = UNSET
    tokens_revoked: int | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        revoked = self.revoked

        tokens_revoked = self.tokens_revoked

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if revoked is not UNSET:
            field_dict["revoked"] = revoked
        if tokens_revoked is not UNSET:
            field_dict["tokens_revoked"] = tokens_revoked
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ConnectedAppRevocationObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ConnectedAppRevocationObject(_object_)

        id = d.pop("id", UNSET)

        revoked = d.pop("revoked", UNSET)

        tokens_revoked = d.pop("tokens_revoked", UNSET)

        message = d.pop("message", UNSET)

        connected_app_revocation = cls(
            object_=object_,
            id=id,
            revoked=revoked,
            tokens_revoked=tokens_revoked,
            message=message,
        )

        connected_app_revocation.additional_properties = d
        return connected_app_revocation

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
