from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="EditPreviewType0")


@_attrs_define
class EditPreviewType0:
    """
    Attributes:
        still_url (None | str | Unset): The edited still (null on a dry run). Send it back as `preview_still`.
        still_credits (float | None | Unset): What the still cost, or on a dry run what it reserves.
        still_refused (None | str | Unset):
        frame_at (float | None | Unset): The second of the clip the still was taken from.
        note (None | str | Unset):
    """

    still_url: None | str | Unset = UNSET
    still_credits: float | None | Unset = UNSET
    still_refused: None | str | Unset = UNSET
    frame_at: float | None | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        still_url: None | str | Unset
        if isinstance(self.still_url, Unset):
            still_url = UNSET
        else:
            still_url = self.still_url

        still_credits: float | None | Unset
        if isinstance(self.still_credits, Unset):
            still_credits = UNSET
        else:
            still_credits = self.still_credits

        still_refused: None | str | Unset
        if isinstance(self.still_refused, Unset):
            still_refused = UNSET
        else:
            still_refused = self.still_refused

        frame_at: float | None | Unset
        if isinstance(self.frame_at, Unset):
            frame_at = UNSET
        else:
            frame_at = self.frame_at

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if still_url is not UNSET:
            field_dict["still_url"] = still_url
        if still_credits is not UNSET:
            field_dict["still_credits"] = still_credits
        if still_refused is not UNSET:
            field_dict["still_refused"] = still_refused
        if frame_at is not UNSET:
            field_dict["frame_at"] = frame_at
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_still_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        still_url = _parse_still_url(d.pop("still_url", UNSET))

        def _parse_still_credits(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        still_credits = _parse_still_credits(d.pop("still_credits", UNSET))

        def _parse_still_refused(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        still_refused = _parse_still_refused(d.pop("still_refused", UNSET))

        def _parse_frame_at(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        frame_at = _parse_frame_at(d.pop("frame_at", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        edit_preview_type_0 = cls(
            still_url=still_url,
            still_credits=still_credits,
            still_refused=still_refused,
            frame_at=frame_at,
            note=note,
        )

        edit_preview_type_0.additional_properties = d
        return edit_preview_type_0

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
