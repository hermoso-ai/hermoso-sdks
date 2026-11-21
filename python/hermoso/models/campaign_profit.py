from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.campaign_profit_object import CampaignProfitObject

if TYPE_CHECKING:
    from ..models.campaign_profit_rows_item import CampaignProfitRowsItem
    from ..models.campaign_profit_totals_item import CampaignProfitTotalsItem
    from ..models.campaign_profit_unreadable_item import CampaignProfitUnreadableItem


T = TypeVar("T", bound="CampaignProfit")


@_attrs_define
class CampaignProfit:
    """
    Attributes:
        object_ (CampaignProfitObject | Unset):
        from_ (str | Unset):
        to (str | Unset):
        model (str | Unset):
        rows (list[CampaignProfitRowsItem] | Unset):
        totals (list[CampaignProfitTotalsItem] | Unset):
        unreadable (list[CampaignProfitUnreadableItem] | Unset):
        note (str | Unset):
    """

    object_: CampaignProfitObject | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    model: str | Unset = UNSET
    rows: list[CampaignProfitRowsItem] | Unset = UNSET
    totals: list[CampaignProfitTotalsItem] | Unset = UNSET
    unreadable: list[CampaignProfitUnreadableItem] | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        from_ = self.from_

        to = self.to

        model = self.model

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        totals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = []
            for totals_item_data in self.totals:
                totals_item = totals_item_data.to_dict()
                totals.append(totals_item)

        unreadable: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unreadable, Unset):
            unreadable = []
            for unreadable_item_data in self.unreadable:
                unreadable_item = unreadable_item_data.to_dict()
                unreadable.append(unreadable_item)

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if model is not UNSET:
            field_dict["model"] = model
        if rows is not UNSET:
            field_dict["rows"] = rows
        if totals is not UNSET:
            field_dict["totals"] = totals
        if unreadable is not UNSET:
            field_dict["unreadable"] = unreadable
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.campaign_profit_rows_item import CampaignProfitRowsItem  # noqa: PLC0415
        from ..models.campaign_profit_totals_item import CampaignProfitTotalsItem  # noqa: PLC0415
        from ..models.campaign_profit_unreadable_item import (
            CampaignProfitUnreadableItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: CampaignProfitObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = CampaignProfitObject(_object_)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        model = d.pop("model", UNSET)

        _rows = d.pop("rows", UNSET)
        rows: list[CampaignProfitRowsItem] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = CampaignProfitRowsItem.from_dict(rows_item_data)

                rows.append(rows_item)

        _totals = d.pop("totals", UNSET)
        totals: list[CampaignProfitTotalsItem] | Unset = UNSET
        if _totals is not UNSET:
            totals = []
            for totals_item_data in _totals:
                totals_item = CampaignProfitTotalsItem.from_dict(totals_item_data)

                totals.append(totals_item)

        _unreadable = d.pop("unreadable", UNSET)
        unreadable: list[CampaignProfitUnreadableItem] | Unset = UNSET
        if _unreadable is not UNSET:
            unreadable = []
            for unreadable_item_data in _unreadable:
                unreadable_item = CampaignProfitUnreadableItem.from_dict(
                    unreadable_item_data
                )

                unreadable.append(unreadable_item)

        note = d.pop("note", UNSET)

        campaign_profit = cls(
            object_=object_,
            from_=from_,
            to=to,
            model=model,
            rows=rows,
            totals=totals,
            unreadable=unreadable,
            note=note,
        )

        campaign_profit.additional_properties = d
        return campaign_profit

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
