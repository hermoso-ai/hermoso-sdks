from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.workspace_checkout_link_object import WorkspaceCheckoutLinkObject


T = TypeVar("T", bound="WorkspaceCheckoutLink")


@_attrs_define
class WorkspaceCheckoutLink:
    """
    Attributes:
        object_ (WorkspaceCheckoutLinkObject | Unset):
        url (str | Unset):
        brand (str | Unset):
        kind (str | Unset):
        item (str | Unset):
        note (str | Unset):
    """

    object_: WorkspaceCheckoutLinkObject | Unset = UNSET
    url: str | Unset = UNSET
    brand: str | Unset = UNSET
    kind: str | Unset = UNSET
    item: str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        url = self.url

        brand = self.brand

        kind = self.kind

        item = self.item

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if url is not UNSET:
            field_dict["url"] = url
        if brand is not UNSET:
            field_dict["brand"] = brand
        if kind is not UNSET:
            field_dict["kind"] = kind
        if item is not UNSET:
            field_dict["item"] = item
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: WorkspaceCheckoutLinkObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = WorkspaceCheckoutLinkObject(_object_)

        url = d.pop("url", UNSET)

        brand = d.pop("brand", UNSET)

        kind = d.pop("kind", UNSET)

        item = d.pop("item", UNSET)

        note = d.pop("note", UNSET)

        workspace_checkout_link = cls(
            object_=object_,
            url=url,
            brand=brand,
            kind=kind,
            item=item,
            note=note,
        )

        workspace_checkout_link.additional_properties = d
        return workspace_checkout_link

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
