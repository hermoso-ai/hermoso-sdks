from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.automation_list_object import AutomationListObject

if TYPE_CHECKING:
    from ..models.automation_list_data_item import AutomationListDataItem
    from ..models.automation_list_unread_item import AutomationListUnreadItem


T = TypeVar("T", bound="AutomationList")


@_attrs_define
class AutomationList:
    """
    Attributes:
        object_ (AutomationListObject | Unset):
        data (list[AutomationListDataItem] | Unset):
        unread (list[AutomationListUnreadItem] | Unset):
        note (str | Unset):
    """

    object_: AutomationListObject | Unset = UNSET
    data: list[AutomationListDataItem] | Unset = UNSET
    unread: list[AutomationListUnreadItem] | Unset = UNSET
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

        unread: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unread, Unset):
            unread = []
            for unread_item_data in self.unread:
                unread_item = unread_item_data.to_dict()
                unread.append(unread_item)

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if data is not UNSET:
            field_dict["data"] = data
        if unread is not UNSET:
            field_dict["unread"] = unread
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_list_data_item import AutomationListDataItem  # noqa: PLC0415
        from ..models.automation_list_unread_item import AutomationListUnreadItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: AutomationListObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = AutomationListObject(_object_)

        _data = d.pop("data", UNSET)
        data: list[AutomationListDataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = AutomationListDataItem.from_dict(data_item_data)

                data.append(data_item)

        _unread = d.pop("unread", UNSET)
        unread: list[AutomationListUnreadItem] | Unset = UNSET
        if _unread is not UNSET:
            unread = []
            for unread_item_data in _unread:
                unread_item = AutomationListUnreadItem.from_dict(unread_item_data)

                unread.append(unread_item)

        note = d.pop("note", UNSET)

        automation_list = cls(
            object_=object_,
            data=data,
            unread=unread,
            note=note,
        )

        automation_list.additional_properties = d
        return automation_list

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
