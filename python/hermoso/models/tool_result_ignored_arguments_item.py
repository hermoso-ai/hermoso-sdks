from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="ToolResultIgnoredArgumentsItem")


@_attrs_define
class ToolResultIgnoredArgumentsItem:
    """
    Attributes:
        name (str | Unset): The key that was sent.
        did_you_mean (None | str | Unset): An argument THIS tool declares that the key most likely meant, or null.
    """

    name: str | Unset = UNSET
    did_you_mean: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        did_you_mean: None | str | Unset
        if isinstance(self.did_you_mean, Unset):
            did_you_mean = UNSET
        else:
            did_you_mean = self.did_you_mean

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if did_you_mean is not UNSET:
            field_dict["did_you_mean"] = did_you_mean

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_did_you_mean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        did_you_mean = _parse_did_you_mean(d.pop("did_you_mean", UNSET))

        tool_result_ignored_arguments_item = cls(
            name=name,
            did_you_mean=did_you_mean,
        )

        tool_result_ignored_arguments_item.additional_properties = d
        return tool_result_ignored_arguments_item

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
