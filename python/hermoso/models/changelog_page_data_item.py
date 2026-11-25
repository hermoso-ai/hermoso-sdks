from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.changelog_page_data_item_changes_type_0 import (
        ChangelogPageDataItemChangesType0,
    )


T = TypeVar("T", bound="ChangelogPageDataItem")


@_attrs_define
class ChangelogPageDataItem:
    """
    Attributes:
        id (str | Unset):
        type_ (str | Unset):
        impact (str | Unset):
        platforms (list[str] | Unset):
        title (str | Unset):
        summary (str | Unset):
        message (str | Unset):
        published_at (str | Unset):
        changes (ChangelogPageDataItemChangesType0 | None | Unset):
    """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    impact: str | Unset = UNSET
    platforms: list[str] | Unset = UNSET
    title: str | Unset = UNSET
    summary: str | Unset = UNSET
    message: str | Unset = UNSET
    published_at: str | Unset = UNSET
    changes: ChangelogPageDataItemChangesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.changelog_page_data_item_changes_type_0 import (
            ChangelogPageDataItemChangesType0,
        )  # noqa: PLC0415

        id = self.id

        type_ = self.type_

        impact = self.impact

        platforms: list[str] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = self.platforms

        title = self.title

        summary = self.summary

        message = self.message

        published_at = self.published_at

        changes: dict[str, Any] | None | Unset
        if isinstance(self.changes, Unset):
            changes = UNSET
        elif isinstance(self.changes, ChangelogPageDataItemChangesType0):
            changes = self.changes.to_dict()
        else:
            changes = self.changes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if impact is not UNSET:
            field_dict["impact"] = impact
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if title is not UNSET:
            field_dict["title"] = title
        if summary is not UNSET:
            field_dict["summary"] = summary
        if message is not UNSET:
            field_dict["message"] = message
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.changelog_page_data_item_changes_type_0 import (
            ChangelogPageDataItemChangesType0,
        )  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        impact = d.pop("impact", UNSET)

        platforms = cast(list[str], d.pop("platforms", UNSET))

        title = d.pop("title", UNSET)

        summary = d.pop("summary", UNSET)

        message = d.pop("message", UNSET)

        published_at = d.pop("published_at", UNSET)

        def _parse_changes(
            data: object,
        ) -> ChangelogPageDataItemChangesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                changes_type_0 = ChangelogPageDataItemChangesType0.from_dict(data)

                return changes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChangelogPageDataItemChangesType0 | None | Unset, data)

        changes = _parse_changes(d.pop("changes", UNSET))

        changelog_page_data_item = cls(
            id=id,
            type_=type_,
            impact=impact,
            platforms=platforms,
            title=title,
            summary=summary,
            message=message,
            published_at=published_at,
            changes=changes,
        )

        changelog_page_data_item.additional_properties = d
        return changelog_page_data_item

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
