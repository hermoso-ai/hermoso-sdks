from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.job_list_object import JobListObject
from typing import cast

if TYPE_CHECKING:
    from ..models.job import Job


T = TypeVar("T", bound="JobList")


@_attrs_define
class JobList:
    """
    Attributes:
        object_ (JobListObject | Unset):
        data (list[Job] | Unset):
        running (int | Unset): How many of the jobs matching this filter are running right now.
        has_more (bool | Unset):
        next_cursor (None | str | Unset): Pass it back as `starting_after`.
    """

    object_: JobListObject | Unset = UNSET
    data: list[Job] | Unset = UNSET
    running: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    next_cursor: None | str | Unset = UNSET
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

        running = self.running

        has_more = self.has_more

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if data is not UNSET:
            field_dict["data"] = data
        if running is not UNSET:
            field_dict["running"] = running
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job import Job  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: JobListObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = JobListObject(_object_)

        _data = d.pop("data", UNSET)
        data: list[Job] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = Job.from_dict(data_item_data)

                data.append(data_item)

        running = d.pop("running", UNSET)

        has_more = d.pop("has_more", UNSET)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))

        job_list = cls(
            object_=object_,
            data=data,
            running=running,
            has_more=has_more,
            next_cursor=next_cursor,
        )

        job_list.additional_properties = d
        return job_list

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
