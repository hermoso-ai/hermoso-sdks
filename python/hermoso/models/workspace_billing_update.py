from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="WorkspaceBillingUpdate")


@_attrs_define
class WorkspaceBillingUpdate:
    """
    Attributes:
        billed_separately (bool | Unset):
        confirm (bool | Unset): true after the account holder agreed to change who pays.
    """

    billed_separately: bool | Unset = UNSET
    confirm: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billed_separately = self.billed_separately

        confirm = self.confirm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billed_separately is not UNSET:
            field_dict["billed_separately"] = billed_separately
        if confirm is not UNSET:
            field_dict["confirm"] = confirm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billed_separately = d.pop("billed_separately", UNSET)

        confirm = d.pop("confirm", UNSET)

        workspace_billing_update = cls(
            billed_separately=billed_separately,
            confirm=confirm,
        )

        workspace_billing_update.additional_properties = d
        return workspace_billing_update

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
