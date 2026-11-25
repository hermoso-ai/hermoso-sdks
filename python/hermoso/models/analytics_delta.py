from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.analytics_delta_object import AnalyticsDeltaObject

if TYPE_CHECKING:
    from ..models.analytics_delta_data_item import AnalyticsDeltaDataItem


T = TypeVar("T", bound="AnalyticsDelta")


@_attrs_define
class AnalyticsDelta:
    """
    Attributes:
        object_ (AnalyticsDeltaObject | Unset):
        data (list[AnalyticsDeltaDataItem] | Unset):
        cursor (str | Unset):
        has_more (bool | Unset):
        note (str | Unset):
    """

    object_: AnalyticsDeltaObject | Unset = UNSET
    data: list[AnalyticsDeltaDataItem] | Unset = UNSET
    cursor: str | Unset = UNSET
    has_more: bool | Unset = UNSET
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

        cursor = self.cursor

        has_more = self.has_more

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if data is not UNSET:
            field_dict["data"] = data
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_delta_data_item import AnalyticsDeltaDataItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: AnalyticsDeltaObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = AnalyticsDeltaObject(_object_)

        _data = d.pop("data", UNSET)
        data: list[AnalyticsDeltaDataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = AnalyticsDeltaDataItem.from_dict(data_item_data)

                data.append(data_item)

        cursor = d.pop("cursor", UNSET)

        has_more = d.pop("has_more", UNSET)

        note = d.pop("note", UNSET)

        analytics_delta = cls(
            object_=object_,
            data=data,
            cursor=cursor,
            has_more=has_more,
            note=note,
        )

        analytics_delta.additional_properties = d
        return analytics_delta

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
