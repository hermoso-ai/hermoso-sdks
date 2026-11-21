from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.best_time_object import BestTimeObject

if TYPE_CHECKING:
    from ..models.best_time_channels_item import BestTimeChannelsItem
    from ..models.best_time_overall import BestTimeOverall
    from ..models.best_time_slots_item import BestTimeSlotsItem


T = TypeVar("T", bound="BestTime")


@_attrs_define
class BestTime:
    """
    Attributes:
        object_ (BestTimeObject | Unset):
        zone (str | Unset):
        days (int | Unset):
        slots (list[BestTimeSlotsItem] | Unset):
        overall (BestTimeOverall | Unset):
        channels (list[BestTimeChannelsItem] | Unset):
        text (str | Unset):
    """

    object_: BestTimeObject | Unset = UNSET
    zone: str | Unset = UNSET
    days: int | Unset = UNSET
    slots: list[BestTimeSlotsItem] | Unset = UNSET
    overall: BestTimeOverall | Unset = UNSET
    channels: list[BestTimeChannelsItem] | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        zone = self.zone

        days = self.days

        slots: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.slots, Unset):
            slots = []
            for slots_item_data in self.slots:
                slots_item = slots_item_data.to_dict()
                slots.append(slots_item)

        overall: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overall, Unset):
            overall = self.overall.to_dict()

        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if zone is not UNSET:
            field_dict["zone"] = zone
        if days is not UNSET:
            field_dict["days"] = days
        if slots is not UNSET:
            field_dict["slots"] = slots
        if overall is not UNSET:
            field_dict["overall"] = overall
        if channels is not UNSET:
            field_dict["channels"] = channels
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.best_time_channels_item import BestTimeChannelsItem  # noqa: PLC0415
        from ..models.best_time_overall import BestTimeOverall  # noqa: PLC0415
        from ..models.best_time_slots_item import BestTimeSlotsItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: BestTimeObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = BestTimeObject(_object_)

        zone = d.pop("zone", UNSET)

        days = d.pop("days", UNSET)

        _slots = d.pop("slots", UNSET)
        slots: list[BestTimeSlotsItem] | Unset = UNSET
        if _slots is not UNSET:
            slots = []
            for slots_item_data in _slots:
                slots_item = BestTimeSlotsItem.from_dict(slots_item_data)

                slots.append(slots_item)

        _overall = d.pop("overall", UNSET)
        overall: BestTimeOverall | Unset
        if isinstance(_overall, Unset):
            overall = UNSET
        else:
            overall = BestTimeOverall.from_dict(_overall)

        _channels = d.pop("channels", UNSET)
        channels: list[BestTimeChannelsItem] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = BestTimeChannelsItem.from_dict(channels_item_data)

                channels.append(channels_item)

        text = d.pop("text", UNSET)

        best_time = cls(
            object_=object_,
            zone=zone,
            days=days,
            slots=slots,
            overall=overall,
            channels=channels,
            text=text,
        )

        best_time.additional_properties = d
        return best_time

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
