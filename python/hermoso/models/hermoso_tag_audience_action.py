from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.hermoso_tag_audience_action_action import HermosoTagAudienceActionAction
from ..models.hermoso_tag_audience_action_platform import (
    HermosoTagAudienceActionPlatform,
)
from typing import cast


T = TypeVar("T", bound="HermosoTagAudienceAction")


@_attrs_define
class HermosoTagAudienceAction:
    """
    Attributes:
        action (HermosoTagAudienceActionAction | Unset):
        segment_id (str | Unset):
        name (str | Unset):
        visited (list[str] | Unset):
        events (list[str] | Unset):
        not_events (list[str] | Unset):
        within_days (int | Unset):
        platform (HermosoTagAudienceActionPlatform | Unset):
        audience_id (str | Unset):
        audience_name (str | Unset):
        ad_account_id (str | Unset):
        customer_id (str | Unset):
        accept_terms (bool | Unset):
        confirm (bool | Unset):
    """

    action: HermosoTagAudienceActionAction | Unset = UNSET
    segment_id: str | Unset = UNSET
    name: str | Unset = UNSET
    visited: list[str] | Unset = UNSET
    events: list[str] | Unset = UNSET
    not_events: list[str] | Unset = UNSET
    within_days: int | Unset = UNSET
    platform: HermosoTagAudienceActionPlatform | Unset = UNSET
    audience_id: str | Unset = UNSET
    audience_name: str | Unset = UNSET
    ad_account_id: str | Unset = UNSET
    customer_id: str | Unset = UNSET
    accept_terms: bool | Unset = UNSET
    confirm: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        segment_id = self.segment_id

        name = self.name

        visited: list[str] | Unset = UNSET
        if not isinstance(self.visited, Unset):
            visited = self.visited

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        not_events: list[str] | Unset = UNSET
        if not isinstance(self.not_events, Unset):
            not_events = self.not_events

        within_days = self.within_days

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        audience_id = self.audience_id

        audience_name = self.audience_name

        ad_account_id = self.ad_account_id

        customer_id = self.customer_id

        accept_terms = self.accept_terms

        confirm = self.confirm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if segment_id is not UNSET:
            field_dict["segment_id"] = segment_id
        if name is not UNSET:
            field_dict["name"] = name
        if visited is not UNSET:
            field_dict["visited"] = visited
        if events is not UNSET:
            field_dict["events"] = events
        if not_events is not UNSET:
            field_dict["not_events"] = not_events
        if within_days is not UNSET:
            field_dict["within_days"] = within_days
        if platform is not UNSET:
            field_dict["platform"] = platform
        if audience_id is not UNSET:
            field_dict["audience_id"] = audience_id
        if audience_name is not UNSET:
            field_dict["audience_name"] = audience_name
        if ad_account_id is not UNSET:
            field_dict["ad_account_id"] = ad_account_id
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if accept_terms is not UNSET:
            field_dict["accept_terms"] = accept_terms
        if confirm is not UNSET:
            field_dict["confirm"] = confirm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: HermosoTagAudienceActionAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = HermosoTagAudienceActionAction(_action)

        segment_id = d.pop("segment_id", UNSET)

        name = d.pop("name", UNSET)

        visited = cast(list[str], d.pop("visited", UNSET))

        events = cast(list[str], d.pop("events", UNSET))

        not_events = cast(list[str], d.pop("not_events", UNSET))

        within_days = d.pop("within_days", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: HermosoTagAudienceActionPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = HermosoTagAudienceActionPlatform(_platform)

        audience_id = d.pop("audience_id", UNSET)

        audience_name = d.pop("audience_name", UNSET)

        ad_account_id = d.pop("ad_account_id", UNSET)

        customer_id = d.pop("customer_id", UNSET)

        accept_terms = d.pop("accept_terms", UNSET)

        confirm = d.pop("confirm", UNSET)

        hermoso_tag_audience_action = cls(
            action=action,
            segment_id=segment_id,
            name=name,
            visited=visited,
            events=events,
            not_events=not_events,
            within_days=within_days,
            platform=platform,
            audience_id=audience_id,
            audience_name=audience_name,
            ad_account_id=ad_account_id,
            customer_id=customer_id,
            accept_terms=accept_terms,
            confirm=confirm,
        )

        hermoso_tag_audience_action.additional_properties = d
        return hermoso_tag_audience_action

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
