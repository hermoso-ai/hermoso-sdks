from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="ContentDecayBucketsItem")


@_attrs_define
class ContentDecayBucketsItem:
    """
    Attributes:
        bucket_order (int | Unset):
        bucket_label (str | Unset):
        avg_pct_of_final (float | None | Unset):
        post_count (int | Unset):
    """

    bucket_order: int | Unset = UNSET
    bucket_label: str | Unset = UNSET
    avg_pct_of_final: float | None | Unset = UNSET
    post_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_order = self.bucket_order

        bucket_label = self.bucket_label

        avg_pct_of_final: float | None | Unset
        if isinstance(self.avg_pct_of_final, Unset):
            avg_pct_of_final = UNSET
        else:
            avg_pct_of_final = self.avg_pct_of_final

        post_count = self.post_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_order is not UNSET:
            field_dict["bucket_order"] = bucket_order
        if bucket_label is not UNSET:
            field_dict["bucket_label"] = bucket_label
        if avg_pct_of_final is not UNSET:
            field_dict["avg_pct_of_final"] = avg_pct_of_final
        if post_count is not UNSET:
            field_dict["post_count"] = post_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket_order = d.pop("bucket_order", UNSET)

        bucket_label = d.pop("bucket_label", UNSET)

        def _parse_avg_pct_of_final(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_pct_of_final = _parse_avg_pct_of_final(d.pop("avg_pct_of_final", UNSET))

        post_count = d.pop("post_count", UNSET)

        content_decay_buckets_item = cls(
            bucket_order=bucket_order,
            bucket_label=bucket_label,
            avg_pct_of_final=avg_pct_of_final,
            post_count=post_count,
        )

        content_decay_buckets_item.additional_properties = d
        return content_decay_buckets_item

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
