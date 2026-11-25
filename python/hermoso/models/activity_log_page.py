from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.activity_log_page_object import ActivityLogPageObject
from typing import cast

if TYPE_CHECKING:
    from ..models.activity_log_page_data_item import ActivityLogPageDataItem


T = TypeVar("T", bound="ActivityLogPage")


@_attrs_define
class ActivityLogPage:
    """
    Attributes:
        object_ (ActivityLogPageObject | Unset):
        data (list[ActivityLogPageDataItem] | Unset):
        unreadable (list[str] | Unset):
        retention_days (int | Unset):
    """

    object_: ActivityLogPageObject | Unset = UNSET
    data: list[ActivityLogPageDataItem] | Unset = UNSET
    unreadable: list[str] | Unset = UNSET
    retention_days: int | Unset = UNSET
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

        unreadable: list[str] | Unset = UNSET
        if not isinstance(self.unreadable, Unset):
            unreadable = self.unreadable

        retention_days = self.retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if data is not UNSET:
            field_dict["data"] = data
        if unreadable is not UNSET:
            field_dict["unreadable"] = unreadable
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_log_page_data_item import ActivityLogPageDataItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ActivityLogPageObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ActivityLogPageObject(_object_)

        _data = d.pop("data", UNSET)
        data: list[ActivityLogPageDataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ActivityLogPageDataItem.from_dict(data_item_data)

                data.append(data_item)

        unreadable = cast(list[str], d.pop("unreadable", UNSET))

        retention_days = d.pop("retention_days", UNSET)

        activity_log_page = cls(
            object_=object_,
            data=data,
            unreadable=unreadable,
            retention_days=retention_days,
        )

        activity_log_page.additional_properties = d
        return activity_log_page

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
