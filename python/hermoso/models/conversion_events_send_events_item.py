from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.conversion_events_send_events_item_campaign import (
        ConversionEventsSendEventsItemCampaign,
    )
    from ..models.conversion_events_send_events_item_consent import (
        ConversionEventsSendEventsItemConsent,
    )
    from ..models.conversion_events_send_events_item_items_item import (
        ConversionEventsSendEventsItemItemsItem,
    )
    from ..models.conversion_events_send_events_item_user import (
        ConversionEventsSendEventsItemUser,
    )


T = TypeVar("T", bound="ConversionEventsSendEventsItem")


@_attrs_define
class ConversionEventsSendEventsItem:
    """
    Attributes:
        event_name (str): Purchase, Lead, QualifiedLead, CompleteRegistration, AddToCart, InitiateCheckout, Subscribe,
            StartTrial, ViewContent, PageView … or your own.
        event_id (str): The one dedup key every platform receives.
        event_time (int | Unset): Unix seconds; default now.
        value (float | Unset):
        currency (str | Unset):
        action_source (str | Unset):
        source_url (str | Unset):
        referrer (str | Unset):
        user (ConversionEventsSendEventsItemUser | Unset): email, phone, first_name, last_name, external_id, ip_address,
            user_agent, country, city, state, zip, dob, gender, lead_id, visitor_id, click_ids {gclid, fbc, fbp, ttclid,
            li_fat_id, epik, rdt_cid, twclid, msclkid, sccid, oppref …}. Plain values: hashed per platform on our server.
        items (list[ConversionEventsSendEventsItemItemsItem] | Unset):
        campaign (ConversionEventsSendEventsItemCampaign | Unset):
        consent (ConversionEventsSendEventsItemConsent | Unset):
        limited_data_use (bool | Unset):
    """

    event_name: str
    event_id: str
    event_time: int | Unset = UNSET
    value: float | Unset = UNSET
    currency: str | Unset = UNSET
    action_source: str | Unset = UNSET
    source_url: str | Unset = UNSET
    referrer: str | Unset = UNSET
    user: ConversionEventsSendEventsItemUser | Unset = UNSET
    items: list[ConversionEventsSendEventsItemItemsItem] | Unset = UNSET
    campaign: ConversionEventsSendEventsItemCampaign | Unset = UNSET
    consent: ConversionEventsSendEventsItemConsent | Unset = UNSET
    limited_data_use: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_name = self.event_name

        event_id = self.event_id

        event_time = self.event_time

        value = self.value

        currency = self.currency

        action_source = self.action_source

        source_url = self.source_url

        referrer = self.referrer

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        campaign: dict[str, Any] | Unset = UNSET
        if not isinstance(self.campaign, Unset):
            campaign = self.campaign.to_dict()

        consent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.consent, Unset):
            consent = self.consent.to_dict()

        limited_data_use = self.limited_data_use

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_name": event_name,
                "event_id": event_id,
            }
        )
        if event_time is not UNSET:
            field_dict["event_time"] = event_time
        if value is not UNSET:
            field_dict["value"] = value
        if currency is not UNSET:
            field_dict["currency"] = currency
        if action_source is not UNSET:
            field_dict["action_source"] = action_source
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if referrer is not UNSET:
            field_dict["referrer"] = referrer
        if user is not UNSET:
            field_dict["user"] = user
        if items is not UNSET:
            field_dict["items"] = items
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if consent is not UNSET:
            field_dict["consent"] = consent
        if limited_data_use is not UNSET:
            field_dict["limited_data_use"] = limited_data_use

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_events_send_events_item_campaign import (
            ConversionEventsSendEventsItemCampaign,
        )  # noqa: PLC0415
        from ..models.conversion_events_send_events_item_consent import (
            ConversionEventsSendEventsItemConsent,
        )  # noqa: PLC0415
        from ..models.conversion_events_send_events_item_items_item import (
            ConversionEventsSendEventsItemItemsItem,
        )  # noqa: PLC0415
        from ..models.conversion_events_send_events_item_user import (
            ConversionEventsSendEventsItemUser,
        )  # noqa: PLC0415

        d = dict(src_dict)
        event_name = d.pop("event_name")

        event_id = d.pop("event_id")

        event_time = d.pop("event_time", UNSET)

        value = d.pop("value", UNSET)

        currency = d.pop("currency", UNSET)

        action_source = d.pop("action_source", UNSET)

        source_url = d.pop("source_url", UNSET)

        referrer = d.pop("referrer", UNSET)

        _user = d.pop("user", UNSET)
        user: ConversionEventsSendEventsItemUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ConversionEventsSendEventsItemUser.from_dict(_user)

        _items = d.pop("items", UNSET)
        items: list[ConversionEventsSendEventsItemItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = ConversionEventsSendEventsItemItemsItem.from_dict(
                    items_item_data
                )

                items.append(items_item)

        _campaign = d.pop("campaign", UNSET)
        campaign: ConversionEventsSendEventsItemCampaign | Unset
        if isinstance(_campaign, Unset):
            campaign = UNSET
        else:
            campaign = ConversionEventsSendEventsItemCampaign.from_dict(_campaign)

        _consent = d.pop("consent", UNSET)
        consent: ConversionEventsSendEventsItemConsent | Unset
        if isinstance(_consent, Unset):
            consent = UNSET
        else:
            consent = ConversionEventsSendEventsItemConsent.from_dict(_consent)

        limited_data_use = d.pop("limited_data_use", UNSET)

        conversion_events_send_events_item = cls(
            event_name=event_name,
            event_id=event_id,
            event_time=event_time,
            value=value,
            currency=currency,
            action_source=action_source,
            source_url=source_url,
            referrer=referrer,
            user=user,
            items=items,
            campaign=campaign,
            consent=consent,
            limited_data_use=limited_data_use,
        )

        conversion_events_send_events_item.additional_properties = d
        return conversion_events_send_events_item

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
