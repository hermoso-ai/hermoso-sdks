from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.campaign_results_upload_rows_item_values import (
        CampaignResultsUploadRowsItemValues,
    )


T = TypeVar("T", bound="CampaignResultsUploadRowsItem")


@_attrs_define
class CampaignResultsUploadRowsItem:
    """
    Attributes:
        date (str):
        values (CampaignResultsUploadRowsItemValues):
        campaign_id (str | Unset):
        utm_campaign (str | Unset):
        campaign_name (str | Unset):
        ad_account_id (str | Unset):
        platform (str | Unset):
        currency (str | Unset):
    """

    date: str
    values: CampaignResultsUploadRowsItemValues
    campaign_id: str | Unset = UNSET
    utm_campaign: str | Unset = UNSET
    campaign_name: str | Unset = UNSET
    ad_account_id: str | Unset = UNSET
    platform: str | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        values = self.values.to_dict()

        campaign_id = self.campaign_id

        utm_campaign = self.utm_campaign

        campaign_name = self.campaign_name

        ad_account_id = self.ad_account_id

        platform = self.platform

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "values": values,
            }
        )
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if utm_campaign is not UNSET:
            field_dict["utm_campaign"] = utm_campaign
        if campaign_name is not UNSET:
            field_dict["campaign_name"] = campaign_name
        if ad_account_id is not UNSET:
            field_dict["ad_account_id"] = ad_account_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.campaign_results_upload_rows_item_values import (
            CampaignResultsUploadRowsItemValues,
        )  # noqa: PLC0415

        d = dict(src_dict)
        date = d.pop("date")

        values = CampaignResultsUploadRowsItemValues.from_dict(d.pop("values"))

        campaign_id = d.pop("campaign_id", UNSET)

        utm_campaign = d.pop("utm_campaign", UNSET)

        campaign_name = d.pop("campaign_name", UNSET)

        ad_account_id = d.pop("ad_account_id", UNSET)

        platform = d.pop("platform", UNSET)

        currency = d.pop("currency", UNSET)

        campaign_results_upload_rows_item = cls(
            date=date,
            values=values,
            campaign_id=campaign_id,
            utm_campaign=utm_campaign,
            campaign_name=campaign_name,
            ad_account_id=ad_account_id,
            platform=platform,
            currency=currency,
        )

        campaign_results_upload_rows_item.additional_properties = d
        return campaign_results_upload_rows_item

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
