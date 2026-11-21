from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.profit_settings_object import ProfitSettingsObject
from typing import cast

if TYPE_CHECKING:
    from ..models.profit_settings_campaign_margins import ProfitSettingsCampaignMargins


T = TypeVar("T", bound="ProfitSettings")


@_attrs_define
class ProfitSettings:
    """
    Attributes:
        object_ (ProfitSettingsObject | Unset):
        margin_percent (float | None | Unset):
        cost_per_order (float | None | Unset):
        campaign_margins (ProfitSettingsCampaignMargins | Unset):
        note (str | Unset):
    """

    object_: ProfitSettingsObject | Unset = UNSET
    margin_percent: float | None | Unset = UNSET
    cost_per_order: float | None | Unset = UNSET
    campaign_margins: ProfitSettingsCampaignMargins | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        margin_percent: float | None | Unset
        if isinstance(self.margin_percent, Unset):
            margin_percent = UNSET
        else:
            margin_percent = self.margin_percent

        cost_per_order: float | None | Unset
        if isinstance(self.cost_per_order, Unset):
            cost_per_order = UNSET
        else:
            cost_per_order = self.cost_per_order

        campaign_margins: dict[str, Any] | Unset = UNSET
        if not isinstance(self.campaign_margins, Unset):
            campaign_margins = self.campaign_margins.to_dict()

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if margin_percent is not UNSET:
            field_dict["margin_percent"] = margin_percent
        if cost_per_order is not UNSET:
            field_dict["cost_per_order"] = cost_per_order
        if campaign_margins is not UNSET:
            field_dict["campaign_margins"] = campaign_margins
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profit_settings_campaign_margins import (
            ProfitSettingsCampaignMargins,
        )  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ProfitSettingsObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ProfitSettingsObject(_object_)

        def _parse_margin_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        margin_percent = _parse_margin_percent(d.pop("margin_percent", UNSET))

        def _parse_cost_per_order(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cost_per_order = _parse_cost_per_order(d.pop("cost_per_order", UNSET))

        _campaign_margins = d.pop("campaign_margins", UNSET)
        campaign_margins: ProfitSettingsCampaignMargins | Unset
        if isinstance(_campaign_margins, Unset):
            campaign_margins = UNSET
        else:
            campaign_margins = ProfitSettingsCampaignMargins.from_dict(
                _campaign_margins
            )

        note = d.pop("note", UNSET)

        profit_settings = cls(
            object_=object_,
            margin_percent=margin_percent,
            cost_per_order=cost_per_order,
            campaign_margins=campaign_margins,
            note=note,
        )

        profit_settings.additional_properties = d
        return profit_settings

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
