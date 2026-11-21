from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.channel_list_object import ChannelListObject

if TYPE_CHECKING:
    from ..models.channel import Channel


T = TypeVar("T", bound="ChannelList")


@_attrs_define
class ChannelList:
    """
    Attributes:
        object_ (ChannelListObject | Unset):
        data (list[Channel] | Unset):
    """

    object_: ChannelListObject | Unset = UNSET
    data: list[Channel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel import Channel  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ChannelListObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ChannelListObject(_object_)

        _data = d.pop("data", UNSET)
        data: list[Channel] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = Channel.from_dict(data_item_data)

                data.append(data_item)

        channel_list = cls(
            object_=object_,
            data=data,
        )

        channel_list.additional_properties = d
        return channel_list

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
