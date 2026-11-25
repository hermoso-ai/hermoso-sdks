from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ad_account_automation_controls_update_platform import (
    AdAccountAutomationControlsUpdatePlatform,
)
from typing import cast


T = TypeVar("T", bound="AdAccountAutomationControlsUpdate")


@_attrs_define
class AdAccountAutomationControlsUpdate:
    """
    Attributes:
        platform (AdAccountAutomationControlsUpdatePlatform):
        ad_account_id (str):
        paused (bool | Unset):
        daily_raise_limit (float | None | Unset):
        confirm (bool | Unset):
    """

    platform: AdAccountAutomationControlsUpdatePlatform
    ad_account_id: str
    paused: bool | Unset = UNSET
    daily_raise_limit: float | None | Unset = UNSET
    confirm: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform.value

        ad_account_id = self.ad_account_id

        paused = self.paused

        daily_raise_limit: float | None | Unset
        if isinstance(self.daily_raise_limit, Unset):
            daily_raise_limit = UNSET
        else:
            daily_raise_limit = self.daily_raise_limit

        confirm = self.confirm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "ad_account_id": ad_account_id,
            }
        )
        if paused is not UNSET:
            field_dict["paused"] = paused
        if daily_raise_limit is not UNSET:
            field_dict["daily_raise_limit"] = daily_raise_limit
        if confirm is not UNSET:
            field_dict["confirm"] = confirm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform = AdAccountAutomationControlsUpdatePlatform(d.pop("platform"))

        ad_account_id = d.pop("ad_account_id")

        paused = d.pop("paused", UNSET)

        def _parse_daily_raise_limit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        daily_raise_limit = _parse_daily_raise_limit(d.pop("daily_raise_limit", UNSET))

        confirm = d.pop("confirm", UNSET)

        ad_account_automation_controls_update = cls(
            platform=platform,
            ad_account_id=ad_account_id,
            paused=paused,
            daily_raise_limit=daily_raise_limit,
            confirm=confirm,
        )

        ad_account_automation_controls_update.additional_properties = d
        return ad_account_automation_controls_update

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
