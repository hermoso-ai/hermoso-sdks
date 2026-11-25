from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.automation_run_list_object import AutomationRunListObject

if TYPE_CHECKING:
    from ..models.automation_run_list_data_item import AutomationRunListDataItem


T = TypeVar("T", bound="AutomationRunList")


@_attrs_define
class AutomationRunList:
    """
    Attributes:
        object_ (AutomationRunListObject | Unset):
        data (list[AutomationRunListDataItem] | Unset):
        note (str | Unset):
    """

    object_: AutomationRunListObject | Unset = UNSET
    data: list[AutomationRunListDataItem] | Unset = UNSET
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

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if data is not UNSET:
            field_dict["data"] = data
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_run_list_data_item import AutomationRunListDataItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: AutomationRunListObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = AutomationRunListObject(_object_)

        _data = d.pop("data", UNSET)
        data: list[AutomationRunListDataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = AutomationRunListDataItem.from_dict(data_item_data)

                data.append(data_item)

        note = d.pop("note", UNSET)

        automation_run_list = cls(
            object_=object_,
            data=data,
            note=note,
        )

        automation_run_list.additional_properties = d
        return automation_run_list

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
