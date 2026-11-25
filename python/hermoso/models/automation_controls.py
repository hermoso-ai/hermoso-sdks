from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.automation_controls_object import AutomationControlsObject
from typing import cast

if TYPE_CHECKING:
    from ..models.automation_controls_ad_accounts_item import (
        AutomationControlsAdAccountsItem,
    )


T = TypeVar("T", bound="AutomationControls")


@_attrs_define
class AutomationControls:
    """
    Attributes:
        object_ (AutomationControlsObject | Unset):
        paused (bool | Unset):
        paused_at (None | str | Unset):
        ad_accounts (list[AutomationControlsAdAccountsItem] | Unset):
        needs_confirm (bool | Unset):
        note (str | Unset):
    """

    object_: AutomationControlsObject | Unset = UNSET
    paused: bool | Unset = UNSET
    paused_at: None | str | Unset = UNSET
    ad_accounts: list[AutomationControlsAdAccountsItem] | Unset = UNSET
    needs_confirm: bool | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        paused = self.paused

        paused_at: None | str | Unset
        if isinstance(self.paused_at, Unset):
            paused_at = UNSET
        else:
            paused_at = self.paused_at

        ad_accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ad_accounts, Unset):
            ad_accounts = []
            for ad_accounts_item_data in self.ad_accounts:
                ad_accounts_item = ad_accounts_item_data.to_dict()
                ad_accounts.append(ad_accounts_item)

        needs_confirm = self.needs_confirm

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if paused is not UNSET:
            field_dict["paused"] = paused
        if paused_at is not UNSET:
            field_dict["paused_at"] = paused_at
        if ad_accounts is not UNSET:
            field_dict["ad_accounts"] = ad_accounts
        if needs_confirm is not UNSET:
            field_dict["needs_confirm"] = needs_confirm
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_controls_ad_accounts_item import (
            AutomationControlsAdAccountsItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: AutomationControlsObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = AutomationControlsObject(_object_)

        paused = d.pop("paused", UNSET)

        def _parse_paused_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        paused_at = _parse_paused_at(d.pop("paused_at", UNSET))

        _ad_accounts = d.pop("ad_accounts", UNSET)
        ad_accounts: list[AutomationControlsAdAccountsItem] | Unset = UNSET
        if _ad_accounts is not UNSET:
            ad_accounts = []
            for ad_accounts_item_data in _ad_accounts:
                ad_accounts_item = AutomationControlsAdAccountsItem.from_dict(
                    ad_accounts_item_data
                )

                ad_accounts.append(ad_accounts_item)

        needs_confirm = d.pop("needs_confirm", UNSET)

        note = d.pop("note", UNSET)

        automation_controls = cls(
            object_=object_,
            paused=paused,
            paused_at=paused_at,
            ad_accounts=ad_accounts,
            needs_confirm=needs_confirm,
            note=note,
        )

        automation_controls.additional_properties = d
        return automation_controls

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
