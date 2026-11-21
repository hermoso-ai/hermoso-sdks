from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="ConversionEventsSendEventsItemUser")


@_attrs_define
class ConversionEventsSendEventsItemUser:
    """email, phone, first_name, last_name, external_id, ip_address, user_agent, country, city, state, zip, dob, gender,
    lead_id, visitor_id, click_ids {gclid, fbc, fbp, ttclid, li_fat_id, epik, rdt_cid, twclid, msclkid, sccid, oppref
    …}. Plain values: hashed per platform on our server.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversion_events_send_events_item_user = cls()

        conversion_events_send_events_item_user.additional_properties = d
        return conversion_events_send_events_item_user

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
