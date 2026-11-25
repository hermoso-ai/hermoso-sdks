from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.user_list_object import UserListObject

if TYPE_CHECKING:
    from ..models.user import User
    from ..models.user_list_areas_item import UserListAreasItem
    from ..models.user_list_roles_item import UserListRolesItem


T = TypeVar("T", bound="UserList")


@_attrs_define
class UserList:
    """
    Attributes:
        object_ (UserListObject | Unset):
        data (list[User] | Unset):
        roles (list[UserListRolesItem] | Unset):
        areas (list[UserListAreasItem] | Unset):
    """

    object_: UserListObject | Unset = UNSET
    data: list[User] | Unset = UNSET
    roles: list[UserListRolesItem] | Unset = UNSET
    areas: list[UserListAreasItem] | Unset = UNSET
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

        roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.areas, Unset):
            areas = []
            for areas_item_data in self.areas:
                areas_item = areas_item_data.to_dict()
                areas.append(areas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if data is not UNSET:
            field_dict["data"] = data
        if roles is not UNSET:
            field_dict["roles"] = roles
        if areas is not UNSET:
            field_dict["areas"] = areas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User  # noqa: PLC0415
        from ..models.user_list_areas_item import UserListAreasItem  # noqa: PLC0415
        from ..models.user_list_roles_item import UserListRolesItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: UserListObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = UserListObject(_object_)

        _data = d.pop("data", UNSET)
        data: list[User] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = User.from_dict(data_item_data)

                data.append(data_item)

        _roles = d.pop("roles", UNSET)
        roles: list[UserListRolesItem] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = UserListRolesItem.from_dict(roles_item_data)

                roles.append(roles_item)

        _areas = d.pop("areas", UNSET)
        areas: list[UserListAreasItem] | Unset = UNSET
        if _areas is not UNSET:
            areas = []
            for areas_item_data in _areas:
                areas_item = UserListAreasItem.from_dict(areas_item_data)

                areas.append(areas_item)

        user_list = cls(
            object_=object_,
            data=data,
            roles=roles,
            areas=areas,
        )

        user_list.additional_properties = d
        return user_list

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
