from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.hermoso_tag_update_action import HermosoTagUpdateAction
from ..models.hermoso_tag_update_consent_default import HermosoTagUpdateConsentDefault
from typing import cast

if TYPE_CHECKING:
    from ..models.hermoso_tag_update_auto_track import HermosoTagUpdateAutoTrack
    from ..models.hermoso_tag_update_conversions import HermosoTagUpdateConversions


T = TypeVar("T", bound="HermosoTagUpdate")


@_attrs_define
class HermosoTagUpdate:
    """
    Attributes:
        action (HermosoTagUpdateAction | Unset):
        auto_track (HermosoTagUpdateAutoTrack | Unset):
        link_domains (list[str] | Unset):
        signing_secret (str | Unset):
        consent_default (HermosoTagUpdateConsentDefault | Unset):
        wait_for_consent (bool | Unset):
        honor_gpc (bool | Unset):
        honor_dnt (bool | Unset):
        forward (bool | Unset):
        forward_events (list[str] | None | Unset):
        allowed_domains (list[str] | Unset):
        spa (bool | Unset):
        test_mode (str | Unset):
        conversions (HermosoTagUpdateConversions | Unset):
        replace_conversions (bool | Unset):
        url (str | Unset):
        render (bool | Unset):
    """

    action: HermosoTagUpdateAction | Unset = UNSET
    auto_track: HermosoTagUpdateAutoTrack | Unset = UNSET
    link_domains: list[str] | Unset = UNSET
    signing_secret: str | Unset = UNSET
    consent_default: HermosoTagUpdateConsentDefault | Unset = UNSET
    wait_for_consent: bool | Unset = UNSET
    honor_gpc: bool | Unset = UNSET
    honor_dnt: bool | Unset = UNSET
    forward: bool | Unset = UNSET
    forward_events: list[str] | None | Unset = UNSET
    allowed_domains: list[str] | Unset = UNSET
    spa: bool | Unset = UNSET
    test_mode: str | Unset = UNSET
    conversions: HermosoTagUpdateConversions | Unset = UNSET
    replace_conversions: bool | Unset = UNSET
    url: str | Unset = UNSET
    render: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        auto_track: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auto_track, Unset):
            auto_track = self.auto_track.to_dict()

        link_domains: list[str] | Unset = UNSET
        if not isinstance(self.link_domains, Unset):
            link_domains = self.link_domains

        signing_secret = self.signing_secret

        consent_default: str | Unset = UNSET
        if not isinstance(self.consent_default, Unset):
            consent_default = self.consent_default.value

        wait_for_consent = self.wait_for_consent

        honor_gpc = self.honor_gpc

        honor_dnt = self.honor_dnt

        forward = self.forward

        forward_events: list[str] | None | Unset
        if isinstance(self.forward_events, Unset):
            forward_events = UNSET
        elif isinstance(self.forward_events, list):
            forward_events = self.forward_events

        else:
            forward_events = self.forward_events

        allowed_domains: list[str] | Unset = UNSET
        if not isinstance(self.allowed_domains, Unset):
            allowed_domains = self.allowed_domains

        spa = self.spa

        test_mode = self.test_mode

        conversions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conversions, Unset):
            conversions = self.conversions.to_dict()

        replace_conversions = self.replace_conversions

        url = self.url

        render = self.render

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if auto_track is not UNSET:
            field_dict["auto_track"] = auto_track
        if link_domains is not UNSET:
            field_dict["link_domains"] = link_domains
        if signing_secret is not UNSET:
            field_dict["signing_secret"] = signing_secret
        if consent_default is not UNSET:
            field_dict["consent_default"] = consent_default
        if wait_for_consent is not UNSET:
            field_dict["wait_for_consent"] = wait_for_consent
        if honor_gpc is not UNSET:
            field_dict["honor_gpc"] = honor_gpc
        if honor_dnt is not UNSET:
            field_dict["honor_dnt"] = honor_dnt
        if forward is not UNSET:
            field_dict["forward"] = forward
        if forward_events is not UNSET:
            field_dict["forward_events"] = forward_events
        if allowed_domains is not UNSET:
            field_dict["allowed_domains"] = allowed_domains
        if spa is not UNSET:
            field_dict["spa"] = spa
        if test_mode is not UNSET:
            field_dict["test_mode"] = test_mode
        if conversions is not UNSET:
            field_dict["conversions"] = conversions
        if replace_conversions is not UNSET:
            field_dict["replace_conversions"] = replace_conversions
        if url is not UNSET:
            field_dict["url"] = url
        if render is not UNSET:
            field_dict["render"] = render

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hermoso_tag_update_auto_track import HermosoTagUpdateAutoTrack  # noqa: PLC0415
        from ..models.hermoso_tag_update_conversions import HermosoTagUpdateConversions  # noqa: PLC0415

        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: HermosoTagUpdateAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = HermosoTagUpdateAction(_action)

        _auto_track = d.pop("auto_track", UNSET)
        auto_track: HermosoTagUpdateAutoTrack | Unset
        if isinstance(_auto_track, Unset):
            auto_track = UNSET
        else:
            auto_track = HermosoTagUpdateAutoTrack.from_dict(_auto_track)

        link_domains = cast(list[str], d.pop("link_domains", UNSET))

        signing_secret = d.pop("signing_secret", UNSET)

        _consent_default = d.pop("consent_default", UNSET)
        consent_default: HermosoTagUpdateConsentDefault | Unset
        if isinstance(_consent_default, Unset):
            consent_default = UNSET
        else:
            consent_default = HermosoTagUpdateConsentDefault(_consent_default)

        wait_for_consent = d.pop("wait_for_consent", UNSET)

        honor_gpc = d.pop("honor_gpc", UNSET)

        honor_dnt = d.pop("honor_dnt", UNSET)

        forward = d.pop("forward", UNSET)

        def _parse_forward_events(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                forward_events_type_0 = cast(list[str], data)

                return forward_events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        forward_events = _parse_forward_events(d.pop("forward_events", UNSET))

        allowed_domains = cast(list[str], d.pop("allowed_domains", UNSET))

        spa = d.pop("spa", UNSET)

        test_mode = d.pop("test_mode", UNSET)

        _conversions = d.pop("conversions", UNSET)
        conversions: HermosoTagUpdateConversions | Unset
        if isinstance(_conversions, Unset):
            conversions = UNSET
        else:
            conversions = HermosoTagUpdateConversions.from_dict(_conversions)

        replace_conversions = d.pop("replace_conversions", UNSET)

        url = d.pop("url", UNSET)

        render = d.pop("render", UNSET)

        hermoso_tag_update = cls(
            action=action,
            auto_track=auto_track,
            link_domains=link_domains,
            signing_secret=signing_secret,
            consent_default=consent_default,
            wait_for_consent=wait_for_consent,
            honor_gpc=honor_gpc,
            honor_dnt=honor_dnt,
            forward=forward,
            forward_events=forward_events,
            allowed_domains=allowed_domains,
            spa=spa,
            test_mode=test_mode,
            conversions=conversions,
            replace_conversions=replace_conversions,
            url=url,
            render=render,
        )

        hermoso_tag_update.additional_properties = d
        return hermoso_tag_update

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
