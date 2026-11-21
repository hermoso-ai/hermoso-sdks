from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="RecastVoiceType0")


@_attrs_define
class RecastVoiceType0:
    """
    Attributes:
        voice (str | Unset):
        language (None | str | Unset):
        lip_synced (bool | Unset):
    """

    voice: str | Unset = UNSET
    language: None | str | Unset = UNSET
    lip_synced: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        voice = self.voice

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        lip_synced = self.lip_synced

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if voice is not UNSET:
            field_dict["voice"] = voice
        if language is not UNSET:
            field_dict["language"] = language
        if lip_synced is not UNSET:
            field_dict["lip_synced"] = lip_synced

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        voice = d.pop("voice", UNSET)

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        lip_synced = d.pop("lip_synced", UNSET)

        recast_voice_type_0 = cls(
            voice=voice,
            language=language,
            lip_synced=lip_synced,
        )

        recast_voice_type_0.additional_properties = d
        return recast_voice_type_0

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
