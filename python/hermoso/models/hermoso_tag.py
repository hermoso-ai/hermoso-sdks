from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.hermoso_tag_object import HermosoTagObject

if TYPE_CHECKING:
    from ..models.hermoso_tag_page import HermosoTagPage
    from ..models.hermoso_tag_tag import HermosoTagTag


T = TypeVar("T", bound="HermosoTag")


@_attrs_define
class HermosoTag:
    """
    Attributes:
        object_ (HermosoTagObject | Unset):
        created (bool | Unset):
        tag (HermosoTagTag | Unset):
        page (HermosoTagPage | Unset):
        note (str | Unset):
    """

    object_: HermosoTagObject | Unset = UNSET
    created: bool | Unset = UNSET
    tag: HermosoTagTag | Unset = UNSET
    page: HermosoTagPage | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        created = self.created

        tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.to_dict()

        page: dict[str, Any] | Unset = UNSET
        if not isinstance(self.page, Unset):
            page = self.page.to_dict()

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if created is not UNSET:
            field_dict["created"] = created
        if tag is not UNSET:
            field_dict["tag"] = tag
        if page is not UNSET:
            field_dict["page"] = page
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hermoso_tag_page import HermosoTagPage  # noqa: PLC0415
        from ..models.hermoso_tag_tag import HermosoTagTag  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: HermosoTagObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = HermosoTagObject(_object_)

        created = d.pop("created", UNSET)

        _tag = d.pop("tag", UNSET)
        tag: HermosoTagTag | Unset
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = HermosoTagTag.from_dict(_tag)

        _page = d.pop("page", UNSET)
        page: HermosoTagPage | Unset
        if isinstance(_page, Unset):
            page = UNSET
        else:
            page = HermosoTagPage.from_dict(_page)

        note = d.pop("note", UNSET)

        hermoso_tag = cls(
            object_=object_,
            created=created,
            tag=tag,
            page=page,
            note=note,
        )

        hermoso_tag.additional_properties = d
        return hermoso_tag

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
