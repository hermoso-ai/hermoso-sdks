from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tool_list_object import ToolListObject
from typing import cast

if TYPE_CHECKING:
    from ..models.tool import Tool
    from ..models.tool_list_areas_item import ToolListAreasItem
    from ..models.tool_list_search_type_0 import ToolListSearchType0
    from ..models.warning import Warning_


T = TypeVar("T", bound="ToolList")


@_attrs_define
class ToolList:
    """
    Attributes:
        object_ (ToolListObject | Unset):
        areas (list[ToolListAreasItem] | Unset): Every area holding at least one tool available to this workspace, so
            one call shows the whole map before you page through it.
        data (list[Tool] | Unset):
        total (int | Unset): Tools matching this filter, across all pages.
        has_more (bool | Unset):
        next_cursor (None | str | Unset): Pass it back as `starting_after`.
        limit (int | Unset):
        search (None | ToolListSearchType0 | Unset): Present only when `search` was sent.
        warnings (list[Warning_] | Unset):
    """

    object_: ToolListObject | Unset = UNSET
    areas: list[ToolListAreasItem] | Unset = UNSET
    data: list[Tool] | Unset = UNSET
    total: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    next_cursor: None | str | Unset = UNSET
    limit: int | Unset = UNSET
    search: None | ToolListSearchType0 | Unset = UNSET
    warnings: list[Warning_] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_list_search_type_0 import ToolListSearchType0  # noqa: PLC0415

        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.areas, Unset):
            areas = []
            for areas_item_data in self.areas:
                areas_item = areas_item_data.to_dict()
                areas.append(areas_item)

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        total = self.total

        has_more = self.has_more

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        limit = self.limit

        search: dict[str, Any] | None | Unset
        if isinstance(self.search, Unset):
            search = UNSET
        elif isinstance(self.search, ToolListSearchType0):
            search = self.search.to_dict()
        else:
            search = self.search

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if areas is not UNSET:
            field_dict["areas"] = areas
        if data is not UNSET:
            field_dict["data"] = data
        if total is not UNSET:
            field_dict["total"] = total
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if limit is not UNSET:
            field_dict["limit"] = limit
        if search is not UNSET:
            field_dict["search"] = search
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool import Tool  # noqa: PLC0415
        from ..models.tool_list_areas_item import ToolListAreasItem  # noqa: PLC0415
        from ..models.tool_list_search_type_0 import ToolListSearchType0  # noqa: PLC0415
        from ..models.warning import Warning_  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ToolListObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ToolListObject(_object_)

        _areas = d.pop("areas", UNSET)
        areas: list[ToolListAreasItem] | Unset = UNSET
        if _areas is not UNSET:
            areas = []
            for areas_item_data in _areas:
                areas_item = ToolListAreasItem.from_dict(areas_item_data)

                areas.append(areas_item)

        _data = d.pop("data", UNSET)
        data: list[Tool] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = Tool.from_dict(data_item_data)

                data.append(data_item)

        total = d.pop("total", UNSET)

        has_more = d.pop("has_more", UNSET)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))

        limit = d.pop("limit", UNSET)

        def _parse_search(data: object) -> None | ToolListSearchType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_type_0 = ToolListSearchType0.from_dict(data)

                return search_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolListSearchType0 | Unset, data)

        search = _parse_search(d.pop("search", UNSET))

        _warnings = d.pop("warnings", UNSET)
        warnings: list[Warning_] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = Warning_.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        tool_list = cls(
            object_=object_,
            areas=areas,
            data=data,
            total=total,
            has_more=has_more,
            next_cursor=next_cursor,
            limit=limit,
            search=search,
            warnings=warnings,
        )

        tool_list.additional_properties = d
        return tool_list

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
