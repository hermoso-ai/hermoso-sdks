from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.workspace_object import WorkspaceObject
from typing import cast


T = TypeVar("T", bound="Workspace")


@_attrs_define
class Workspace:
    """
    Attributes:
        object_ (WorkspaceObject | Unset):
        id (str | Unset):
        name (str | Unset):
        current (bool | Unset):
        shared (bool | Unset):
        owner_account_id (None | str | Unset):
        role (None | str | Unset):
    """

    object_: WorkspaceObject | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    current: bool | Unset = UNSET
    shared: bool | Unset = UNSET
    owner_account_id: None | str | Unset = UNSET
    role: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        name = self.name

        current = self.current

        shared = self.shared

        owner_account_id: None | str | Unset
        if isinstance(self.owner_account_id, Unset):
            owner_account_id = UNSET
        else:
            owner_account_id = self.owner_account_id

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if current is not UNSET:
            field_dict["current"] = current
        if shared is not UNSET:
            field_dict["shared"] = shared
        if owner_account_id is not UNSET:
            field_dict["owner_account_id"] = owner_account_id
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: WorkspaceObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = WorkspaceObject(_object_)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        current = d.pop("current", UNSET)

        shared = d.pop("shared", UNSET)

        def _parse_owner_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_account_id = _parse_owner_account_id(d.pop("owner_account_id", UNSET))

        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        workspace = cls(
            object_=object_,
            id=id,
            name=name,
            current=current,
            shared=shared,
            owner_account_id=owner_account_id,
            role=role,
        )

        workspace.additional_properties = d
        return workspace

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
