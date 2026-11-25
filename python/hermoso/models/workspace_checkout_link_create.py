from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.workspace_checkout_link_create_kind import WorkspaceCheckoutLinkCreateKind


T = TypeVar("T", bound="WorkspaceCheckoutLinkCreate")


@_attrs_define
class WorkspaceCheckoutLinkCreate:
    """
    Attributes:
        id (str): the pack or plan id.
        kind (WorkspaceCheckoutLinkCreateKind | Unset):
    """

    id: str
    kind: WorkspaceCheckoutLinkCreateKind | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        _kind = d.pop("kind", UNSET)
        kind: WorkspaceCheckoutLinkCreateKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = WorkspaceCheckoutLinkCreateKind(_kind)

        workspace_checkout_link_create = cls(
            id=id,
            kind=kind,
        )

        workspace_checkout_link_create.additional_properties = d
        return workspace_checkout_link_create

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
