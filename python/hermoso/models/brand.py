from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.brand_object import BrandObject
from typing import cast

if TYPE_CHECKING:
    from ..models.brand_headers import BrandHeaders


T = TypeVar("T", bound="Brand")


@_attrs_define
class Brand:
    """
    Attributes:
        object_ (BrandObject | Unset):
        id (str | Unset): The value `X-Hermoso-User` takes.
        name (None | str | Unset):
        is_default (bool | Unset): The account’s anchor profile, whose id is the literal `default`. It is what a request
            with no `X-Hermoso-User` and an unpinned key acts on.
        current (bool | Unset): The profile THIS request resolved to.
        shared (bool | Unset): True for a profile owned by another account that you were invited into.
        owner_account_id (None | str | Unset): Only on a shared profile: the value `X-Hermoso-Owner` takes.
        role (str | Unset): owner for your own profiles; your role on a shared one.
        headers (BrandHeaders | Unset): Exactly the headers that select this profile.
    """

    object_: BrandObject | Unset = UNSET
    id: str | Unset = UNSET
    name: None | str | Unset = UNSET
    is_default: bool | Unset = UNSET
    current: bool | Unset = UNSET
    shared: bool | Unset = UNSET
    owner_account_id: None | str | Unset = UNSET
    role: str | Unset = UNSET
    headers: BrandHeaders | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_default = self.is_default

        current = self.current

        shared = self.shared

        owner_account_id: None | str | Unset
        if isinstance(self.owner_account_id, Unset):
            owner_account_id = UNSET
        else:
            owner_account_id = self.owner_account_id

        role = self.role

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if current is not UNSET:
            field_dict["current"] = current
        if shared is not UNSET:
            field_dict["shared"] = shared
        if owner_account_id is not UNSET:
            field_dict["owner_account_id"] = owner_account_id
        if role is not UNSET:
            field_dict["role"] = role
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brand_headers import BrandHeaders  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: BrandObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = BrandObject(_object_)

        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        is_default = d.pop("is_default", UNSET)

        current = d.pop("current", UNSET)

        shared = d.pop("shared", UNSET)

        def _parse_owner_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_account_id = _parse_owner_account_id(d.pop("owner_account_id", UNSET))

        role = d.pop("role", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: BrandHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = BrandHeaders.from_dict(_headers)

        brand = cls(
            object_=object_,
            id=id,
            name=name,
            is_default=is_default,
            current=current,
            shared=shared,
            owner_account_id=owner_account_id,
            role=role,
            headers=headers,
        )

        brand.additional_properties = d
        return brand

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
