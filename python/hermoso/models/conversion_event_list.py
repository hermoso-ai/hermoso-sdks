from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conversion_event_list_object import ConversionEventListObject
from typing import cast

if TYPE_CHECKING:
    from ..models.conversion_event_list_data_item import ConversionEventListDataItem


T = TypeVar("T", bound="ConversionEventList")


@_attrs_define
class ConversionEventList:
    """
    Attributes:
        object_ (ConversionEventListObject | Unset):
        data (list[ConversionEventListDataItem] | Unset):
        total (int | Unset):
        next_cursor (None | str | Unset):
        note (str | Unset):
    """

    object_: ConversionEventListObject | Unset = UNSET
    data: list[ConversionEventListDataItem] | Unset = UNSET
    total: int | Unset = UNSET
    next_cursor: None | str | Unset = UNSET
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

        total = self.total

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if data is not UNSET:
            field_dict["data"] = data
        if total is not UNSET:
            field_dict["total"] = total
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_event_list_data_item import ConversionEventListDataItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ConversionEventListObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ConversionEventListObject(_object_)

        _data = d.pop("data", UNSET)
        data: list[ConversionEventListDataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ConversionEventListDataItem.from_dict(data_item_data)

                data.append(data_item)

        total = d.pop("total", UNSET)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))

        note = d.pop("note", UNSET)

        conversion_event_list = cls(
            object_=object_,
            data=data,
            total=total,
            next_cursor=next_cursor,
            note=note,
        )

        conversion_event_list.additional_properties = d
        return conversion_event_list

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
