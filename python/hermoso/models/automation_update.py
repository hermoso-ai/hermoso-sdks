from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.automation_update_changes import AutomationUpdateChanges


T = TypeVar("T", bound="AutomationUpdate")


@_attrs_define
class AutomationUpdate:
    """
    Attributes:
        changes (AutomationUpdateChanges | Unset):
    """

    changes: AutomationUpdateChanges | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = self.changes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_update_changes import AutomationUpdateChanges  # noqa: PLC0415

        d = dict(src_dict)
        _changes = d.pop("changes", UNSET)
        changes: AutomationUpdateChanges | Unset
        if isinstance(_changes, Unset):
            changes = UNSET
        else:
            changes = AutomationUpdateChanges.from_dict(_changes)

        automation_update = cls(
            changes=changes,
        )

        automation_update.additional_properties = d
        return automation_update

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
