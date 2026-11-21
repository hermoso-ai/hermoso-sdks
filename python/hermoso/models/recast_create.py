from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.recast_person import RecastPerson


T = TypeVar("T", bound="RecastCreate")


@_attrs_define
class RecastCreate:
    """
    Attributes:
        video (str): The video the person goes into: a public https link to a video file, a TikTok, Reel, Facebook, X or
            YouTube post link (read once, through one lookup), or a Hermoso file URL (`POST /v1/media`, `GET /v1/library`, a
            job `url`).
        person (RecastPerson): Who goes into the video. Send exactly ONE of the three.
        voice (str | Unset): Optional. A NEW voice for the new person, keeping the original words and timing: `match` (a
            voice that fits them), `female`, `male`, or a stock voice name (Aria, Sarah, Charlotte, George, Brian, Charlie).
            Omit to keep the video's own sound. Never the original speaker's voice or a cloned one.
        language (str | Unset): Optional. The new person speaks this language instead (for example `Spanish`), with the
            mouth lip-synced to the new words. `voice` defaults to `match`.
        start (float | Unset): Optional. Where the recast window starts, in seconds. Default 0.
        end (float | Unset): Optional. Where it ends, in seconds. Default: the end of the video, up to 60 seconds after
            `start`. At least 3 seconds.
        instruction (str | Unset): Optional, in your own words: who in the video is replaced when there are several
            people ("the man on the left").
        dry_run (bool | Unset): true = return the exact price and the plan, and run nothing.
        callback_url (str | Unset): Optional https URL to POST the finished job to (the same as the `X-Hermoso-Callback-
            Url` header).
    """

    video: str
    person: RecastPerson
    voice: str | Unset = UNSET
    language: str | Unset = UNSET
    start: float | Unset = UNSET
    end: float | Unset = UNSET
    instruction: str | Unset = UNSET
    dry_run: bool | Unset = UNSET
    callback_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        video = self.video

        person = self.person.to_dict()

        voice = self.voice

        language = self.language

        start = self.start

        end = self.end

        instruction = self.instruction

        dry_run = self.dry_run

        callback_url = self.callback_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "video": video,
                "person": person,
            }
        )
        if voice is not UNSET:
            field_dict["voice"] = voice
        if language is not UNSET:
            field_dict["language"] = language
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if instruction is not UNSET:
            field_dict["instruction"] = instruction
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if callback_url is not UNSET:
            field_dict["callback_url"] = callback_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recast_person import RecastPerson  # noqa: PLC0415

        d = dict(src_dict)
        video = d.pop("video")

        person = RecastPerson.from_dict(d.pop("person"))

        voice = d.pop("voice", UNSET)

        language = d.pop("language", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        instruction = d.pop("instruction", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        callback_url = d.pop("callback_url", UNSET)

        recast_create = cls(
            video=video,
            person=person,
            voice=voice,
            language=language,
            start=start,
            end=end,
            instruction=instruction,
            dry_run=dry_run,
            callback_url=callback_url,
        )

        recast_create.additional_properties = d
        return recast_create

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
