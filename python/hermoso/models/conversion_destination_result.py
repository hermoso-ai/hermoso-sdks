from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conversion_destination_result_object import (
    ConversionDestinationResultObject,
)

if TYPE_CHECKING:
    from ..models.conversion_destination_result_destination import (
        ConversionDestinationResultDestination,
    )


T = TypeVar("T", bound="ConversionDestinationResult")


@_attrs_define
class ConversionDestinationResult:
    """
    Attributes:
        object_ (ConversionDestinationResultObject | Unset):
        destination (ConversionDestinationResultDestination | Unset):
        verified (bool | Unset):
        note (str | Unset):
    """

    object_: ConversionDestinationResultObject | Unset = UNSET
    destination: ConversionDestinationResultDestination | Unset = UNSET
    verified: bool | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        verified = self.verified

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if destination is not UNSET:
            field_dict["destination"] = destination
        if verified is not UNSET:
            field_dict["verified"] = verified
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_destination_result_destination import (
            ConversionDestinationResultDestination,
        )  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ConversionDestinationResultObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ConversionDestinationResultObject(_object_)

        _destination = d.pop("destination", UNSET)
        destination: ConversionDestinationResultDestination | Unset
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = ConversionDestinationResultDestination.from_dict(_destination)

        verified = d.pop("verified", UNSET)

        note = d.pop("note", UNSET)

        conversion_destination_result = cls(
            object_=object_,
            destination=destination,
            verified=verified,
            note=note,
        )

        conversion_destination_result.additional_properties = d
        return conversion_destination_result

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
