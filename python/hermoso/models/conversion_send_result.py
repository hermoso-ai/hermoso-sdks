from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conversion_send_result_object import ConversionSendResultObject
from typing import cast

if TYPE_CHECKING:
    from ..models.conversion_send_result_destinations_item import (
        ConversionSendResultDestinationsItem,
    )


T = TypeVar("T", bound="ConversionSendResult")


@_attrs_define
class ConversionSendResult:
    """
    Attributes:
        object_ (ConversionSendResultObject | Unset):
        events_received (int | Unset):
        stored (bool | Unset):
        test_code (None | str | Unset):
        validate_only (bool | Unset):
        destinations (list[ConversionSendResultDestinationsItem] | Unset):
        carried_click_ids (int | Unset):
        note (str | Unset):
    """

    object_: ConversionSendResultObject | Unset = UNSET
    events_received: int | Unset = UNSET
    stored: bool | Unset = UNSET
    test_code: None | str | Unset = UNSET
    validate_only: bool | Unset = UNSET
    destinations: list[ConversionSendResultDestinationsItem] | Unset = UNSET
    carried_click_ids: int | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        events_received = self.events_received

        stored = self.stored

        test_code: None | str | Unset
        if isinstance(self.test_code, Unset):
            test_code = UNSET
        else:
            test_code = self.test_code

        validate_only = self.validate_only

        destinations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.destinations, Unset):
            destinations = []
            for destinations_item_data in self.destinations:
                destinations_item = destinations_item_data.to_dict()
                destinations.append(destinations_item)

        carried_click_ids = self.carried_click_ids

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if events_received is not UNSET:
            field_dict["events_received"] = events_received
        if stored is not UNSET:
            field_dict["stored"] = stored
        if test_code is not UNSET:
            field_dict["test_code"] = test_code
        if validate_only is not UNSET:
            field_dict["validate_only"] = validate_only
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if carried_click_ids is not UNSET:
            field_dict["carried_click_ids"] = carried_click_ids
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_send_result_destinations_item import (
            ConversionSendResultDestinationsItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ConversionSendResultObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ConversionSendResultObject(_object_)

        events_received = d.pop("events_received", UNSET)

        stored = d.pop("stored", UNSET)

        def _parse_test_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        test_code = _parse_test_code(d.pop("test_code", UNSET))

        validate_only = d.pop("validate_only", UNSET)

        _destinations = d.pop("destinations", UNSET)
        destinations: list[ConversionSendResultDestinationsItem] | Unset = UNSET
        if _destinations is not UNSET:
            destinations = []
            for destinations_item_data in _destinations:
                destinations_item = ConversionSendResultDestinationsItem.from_dict(
                    destinations_item_data
                )

                destinations.append(destinations_item)

        carried_click_ids = d.pop("carried_click_ids", UNSET)

        note = d.pop("note", UNSET)

        conversion_send_result = cls(
            object_=object_,
            events_received=events_received,
            stored=stored,
            test_code=test_code,
            validate_only=validate_only,
            destinations=destinations,
            carried_click_ids=carried_click_ids,
            note=note,
        )

        conversion_send_result.additional_properties = d
        return conversion_send_result

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
