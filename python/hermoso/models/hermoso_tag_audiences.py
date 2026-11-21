from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.hermoso_tag_audiences_object import HermosoTagAudiencesObject

if TYPE_CHECKING:
    from ..models.hermoso_tag_audiences_segment import HermosoTagAudiencesSegment
    from ..models.hermoso_tag_audiences_segments_item import (
        HermosoTagAudiencesSegmentsItem,
    )


T = TypeVar("T", bound="HermosoTagAudiences")


@_attrs_define
class HermosoTagAudiences:
    """
    Attributes:
        object_ (HermosoTagAudiencesObject | Unset):
        segments (list[HermosoTagAudiencesSegmentsItem] | Unset):
        segment (HermosoTagAudiencesSegment | Unset):
        sent (int | Unset):
        needs_confirm (bool | Unset):
        note (str | Unset):
    """

    object_: HermosoTagAudiencesObject | Unset = UNSET
    segments: list[HermosoTagAudiencesSegmentsItem] | Unset = UNSET
    segment: HermosoTagAudiencesSegment | Unset = UNSET
    sent: int | Unset = UNSET
    needs_confirm: bool | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        segments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()
                segments.append(segments_item)

        segment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.segment, Unset):
            segment = self.segment.to_dict()

        sent = self.sent

        needs_confirm = self.needs_confirm

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if segments is not UNSET:
            field_dict["segments"] = segments
        if segment is not UNSET:
            field_dict["segment"] = segment
        if sent is not UNSET:
            field_dict["sent"] = sent
        if needs_confirm is not UNSET:
            field_dict["needs_confirm"] = needs_confirm
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hermoso_tag_audiences_segment import HermosoTagAudiencesSegment  # noqa: PLC0415
        from ..models.hermoso_tag_audiences_segments_item import (
            HermosoTagAudiencesSegmentsItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: HermosoTagAudiencesObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = HermosoTagAudiencesObject(_object_)

        _segments = d.pop("segments", UNSET)
        segments: list[HermosoTagAudiencesSegmentsItem] | Unset = UNSET
        if _segments is not UNSET:
            segments = []
            for segments_item_data in _segments:
                segments_item = HermosoTagAudiencesSegmentsItem.from_dict(
                    segments_item_data
                )

                segments.append(segments_item)

        _segment = d.pop("segment", UNSET)
        segment: HermosoTagAudiencesSegment | Unset
        if isinstance(_segment, Unset):
            segment = UNSET
        else:
            segment = HermosoTagAudiencesSegment.from_dict(_segment)

        sent = d.pop("sent", UNSET)

        needs_confirm = d.pop("needs_confirm", UNSET)

        note = d.pop("note", UNSET)

        hermoso_tag_audiences = cls(
            object_=object_,
            segments=segments,
            segment=segment,
            sent=sent,
            needs_confirm=needs_confirm,
            note=note,
        )

        hermoso_tag_audiences.additional_properties = d
        return hermoso_tag_audiences

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
