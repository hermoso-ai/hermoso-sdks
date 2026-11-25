from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ledger_entries_object import LedgerEntriesObject
from typing import cast

if TYPE_CHECKING:
    from ..models.ledger_entries_data_item import LedgerEntriesDataItem


T = TypeVar("T", bound="LedgerEntries")


@_attrs_define
class LedgerEntries:
    """
    Attributes:
        object_ (LedgerEntriesObject | Unset):
        data (list[LedgerEntriesDataItem] | Unset):
        total (int | None | Unset):
        next_offset (int | None | Unset):
        note (str | Unset):
    """

    object_: LedgerEntriesObject | Unset = UNSET
    data: list[LedgerEntriesDataItem] | Unset = UNSET
    total: int | None | Unset = UNSET
    next_offset: int | None | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        total: int | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        next_offset: int | None | Unset
        if isinstance(self.next_offset, Unset):
            next_offset = UNSET
        else:
            next_offset = self.next_offset

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if data is not UNSET:
            field_dict["data"] = data
        if total is not UNSET:
            field_dict["total"] = total
        if next_offset is not UNSET:
            field_dict["next_offset"] = next_offset
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_entries_data_item import LedgerEntriesDataItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: LedgerEntriesObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = LedgerEntriesObject(_object_)

        _data = d.pop("data", UNSET)
        data: list[LedgerEntriesDataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = LedgerEntriesDataItem.from_dict(data_item_data)

                data.append(data_item)

        def _parse_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total = _parse_total(d.pop("total", UNSET))

        def _parse_next_offset(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        next_offset = _parse_next_offset(d.pop("next_offset", UNSET))

        note = d.pop("note", UNSET)

        ledger_entries = cls(
            object_=object_,
            data=data,
            total=total,
            next_offset=next_offset,
            note=note,
        )

        ledger_entries.additional_properties = d
        return ledger_entries

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
