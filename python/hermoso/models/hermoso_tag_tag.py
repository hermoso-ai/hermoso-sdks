from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.hermoso_tag_tag_installs_item import HermosoTagTagInstallsItem
    from ..models.hermoso_tag_tag_settings import HermosoTagTagSettings
    from ..models.hermoso_tag_tag_status import HermosoTagTagStatus


T = TypeVar("T", bound="HermosoTagTag")


@_attrs_define
class HermosoTagTag:
    """
    Attributes:
        tag_id (str | Unset):
        snippet (str | Unset):
        script_url (str | Unset):
        settings (HermosoTagTagSettings | Unset):
        status (HermosoTagTagStatus | Unset):
        installs (list[HermosoTagTagInstallsItem] | Unset):
    """

    tag_id: str | Unset = UNSET
    snippet: str | Unset = UNSET
    script_url: str | Unset = UNSET
    settings: HermosoTagTagSettings | Unset = UNSET
    status: HermosoTagTagStatus | Unset = UNSET
    installs: list[HermosoTagTagInstallsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_id = self.tag_id

        snippet = self.snippet

        script_url = self.script_url

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        installs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.installs, Unset):
            installs = []
            for installs_item_data in self.installs:
                installs_item = installs_item_data.to_dict()
                installs.append(installs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag_id is not UNSET:
            field_dict["tag_id"] = tag_id
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if script_url is not UNSET:
            field_dict["script_url"] = script_url
        if settings is not UNSET:
            field_dict["settings"] = settings
        if status is not UNSET:
            field_dict["status"] = status
        if installs is not UNSET:
            field_dict["installs"] = installs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hermoso_tag_tag_installs_item import HermosoTagTagInstallsItem  # noqa: PLC0415
        from ..models.hermoso_tag_tag_settings import HermosoTagTagSettings  # noqa: PLC0415
        from ..models.hermoso_tag_tag_status import HermosoTagTagStatus  # noqa: PLC0415

        d = dict(src_dict)
        tag_id = d.pop("tag_id", UNSET)

        snippet = d.pop("snippet", UNSET)

        script_url = d.pop("script_url", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: HermosoTagTagSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = HermosoTagTagSettings.from_dict(_settings)

        _status = d.pop("status", UNSET)
        status: HermosoTagTagStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = HermosoTagTagStatus.from_dict(_status)

        _installs = d.pop("installs", UNSET)
        installs: list[HermosoTagTagInstallsItem] | Unset = UNSET
        if _installs is not UNSET:
            installs = []
            for installs_item_data in _installs:
                installs_item = HermosoTagTagInstallsItem.from_dict(installs_item_data)

                installs.append(installs_item)

        hermoso_tag_tag = cls(
            tag_id=tag_id,
            snippet=snippet,
            script_url=script_url,
            settings=settings,
            status=status,
            installs=installs,
        )

        hermoso_tag_tag.additional_properties = d
        return hermoso_tag_tag

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
