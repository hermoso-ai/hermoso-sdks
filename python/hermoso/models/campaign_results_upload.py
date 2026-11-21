from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.campaign_results_upload_rows_item import CampaignResultsUploadRowsItem


T = TypeVar("T", bound="CampaignResultsUpload")


@_attrs_define
class CampaignResultsUpload:
    """
    Attributes:
        rows (list[CampaignResultsUploadRowsItem] | Unset):
        csv (str | Unset):
    """

    rows: list[CampaignResultsUploadRowsItem] | Unset = UNSET
    csv: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        csv = self.csv

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rows is not UNSET:
            field_dict["rows"] = rows
        if csv is not UNSET:
            field_dict["csv"] = csv

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.campaign_results_upload_rows_item import (
            CampaignResultsUploadRowsItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        _rows = d.pop("rows", UNSET)
        rows: list[CampaignResultsUploadRowsItem] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = CampaignResultsUploadRowsItem.from_dict(rows_item_data)

                rows.append(rows_item)

        csv = d.pop("csv", UNSET)

        campaign_results_upload = cls(
            rows=rows,
            csv=csv,
        )

        campaign_results_upload.additional_properties = d
        return campaign_results_upload

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
