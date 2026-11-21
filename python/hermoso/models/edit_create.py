from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.edit_create_lighting import EditCreateLighting


T = TypeVar("T", bound="EditCreate")


@_attrs_define
class EditCreate:
    """
    Attributes:
        video (str): The clip to edit: a public https link to a video file or a social post, or a Hermoso file URL. 3 to
            15 seconds.
        instruction (str): The ONE change, in plain words: "change only the mug to red", "swap the bottle for our
            product", "make it nighttime".
        reference (str | Unset): Optional image (https or a Hermoso file URL) that anchors the material of what changes:
            a fabric, a finish, a colour swatch, the real product. Only its surface is used, never its framing or light.
        keep_audio (bool | Unset): Default true: keep the clip's sound. false = silent.
        lighting (EditCreateLighting | Unset): Default auto: keep the light unless the change needs new light (night, a
            lamp). preserve or relight forces it.
        preview_first_frame (bool | Unset): true = edit ONE still of the clip first and return it with the clip's price.
            Nothing else runs.
        preview_still (str | Unset): The `preview.still_url` a preview returned: the clip is then rendered so the change
            looks the way it does in that still.
        preview_at (float | Unset): Which second to preview (default the first frame). Send the same value with
            `preview_still`.
        dry_run (bool | Unset): true = return the exact price, and run nothing.
        callback_url (str | Unset): Optional https URL to POST the finished job to (the same as the `X-Hermoso-Callback-
            Url` header).
    """

    video: str
    instruction: str
    reference: str | Unset = UNSET
    keep_audio: bool | Unset = UNSET
    lighting: EditCreateLighting | Unset = UNSET
    preview_first_frame: bool | Unset = UNSET
    preview_still: str | Unset = UNSET
    preview_at: float | Unset = UNSET
    dry_run: bool | Unset = UNSET
    callback_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        video = self.video

        instruction = self.instruction

        reference = self.reference

        keep_audio = self.keep_audio

        lighting: str | Unset = UNSET
        if not isinstance(self.lighting, Unset):
            lighting = self.lighting.value

        preview_first_frame = self.preview_first_frame

        preview_still = self.preview_still

        preview_at = self.preview_at

        dry_run = self.dry_run

        callback_url = self.callback_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "video": video,
                "instruction": instruction,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference
        if keep_audio is not UNSET:
            field_dict["keep_audio"] = keep_audio
        if lighting is not UNSET:
            field_dict["lighting"] = lighting
        if preview_first_frame is not UNSET:
            field_dict["preview_first_frame"] = preview_first_frame
        if preview_still is not UNSET:
            field_dict["preview_still"] = preview_still
        if preview_at is not UNSET:
            field_dict["preview_at"] = preview_at
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if callback_url is not UNSET:
            field_dict["callback_url"] = callback_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        video = d.pop("video")

        instruction = d.pop("instruction")

        reference = d.pop("reference", UNSET)

        keep_audio = d.pop("keep_audio", UNSET)

        _lighting = d.pop("lighting", UNSET)
        lighting: EditCreateLighting | Unset
        if isinstance(_lighting, Unset):
            lighting = UNSET
        else:
            lighting = EditCreateLighting(_lighting)

        preview_first_frame = d.pop("preview_first_frame", UNSET)

        preview_still = d.pop("preview_still", UNSET)

        preview_at = d.pop("preview_at", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        callback_url = d.pop("callback_url", UNSET)

        edit_create = cls(
            video=video,
            instruction=instruction,
            reference=reference,
            keep_audio=keep_audio,
            lighting=lighting,
            preview_first_frame=preview_first_frame,
            preview_still=preview_still,
            preview_at=preview_at,
            dry_run=dry_run,
            callback_url=callback_url,
        )

        edit_create.additional_properties = d
        return edit_create

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
