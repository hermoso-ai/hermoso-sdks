from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.metrics_result_object import MetricsResultObject
from typing import cast

if TYPE_CHECKING:
    from ..models.metrics_result_rows_item import MetricsResultRowsItem


T = TypeVar("T", bound="MetricsResult")


@_attrs_define
class MetricsResult:
    """
    Attributes:
        object_ (MetricsResultObject | Unset):
        entity (str | Unset):
        granularity (str | Unset):
        rows (list[MetricsResultRowsItem] | Unset):
        notes (list[str] | Unset):
        text (str | Unset):
    """

    object_: MetricsResultObject | Unset = UNSET
    entity: str | Unset = UNSET
    granularity: str | Unset = UNSET
    rows: list[MetricsResultRowsItem] | Unset = UNSET
    notes: list[str] | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        entity = self.entity

        granularity = self.granularity

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        notes: list[str] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if entity is not UNSET:
            field_dict["entity"] = entity
        if granularity is not UNSET:
            field_dict["granularity"] = granularity
        if rows is not UNSET:
            field_dict["rows"] = rows
        if notes is not UNSET:
            field_dict["notes"] = notes
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metrics_result_rows_item import MetricsResultRowsItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: MetricsResultObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = MetricsResultObject(_object_)

        entity = d.pop("entity", UNSET)

        granularity = d.pop("granularity", UNSET)

        _rows = d.pop("rows", UNSET)
        rows: list[MetricsResultRowsItem] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = MetricsResultRowsItem.from_dict(rows_item_data)

                rows.append(rows_item)

        notes = cast(list[str], d.pop("notes", UNSET))

        text = d.pop("text", UNSET)

        metrics_result = cls(
            object_=object_,
            entity=entity,
            granularity=granularity,
            rows=rows,
            notes=notes,
            text=text,
        )

        metrics_result.additional_properties = d
        return metrics_result

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
