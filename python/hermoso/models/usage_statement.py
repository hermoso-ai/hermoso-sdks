from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.usage_statement_object import UsageStatementObject

if TYPE_CHECKING:
    from ..models.usage_statement_brands_item import UsageStatementBrandsItem
    from ..models.usage_statement_total import UsageStatementTotal


T = TypeVar("T", bound="UsageStatement")


@_attrs_define
class UsageStatement:
    """
    Attributes:
        object_ (UsageStatementObject | Unset):
        from_ (str | Unset):
        to (str | Unset):
        group_by (str | Unset):
        brands (list[UsageStatementBrandsItem] | Unset):
        total (UsageStatementTotal | Unset):
        csv (str | Unset):
        note (str | Unset):
    """

    object_: UsageStatementObject | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    group_by: str | Unset = UNSET
    brands: list[UsageStatementBrandsItem] | Unset = UNSET
    total: UsageStatementTotal | Unset = UNSET
    csv: str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        from_ = self.from_

        to = self.to

        group_by = self.group_by

        brands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.brands, Unset):
            brands = []
            for brands_item_data in self.brands:
                brands_item = brands_item_data.to_dict()
                brands.append(brands_item)

        total: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()

        csv = self.csv

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
        if brands is not UNSET:
            field_dict["brands"] = brands
        if total is not UNSET:
            field_dict["total"] = total
        if csv is not UNSET:
            field_dict["csv"] = csv
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_statement_brands_item import UsageStatementBrandsItem  # noqa: PLC0415
        from ..models.usage_statement_total import UsageStatementTotal  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: UsageStatementObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = UsageStatementObject(_object_)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        group_by = d.pop("group_by", UNSET)

        _brands = d.pop("brands", UNSET)
        brands: list[UsageStatementBrandsItem] | Unset = UNSET
        if _brands is not UNSET:
            brands = []
            for brands_item_data in _brands:
                brands_item = UsageStatementBrandsItem.from_dict(brands_item_data)

                brands.append(brands_item)

        _total = d.pop("total", UNSET)
        total: UsageStatementTotal | Unset
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = UsageStatementTotal.from_dict(_total)

        csv = d.pop("csv", UNSET)

        note = d.pop("note", UNSET)

        usage_statement = cls(
            object_=object_,
            from_=from_,
            to=to,
            group_by=group_by,
            brands=brands,
            total=total,
            csv=csv,
            note=note,
        )

        usage_statement.additional_properties = d
        return usage_statement

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
