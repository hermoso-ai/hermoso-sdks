from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="PostResultsType0ItemFirstComment")


@_attrs_define
class PostResultsType0ItemFirstComment:
    """Present when the post carried `first_comment`. `posted` true with the comment `id`, or false with `note` saying why
    (`skipped` when the channel takes no first comment, or it was already posted by an earlier run). A failed comment
    never fails the channel.

        Attributes:
            posted (bool | Unset):
            id (None | str | Unset):
            skipped (bool | Unset):
            note (None | str | Unset):
    """

    posted: bool | Unset = UNSET
    id: None | str | Unset = UNSET
    skipped: bool | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        posted = self.posted

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        skipped = self.skipped

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posted is not UNSET:
            field_dict["posted"] = posted
        if id is not UNSET:
            field_dict["id"] = id
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        posted = d.pop("posted", UNSET)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        skipped = d.pop("skipped", UNSET)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        post_results_type_0_item_first_comment = cls(
            posted=posted,
            id=id,
            skipped=skipped,
            note=note,
        )

        post_results_type_0_item_first_comment.additional_properties = d
        return post_results_type_0_item_first_comment

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
