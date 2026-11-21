from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connect_redirects_object import ConnectRedirectsObject
from typing import cast


T = TypeVar("T", bound="ConnectRedirects")


@_attrs_define
class ConnectRedirects:
    """
    Attributes:
        object_ (ConnectRedirectsObject | Unset):
        urls (list[str] | Unset):
    """

    object_: ConnectRedirectsObject | Unset = UNSET
    urls: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        urls: list[str] | Unset = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if urls is not UNSET:
            field_dict["urls"] = urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ConnectRedirectsObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ConnectRedirectsObject(_object_)

        urls = cast(list[str], d.pop("urls", UNSET))

        connect_redirects = cls(
            object_=object_,
            urls=urls,
        )

        connect_redirects.additional_properties = d
        return connect_redirects

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
