from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.media_object import MediaObject
from typing import cast


T = TypeVar("T", bound="Media")


@_attrs_define
class Media:
    """
    Attributes:
        object_ (MediaObject | Unset):
        url (str | Unset): A durable Hermoso-hosted URL. Pass it straight into POST /v1/posts.
        type_ (str | Unset): image | video | audio | document.
        bytes_ (int | Unset):
        name (None | str | Unset):
    """

    object_: MediaObject | Unset = UNSET
    url: str | Unset = UNSET
    type_: str | Unset = UNSET
    bytes_: int | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        url = self.url

        type_ = self.type_

        bytes_ = self.bytes_

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if url is not UNSET:
            field_dict["url"] = url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: MediaObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = MediaObject(_object_)

        url = d.pop("url", UNSET)

        type_ = d.pop("type", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        media = cls(
            object_=object_,
            url=url,
            type_=type_,
            bytes_=bytes_,
            name=name,
        )

        media.additional_properties = d
        return media

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
