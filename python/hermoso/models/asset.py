from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.asset_object import AssetObject
from typing import cast


T = TypeVar("T", bound="Asset")


@_attrs_define
class Asset:
    """
    Attributes:
        object_ (AssetObject | Unset):
        url (str | Unset): The durable public file.
        type_ (str | Unset): image or video. This set MAY GROW.
        poster_url (None | str | Unset): A still for a video.
        model (None | str | Unset):
        created_at (None | str | Unset): ISO-8601, when known.
    """

    object_: AssetObject | Unset = UNSET
    url: str | Unset = UNSET
    type_: str | Unset = UNSET
    poster_url: None | str | Unset = UNSET
    model: None | str | Unset = UNSET
    created_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        url = self.url

        type_ = self.type_

        poster_url: None | str | Unset
        if isinstance(self.poster_url, Unset):
            poster_url = UNSET
        else:
            poster_url = self.poster_url

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if url is not UNSET:
            field_dict["url"] = url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if poster_url is not UNSET:
            field_dict["poster_url"] = poster_url
        if model is not UNSET:
            field_dict["model"] = model
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: AssetObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = AssetObject(_object_)

        url = d.pop("url", UNSET)

        type_ = d.pop("type", UNSET)

        def _parse_poster_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        poster_url = _parse_poster_url(d.pop("poster_url", UNSET))

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        asset = cls(
            object_=object_,
            url=url,
            type_=type_,
            poster_url=poster_url,
            model=model,
            created_at=created_at,
        )

        asset.additional_properties = d
        return asset

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
