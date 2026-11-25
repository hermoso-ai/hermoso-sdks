from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="AutomationActivate")


@_attrs_define
class AutomationActivate:
    """
    Attributes:
        confirm (bool | Unset):
        confirm_scope (str | Unset):
    """

    confirm: bool | Unset = UNSET
    confirm_scope: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confirm = self.confirm

        confirm_scope = self.confirm_scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confirm is not UNSET:
            field_dict["confirm"] = confirm
        if confirm_scope is not UNSET:
            field_dict["confirm_scope"] = confirm_scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirm = d.pop("confirm", UNSET)

        confirm_scope = d.pop("confirm_scope", UNSET)

        automation_activate = cls(
            confirm=confirm,
            confirm_scope=confirm_scope,
        )

        automation_activate.additional_properties = d
        return automation_activate

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
