from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ad_change_object import AdChangeObject
from ..models.ad_change_status import AdChangeStatus
from typing import cast

if TYPE_CHECKING:
    from ..models.ad_change_after_item import AdChangeAfterItem
    from ..models.ad_change_before_type_0_item import AdChangeBeforeType0Item


T = TypeVar("T", bound="AdChange")


@_attrs_define
class AdChange:
    """
    Attributes:
        object_ (AdChangeObject | Unset):
        id (str | Unset):
        tool (str | Unset):
        platform (str | Unset):
        title (str | Unset):
        status (AdChangeStatus | Unset):
        after (list[AdChangeAfterItem] | Unset):
        before (list[AdChangeBeforeType0Item] | None | Unset):
        result (str | Unset):
        needs_confirm (bool | Unset):
        note (str | Unset):
    """

    object_: AdChangeObject | Unset = UNSET
    id: str | Unset = UNSET
    tool: str | Unset = UNSET
    platform: str | Unset = UNSET
    title: str | Unset = UNSET
    status: AdChangeStatus | Unset = UNSET
    after: list[AdChangeAfterItem] | Unset = UNSET
    before: list[AdChangeBeforeType0Item] | None | Unset = UNSET
    result: str | Unset = UNSET
    needs_confirm: bool | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        tool = self.tool

        platform = self.platform

        title = self.title

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        after: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.after, Unset):
            after = []
            for after_item_data in self.after:
                after_item = after_item_data.to_dict()
                after.append(after_item)

        before: list[dict[str, Any]] | None | Unset
        if isinstance(self.before, Unset):
            before = UNSET
        elif isinstance(self.before, list):
            before = []
            for before_type_0_item_data in self.before:
                before_type_0_item = before_type_0_item_data.to_dict()
                before.append(before_type_0_item)

        else:
            before = self.before

        result = self.result

        needs_confirm = self.needs_confirm

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if tool is not UNSET:
            field_dict["tool"] = tool
        if platform is not UNSET:
            field_dict["platform"] = platform
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before
        if result is not UNSET:
            field_dict["result"] = result
        if needs_confirm is not UNSET:
            field_dict["needs_confirm"] = needs_confirm
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_change_after_item import AdChangeAfterItem  # noqa: PLC0415
        from ..models.ad_change_before_type_0_item import AdChangeBeforeType0Item  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: AdChangeObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = AdChangeObject(_object_)

        id = d.pop("id", UNSET)

        tool = d.pop("tool", UNSET)

        platform = d.pop("platform", UNSET)

        title = d.pop("title", UNSET)

        _status = d.pop("status", UNSET)
        status: AdChangeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AdChangeStatus(_status)

        _after = d.pop("after", UNSET)
        after: list[AdChangeAfterItem] | Unset = UNSET
        if _after is not UNSET:
            after = []
            for after_item_data in _after:
                after_item = AdChangeAfterItem.from_dict(after_item_data)

                after.append(after_item)

        def _parse_before(data: object) -> list[AdChangeBeforeType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                before_type_0 = []
                _before_type_0 = data
                for before_type_0_item_data in _before_type_0:
                    before_type_0_item = AdChangeBeforeType0Item.from_dict(
                        before_type_0_item_data
                    )

                    before_type_0.append(before_type_0_item)

                return before_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AdChangeBeforeType0Item] | None | Unset, data)

        before = _parse_before(d.pop("before", UNSET))

        result = d.pop("result", UNSET)

        needs_confirm = d.pop("needs_confirm", UNSET)

        note = d.pop("note", UNSET)

        ad_change = cls(
            object_=object_,
            id=id,
            tool=tool,
            platform=platform,
            title=title,
            status=status,
            after=after,
            before=before,
            result=result,
            needs_confirm=needs_confirm,
            note=note,
        )

        ad_change.additional_properties = d
        return ad_change

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
