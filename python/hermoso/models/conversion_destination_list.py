from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conversion_destination_list_object import ConversionDestinationListObject

if TYPE_CHECKING:
    from ..models.conversion_destination_list_data_item import (
        ConversionDestinationListDataItem,
    )
    from ..models.conversion_destination_list_platforms_item import (
        ConversionDestinationListPlatformsItem,
    )


T = TypeVar("T", bound="ConversionDestinationList")


@_attrs_define
class ConversionDestinationList:
    """
    Attributes:
        object_ (ConversionDestinationListObject | Unset):
        data (list[ConversionDestinationListDataItem] | Unset):
        platforms (list[ConversionDestinationListPlatformsItem] | Unset):
        note (str | Unset):
    """

    object_: ConversionDestinationListObject | Unset = UNSET
    data: list[ConversionDestinationListDataItem] | Unset = UNSET
    platforms: list[ConversionDestinationListPlatformsItem] | Unset = UNSET
    note: str | Unset = UNSET
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

        platforms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.to_dict()
                platforms.append(platforms_item)

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if data is not UNSET:
            field_dict["data"] = data
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_destination_list_data_item import (
            ConversionDestinationListDataItem,
        )  # noqa: PLC0415
        from ..models.conversion_destination_list_platforms_item import (
            ConversionDestinationListPlatformsItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ConversionDestinationListObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ConversionDestinationListObject(_object_)

        _data = d.pop("data", UNSET)
        data: list[ConversionDestinationListDataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ConversionDestinationListDataItem.from_dict(data_item_data)

                data.append(data_item)

        _platforms = d.pop("platforms", UNSET)
        platforms: list[ConversionDestinationListPlatformsItem] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = ConversionDestinationListPlatformsItem.from_dict(
                    platforms_item_data
                )

                platforms.append(platforms_item)

        note = d.pop("note", UNSET)

        conversion_destination_list = cls(
            object_=object_,
            data=data,
            platforms=platforms,
            note=note,
        )

        conversion_destination_list.additional_properties = d
        return conversion_destination_list

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
