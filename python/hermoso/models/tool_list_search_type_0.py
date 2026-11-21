from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="ToolListSearchType0")


@_attrs_define
class ToolListSearchType0:
    """Present only when `search` was sent.

    Attributes:
        query (str | Unset):
        ranked (bool | Unset): True: rows are in relevance order. False only if the ranking was unavailable on this
            server, in which case rows are a plain text match in roster order.
        strong_matches (int | None | Unset): How many of the top rows match strongly (a word of the query is in the
            tool’s name). The rows after them are looser matches.
    """

    query: str | Unset = UNSET
    ranked: bool | Unset = UNSET
    strong_matches: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        ranked = self.ranked

        strong_matches: int | None | Unset
        if isinstance(self.strong_matches, Unset):
            strong_matches = UNSET
        else:
            strong_matches = self.strong_matches

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if ranked is not UNSET:
            field_dict["ranked"] = ranked
        if strong_matches is not UNSET:
            field_dict["strong_matches"] = strong_matches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query", UNSET)

        ranked = d.pop("ranked", UNSET)

        def _parse_strong_matches(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        strong_matches = _parse_strong_matches(d.pop("strong_matches", UNSET))

        tool_list_search_type_0 = cls(
            query=query,
            ranked=ranked,
            strong_matches=strong_matches,
        )

        tool_list_search_type_0.additional_properties = d
        return tool_list_search_type_0

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
