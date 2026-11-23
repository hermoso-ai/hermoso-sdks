from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="RecastPerson")


@_attrs_define
class RecastPerson:
    """Who goes into the video. Send exactly ONE of the three.

    Attributes:
        creator_id (str | Unset): A saved creator's id or exact name, or a preset AI creator's id (the `list_creators`
            tool lists both). A saved photo of a real person needs a paid plan or a credit pack.
        image_url (str | Unset): A clear photo of the person (https or a Hermoso file URL). A photo of a real person
            needs a paid plan or a credit pack, and sending it confirms you have their permission; the confirmation is
            recorded. A portrait Hermoso made from words for this account counts as an AI person on every plan.
        describe (str | Unset): An AI person made from your words, on every plan: age, hair, style, vibe ("a man in his
            40s, short grey hair, navy sweater"). Never a real or famous person by name. The person is made first (priced as
            its own step) and lands in your Library.
    """

    creator_id: str | Unset = UNSET
    image_url: str | Unset = UNSET
    describe: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator_id = self.creator_id

        image_url = self.image_url

        describe = self.describe

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creator_id is not UNSET:
            field_dict["creator_id"] = creator_id
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if describe is not UNSET:
            field_dict["describe"] = describe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_id = d.pop("creator_id", UNSET)

        image_url = d.pop("image_url", UNSET)

        describe = d.pop("describe", UNSET)

        recast_person = cls(
            creator_id=creator_id,
            image_url=image_url,
            describe=describe,
        )

        recast_person.additional_properties = d
        return recast_person

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
