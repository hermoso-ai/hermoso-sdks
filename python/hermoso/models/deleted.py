from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.deleted_object import DeletedObject


T = TypeVar("T", bound="Deleted")


@_attrs_define
class Deleted:
    """
    Attributes:
        object_ (DeletedObject | Unset):
        id (str | Unset):
        deleted (bool | Unset):
    """

    object_: DeletedObject | Unset = UNSET
    id: str | Unset = UNSET
    deleted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: DeletedObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = DeletedObject(_object_)

        id = d.pop("id", UNSET)

        deleted = d.pop("deleted", UNSET)

        deleted = cls(
            object_=object_,
            id=id,
            deleted=deleted,
        )

        deleted.additional_properties = d
        return deleted

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
