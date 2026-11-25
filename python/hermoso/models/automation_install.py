from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.automation_install_object import AutomationInstallObject

if TYPE_CHECKING:
    from ..models.automation_install_failed_item import AutomationInstallFailedItem
    from ..models.automation_install_made_item import AutomationInstallMadeItem


T = TypeVar("T", bound="AutomationInstall")


@_attrs_define
class AutomationInstall:
    """
    Attributes:
        object_ (AutomationInstallObject | Unset):
        made (list[AutomationInstallMadeItem] | Unset):
        failed (list[AutomationInstallFailedItem] | Unset):
        note (str | Unset):
    """

    object_: AutomationInstallObject | Unset = UNSET
    made: list[AutomationInstallMadeItem] | Unset = UNSET
    failed: list[AutomationInstallFailedItem] | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        made: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.made, Unset):
            made = []
            for made_item_data in self.made:
                made_item = made_item_data.to_dict()
                made.append(made_item)

        failed: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed, Unset):
            failed = []
            for failed_item_data in self.failed:
                failed_item = failed_item_data.to_dict()
                failed.append(failed_item)

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if made is not UNSET:
            field_dict["made"] = made
        if failed is not UNSET:
            field_dict["failed"] = failed
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_install_failed_item import AutomationInstallFailedItem  # noqa: PLC0415
        from ..models.automation_install_made_item import AutomationInstallMadeItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: AutomationInstallObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = AutomationInstallObject(_object_)

        _made = d.pop("made", UNSET)
        made: list[AutomationInstallMadeItem] | Unset = UNSET
        if _made is not UNSET:
            made = []
            for made_item_data in _made:
                made_item = AutomationInstallMadeItem.from_dict(made_item_data)

                made.append(made_item)

        _failed = d.pop("failed", UNSET)
        failed: list[AutomationInstallFailedItem] | Unset = UNSET
        if _failed is not UNSET:
            failed = []
            for failed_item_data in _failed:
                failed_item = AutomationInstallFailedItem.from_dict(failed_item_data)

                failed.append(failed_item)

        note = d.pop("note", UNSET)

        automation_install = cls(
            object_=object_,
            made=made,
            failed=failed,
            note=note,
        )

        automation_install.additional_properties = d
        return automation_install

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
