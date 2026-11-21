from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


from ..models.clone_quote_request_type import CloneQuoteRequestType


T = TypeVar("T", bound="CloneQuoteRequest")


@_attrs_define
class CloneQuoteRequest:
    """
    Attributes:
        type_ (CloneQuoteRequestType): image = a static ad image to clone; video = a TikTok, Reel, Facebook, X or
            YouTube link (or a direct video file). This enum MAY GROW.
        url (str): The https URL of the ad image (image) or of the post or video file (video).
    """

    type_: CloneQuoteRequestType
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = CloneQuoteRequestType(d.pop("type"))

        url = d.pop("url")

        clone_quote_request = cls(
            type_=type_,
            url=url,
        )

        clone_quote_request.additional_properties = d
        return clone_quote_request

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
