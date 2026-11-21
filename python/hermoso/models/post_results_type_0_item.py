from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.post_results_type_0_item_first_comment import (
        PostResultsType0ItemFirstComment,
    )


T = TypeVar("T", bound="PostResultsType0Item")


@_attrs_define
class PostResultsType0Item:
    """
    Attributes:
        channel (str | Unset):
        ok (bool | Unset):
        url (None | str | Unset):
        id (None | str | Unset):
        error (None | str | Unset):
        first_comment (PostResultsType0ItemFirstComment | Unset): Present when the post carried `first_comment`.
            `posted` true with the comment `id`, or false with `note` saying why (`skipped` when the channel takes no first
            comment, or it was already posted by an earlier run). A failed comment never fails the channel.
    """

    channel: str | Unset = UNSET
    ok: bool | Unset = UNSET
    url: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    first_comment: PostResultsType0ItemFirstComment | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        ok = self.ok

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        first_comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_comment, Unset):
            first_comment = self.first_comment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if ok is not UNSET:
            field_dict["ok"] = ok
        if url is not UNSET:
            field_dict["url"] = url
        if id is not UNSET:
            field_dict["id"] = id
        if error is not UNSET:
            field_dict["error"] = error
        if first_comment is not UNSET:
            field_dict["first_comment"] = first_comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_results_type_0_item_first_comment import (
            PostResultsType0ItemFirstComment,
        )  # noqa: PLC0415

        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        ok = d.pop("ok", UNSET)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        _first_comment = d.pop("first_comment", UNSET)
        first_comment: PostResultsType0ItemFirstComment | Unset
        if isinstance(_first_comment, Unset):
            first_comment = UNSET
        else:
            first_comment = PostResultsType0ItemFirstComment.from_dict(_first_comment)

        post_results_type_0_item = cls(
            channel=channel,
            ok=ok,
            url=url,
            id=id,
            error=error,
            first_comment=first_comment,
        )

        post_results_type_0_item.additional_properties = d
        return post_results_type_0_item

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
