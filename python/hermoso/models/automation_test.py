from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.automation_test_event import AutomationTestEvent


T = TypeVar("T", bound="AutomationTest")


@_attrs_define
class AutomationTest:
    """
    Attributes:
        event (AutomationTestEvent | Unset):
        subject_id (str | Unset):
    """

    event: AutomationTestEvent | Unset = UNSET
    subject_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        subject_id = self.subject_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event
        if subject_id is not UNSET:
            field_dict["subject_id"] = subject_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_test_event import AutomationTestEvent  # noqa: PLC0415

        d = dict(src_dict)
        _event = d.pop("event", UNSET)
        event: AutomationTestEvent | Unset
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = AutomationTestEvent.from_dict(_event)

        subject_id = d.pop("subject_id", UNSET)

        automation_test = cls(
            event=event,
            subject_id=subject_id,
        )

        automation_test.additional_properties = d
        return automation_test

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
