from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.hermoso_tag_events_sent_object import HermosoTagEventsSentObject

if TYPE_CHECKING:
    from ..models.hermoso_tag_events_sent_refused_item import (
        HermosoTagEventsSentRefusedItem,
    )


T = TypeVar("T", bound="HermosoTagEventsSent")


@_attrs_define
class HermosoTagEventsSent:
    """
    Attributes:
        object_ (HermosoTagEventsSentObject | Unset):
        accepted (int | Unset):
        refused (list[HermosoTagEventsSentRefusedItem] | Unset):
        note (str | Unset):
    """

    object_: HermosoTagEventsSentObject | Unset = UNSET
    accepted: int | Unset = UNSET
    refused: list[HermosoTagEventsSentRefusedItem] | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        accepted = self.accepted

        refused: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.refused, Unset):
            refused = []
            for refused_item_data in self.refused:
                refused_item = refused_item_data.to_dict()
                refused.append(refused_item)

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if accepted is not UNSET:
            field_dict["accepted"] = accepted
        if refused is not UNSET:
            field_dict["refused"] = refused
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hermoso_tag_events_sent_refused_item import (
            HermosoTagEventsSentRefusedItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: HermosoTagEventsSentObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = HermosoTagEventsSentObject(_object_)

        accepted = d.pop("accepted", UNSET)

        _refused = d.pop("refused", UNSET)
        refused: list[HermosoTagEventsSentRefusedItem] | Unset = UNSET
        if _refused is not UNSET:
            refused = []
            for refused_item_data in _refused:
                refused_item = HermosoTagEventsSentRefusedItem.from_dict(
                    refused_item_data
                )

                refused.append(refused_item)

        note = d.pop("note", UNSET)

        hermoso_tag_events_sent = cls(
            object_=object_,
            accepted=accepted,
            refused=refused,
            note=note,
        )

        hermoso_tag_events_sent.additional_properties = d
        return hermoso_tag_events_sent

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
