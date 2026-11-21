from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.hermoso_tag_report_object import HermosoTagReportObject

if TYPE_CHECKING:
    from ..models.hermoso_tag_report_rows_item import HermosoTagReportRowsItem
    from ..models.hermoso_tag_report_status import HermosoTagReportStatus
    from ..models.hermoso_tag_report_totals import HermosoTagReportTotals


T = TypeVar("T", bound="HermosoTagReport")


@_attrs_define
class HermosoTagReport:
    """
    Attributes:
        object_ (HermosoTagReportObject | Unset):
        from_ (str | Unset):
        to (str | Unset):
        group_by (str | Unset):
        totals (HermosoTagReportTotals | Unset):
        rows (list[HermosoTagReportRowsItem] | Unset):
        status (HermosoTagReportStatus | Unset):
        note (str | Unset):
    """

    object_: HermosoTagReportObject | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    group_by: str | Unset = UNSET
    totals: HermosoTagReportTotals | Unset = UNSET
    rows: list[HermosoTagReportRowsItem] | Unset = UNSET
    status: HermosoTagReportStatus | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        from_ = self.from_

        to = self.to

        group_by = self.group_by

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

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
        if group_by is not UNSET:
            field_dict["group_by"] = group_by
        if totals is not UNSET:
            field_dict["totals"] = totals
        if rows is not UNSET:
            field_dict["rows"] = rows
        if status is not UNSET:
            field_dict["status"] = status
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hermoso_tag_report_rows_item import HermosoTagReportRowsItem  # noqa: PLC0415
        from ..models.hermoso_tag_report_status import HermosoTagReportStatus  # noqa: PLC0415
        from ..models.hermoso_tag_report_totals import HermosoTagReportTotals  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: HermosoTagReportObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = HermosoTagReportObject(_object_)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        group_by = d.pop("group_by", UNSET)

        _totals = d.pop("totals", UNSET)
        totals: HermosoTagReportTotals | Unset
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = HermosoTagReportTotals.from_dict(_totals)

        _rows = d.pop("rows", UNSET)
        rows: list[HermosoTagReportRowsItem] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = HermosoTagReportRowsItem.from_dict(rows_item_data)

                rows.append(rows_item)

        _status = d.pop("status", UNSET)
        status: HermosoTagReportStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = HermosoTagReportStatus.from_dict(_status)

        note = d.pop("note", UNSET)

        hermoso_tag_report = cls(
            object_=object_,
            from_=from_,
            to=to,
            group_by=group_by,
            totals=totals,
            rows=rows,
            status=status,
            note=note,
        )

        hermoso_tag_report.additional_properties = d
        return hermoso_tag_report

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
