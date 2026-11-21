from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.conversion_destination_create_event_map import (
        ConversionDestinationCreateEventMap,
    )


T = TypeVar("T", bound="ConversionDestinationCreate")


@_attrs_define
class ConversionDestinationCreate:
    """
    Attributes:
        platform (str): meta, tiktok, linkedin, snapchat, reddit, pinterest, x, microsoft, chatgpt, applovin or amazon.
        label (str | Unset):
        pixel_id (str | Unset):
        ad_account_id (str | Unset):
        advertiser_id (str | Unset):
        event_source_id (str | Unset):
        event_source (str | Unset):
        conversion_id (str | Unset):
        conversion_name (str | Unset):
        event_id (str | Unset):
        pixel_snippet_id (str | Unset):
        api_key (str | Unset):
        amazon_profile_id (str | Unset):
        country_code (str | Unset):
        event_names (list[str] | Unset):
        event_map (ConversionDestinationCreateEventMap | Unset):
    """

    platform: str
    label: str | Unset = UNSET
    pixel_id: str | Unset = UNSET
    ad_account_id: str | Unset = UNSET
    advertiser_id: str | Unset = UNSET
    event_source_id: str | Unset = UNSET
    event_source: str | Unset = UNSET
    conversion_id: str | Unset = UNSET
    conversion_name: str | Unset = UNSET
    event_id: str | Unset = UNSET
    pixel_snippet_id: str | Unset = UNSET
    api_key: str | Unset = UNSET
    amazon_profile_id: str | Unset = UNSET
    country_code: str | Unset = UNSET
    event_names: list[str] | Unset = UNSET
    event_map: ConversionDestinationCreateEventMap | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform

        label = self.label

        pixel_id = self.pixel_id

        ad_account_id = self.ad_account_id

        advertiser_id = self.advertiser_id

        event_source_id = self.event_source_id

        event_source = self.event_source

        conversion_id = self.conversion_id

        conversion_name = self.conversion_name

        event_id = self.event_id

        pixel_snippet_id = self.pixel_snippet_id

        api_key = self.api_key

        amazon_profile_id = self.amazon_profile_id

        country_code = self.country_code

        event_names: list[str] | Unset = UNSET
        if not isinstance(self.event_names, Unset):
            event_names = self.event_names

        event_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_map, Unset):
            event_map = self.event_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if pixel_id is not UNSET:
            field_dict["pixel_id"] = pixel_id
        if ad_account_id is not UNSET:
            field_dict["ad_account_id"] = ad_account_id
        if advertiser_id is not UNSET:
            field_dict["advertiser_id"] = advertiser_id
        if event_source_id is not UNSET:
            field_dict["event_source_id"] = event_source_id
        if event_source is not UNSET:
            field_dict["event_source"] = event_source
        if conversion_id is not UNSET:
            field_dict["conversion_id"] = conversion_id
        if conversion_name is not UNSET:
            field_dict["conversion_name"] = conversion_name
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if pixel_snippet_id is not UNSET:
            field_dict["pixel_snippet_id"] = pixel_snippet_id
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if amazon_profile_id is not UNSET:
            field_dict["amazon_profile_id"] = amazon_profile_id
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if event_names is not UNSET:
            field_dict["event_names"] = event_names
        if event_map is not UNSET:
            field_dict["event_map"] = event_map

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_destination_create_event_map import (
            ConversionDestinationCreateEventMap,
        )  # noqa: PLC0415

        d = dict(src_dict)
        platform = d.pop("platform")

        label = d.pop("label", UNSET)

        pixel_id = d.pop("pixel_id", UNSET)

        ad_account_id = d.pop("ad_account_id", UNSET)

        advertiser_id = d.pop("advertiser_id", UNSET)

        event_source_id = d.pop("event_source_id", UNSET)

        event_source = d.pop("event_source", UNSET)

        conversion_id = d.pop("conversion_id", UNSET)

        conversion_name = d.pop("conversion_name", UNSET)

        event_id = d.pop("event_id", UNSET)

        pixel_snippet_id = d.pop("pixel_snippet_id", UNSET)

        api_key = d.pop("api_key", UNSET)

        amazon_profile_id = d.pop("amazon_profile_id", UNSET)

        country_code = d.pop("country_code", UNSET)

        event_names = cast(list[str], d.pop("event_names", UNSET))

        _event_map = d.pop("event_map", UNSET)
        event_map: ConversionDestinationCreateEventMap | Unset
        if isinstance(_event_map, Unset):
            event_map = UNSET
        else:
            event_map = ConversionDestinationCreateEventMap.from_dict(_event_map)

        conversion_destination_create = cls(
            platform=platform,
            label=label,
            pixel_id=pixel_id,
            ad_account_id=ad_account_id,
            advertiser_id=advertiser_id,
            event_source_id=event_source_id,
            event_source=event_source,
            conversion_id=conversion_id,
            conversion_name=conversion_name,
            event_id=event_id,
            pixel_snippet_id=pixel_snippet_id,
            api_key=api_key,
            amazon_profile_id=amazon_profile_id,
            country_code=country_code,
            event_names=event_names,
            event_map=event_map,
        )

        conversion_destination_create.additional_properties = d
        return conversion_destination_create

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
