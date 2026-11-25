from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="TrackingWindowOpen")


@_attrs_define
class TrackingWindowOpen:
    """
    Attributes:
        post_id (str | Unset): A post the brand published: record id, platform post id or link.
        url (str | Unset): A link to any public post.
        tracking_days (int | Unset): 1-90. Default 30.
        confirm (bool | Unset): Required for a url window, once the person accepted the quote.
    """

    post_id: str | Unset = UNSET
    url: str | Unset = UNSET
    tracking_days: int | Unset = UNSET
    confirm: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post_id = self.post_id

        url = self.url

        tracking_days = self.tracking_days

        confirm = self.confirm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if url is not UNSET:
            field_dict["url"] = url
        if tracking_days is not UNSET:
            field_dict["tracking_days"] = tracking_days
        if confirm is not UNSET:
            field_dict["confirm"] = confirm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        post_id = d.pop("post_id", UNSET)

        url = d.pop("url", UNSET)

        tracking_days = d.pop("tracking_days", UNSET)

        confirm = d.pop("confirm", UNSET)

        tracking_window_open = cls(
            post_id=post_id,
            url=url,
            tracking_days=tracking_days,
            confirm=confirm,
        )

        tracking_window_open.additional_properties = d
        return tracking_window_open

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
