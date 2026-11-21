from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.hermoso_tag_install_result_object import HermosoTagInstallResultObject


T = TypeVar("T", bound="HermosoTagInstallResult")


@_attrs_define
class HermosoTagInstallResult:
    """
    Attributes:
        object_ (HermosoTagInstallResultObject | Unset):
        tag_id (str | Unset):
        site (str | Unset):
        installed (bool | Unset):
        removed (bool | Unset):
        needs_confirm (bool | Unset):
        snippet (str | Unset):
        note (str | Unset):
    """

    object_: HermosoTagInstallResultObject | Unset = UNSET
    tag_id: str | Unset = UNSET
    site: str | Unset = UNSET
    installed: bool | Unset = UNSET
    removed: bool | Unset = UNSET
    needs_confirm: bool | Unset = UNSET
    snippet: str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        tag_id = self.tag_id

        site = self.site

        installed = self.installed

        removed = self.removed

        needs_confirm = self.needs_confirm

        snippet = self.snippet

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if tag_id is not UNSET:
            field_dict["tag_id"] = tag_id
        if site is not UNSET:
            field_dict["site"] = site
        if installed is not UNSET:
            field_dict["installed"] = installed
        if removed is not UNSET:
            field_dict["removed"] = removed
        if needs_confirm is not UNSET:
            field_dict["needs_confirm"] = needs_confirm
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: HermosoTagInstallResultObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = HermosoTagInstallResultObject(_object_)

        tag_id = d.pop("tag_id", UNSET)

        site = d.pop("site", UNSET)

        installed = d.pop("installed", UNSET)

        removed = d.pop("removed", UNSET)

        needs_confirm = d.pop("needs_confirm", UNSET)

        snippet = d.pop("snippet", UNSET)

        note = d.pop("note", UNSET)

        hermoso_tag_install_result = cls(
            object_=object_,
            tag_id=tag_id,
            site=site,
            installed=installed,
            removed=removed,
            needs_confirm=needs_confirm,
            snippet=snippet,
            note=note,
        )

        hermoso_tag_install_result.additional_properties = d
        return hermoso_tag_install_result

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
