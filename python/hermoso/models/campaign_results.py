from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.campaign_results_object import CampaignResultsObject

if TYPE_CHECKING:
    from ..models.campaign_results_rows_item import CampaignResultsRowsItem
    from ..models.campaign_results_totals import CampaignResultsTotals


T = TypeVar("T", bound="CampaignResults")


@_attrs_define
class CampaignResults:
    """
    Attributes:
        object_ (CampaignResultsObject | Unset):
        upload_id (str | Unset):
        received (int | Unset):
        stored (int | Unset):
        rows (list[CampaignResultsRowsItem] | Unset):
        totals (CampaignResultsTotals | Unset):
        note (str | Unset):
    """

    object_: CampaignResultsObject | Unset = UNSET
    upload_id: str | Unset = UNSET
    received: int | Unset = UNSET
    stored: int | Unset = UNSET
    rows: list[CampaignResultsRowsItem] | Unset = UNSET
    totals: CampaignResultsTotals | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        upload_id = self.upload_id

        received = self.received

        stored = self.stored

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if upload_id is not UNSET:
            field_dict["upload_id"] = upload_id
        if received is not UNSET:
            field_dict["received"] = received
        if stored is not UNSET:
            field_dict["stored"] = stored
        if rows is not UNSET:
            field_dict["rows"] = rows
        if totals is not UNSET:
            field_dict["totals"] = totals
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.campaign_results_rows_item import CampaignResultsRowsItem  # noqa: PLC0415
        from ..models.campaign_results_totals import CampaignResultsTotals  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: CampaignResultsObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = CampaignResultsObject(_object_)

        upload_id = d.pop("upload_id", UNSET)

        received = d.pop("received", UNSET)

        stored = d.pop("stored", UNSET)

        _rows = d.pop("rows", UNSET)
        rows: list[CampaignResultsRowsItem] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = CampaignResultsRowsItem.from_dict(rows_item_data)

                rows.append(rows_item)

        _totals = d.pop("totals", UNSET)
        totals: CampaignResultsTotals | Unset
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = CampaignResultsTotals.from_dict(_totals)

        note = d.pop("note", UNSET)

        campaign_results = cls(
            object_=object_,
            upload_id=upload_id,
            received=received,
            stored=stored,
            rows=rows,
            totals=totals,
            note=note,
        )

        campaign_results.additional_properties = d
        return campaign_results

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
