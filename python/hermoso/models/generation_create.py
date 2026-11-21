from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.generation_create_background import GenerationCreateBackground
from ..models.generation_create_complexity import GenerationCreateComplexity
from ..models.generation_create_format import GenerationCreateFormat
from ..models.generation_create_type import GenerationCreateType
from typing import cast


T = TypeVar("T", bound="GenerationCreate")


@_attrs_define
class GenerationCreate:
    """
    Attributes:
        type_ (GenerationCreateType): What to make. This enum MAY GROW.
        prompt (str): What the ad should show, in plain words.
        model (str | Unset): A model id from the live catalog (the `hermoso_capabilities` tool lists them with prices).
            Omit to let Hermoso pick; the quote then prices the model the server would pick.
        aspect_ratio (str | Unset): e.g. 1:1, 4:5, 9:16, 16:9. Each model lists the ratios it renders.
        image_size (str | Unset): Image only: a size tier the model lists (for example 1K, 2K).
        duration_seconds (int | Unset): Video only: one of the chosen model’s listed lengths.
        ref_image (str | Unset): Video only: a Hermoso-hosted image to animate (image-to-video).
        ref_images (list[str] | Unset): Image only: up to 3 Hermoso-hosted images (a `POST /v1/media` or Library `url`)
            the render uses as its reference. When present the brand’s product photos are not attached for you; the quote
            prices exactly this.
        use_brand (bool | Unset): Image only, default true: attach the profile’s own product photos (and its logo when
            the prompt asks for one) so the render shows the real product. The quote prices exactly what this attaches.
        format_ (GenerationCreateFormat | Unset): Image only, default png. gif = a short looping animated GIF, svg = an
            editable vector. Both render on gpt-image-2.6 (default) or gpt-image-2.6-flare from the prompt alone: no
            ref_images, and the profile’s photos are not attached.
        frames (int | Unset): format gif only: frames in the loop (default 9).
        frame_ms (int | Unset): format gif only: milliseconds per frame, rounded to 10 (default 200).
        complexity (GenerationCreateComplexity | Unset): gpt-image-2.6 models only: how much the model plans before
            drawing (default high). No separate charge.
        background (GenerationCreateBackground | Unset): Image only: transparent = a PNG with no background (an alpha
            channel), for a cut-out product, icon or sticker. Renders on gpt-image-2.6 (default) or gpt-image-2.6-flare from
            the prompt alone: no ref_images, and the profile’s photos are not attached. Priced like a plain image of that
            size (the quote shows it).
    """

    type_: GenerationCreateType
    prompt: str
    model: str | Unset = UNSET
    aspect_ratio: str | Unset = UNSET
    image_size: str | Unset = UNSET
    duration_seconds: int | Unset = UNSET
    ref_image: str | Unset = UNSET
    ref_images: list[str] | Unset = UNSET
    use_brand: bool | Unset = UNSET
    format_: GenerationCreateFormat | Unset = UNSET
    frames: int | Unset = UNSET
    frame_ms: int | Unset = UNSET
    complexity: GenerationCreateComplexity | Unset = UNSET
    background: GenerationCreateBackground | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        prompt = self.prompt

        model = self.model

        aspect_ratio = self.aspect_ratio

        image_size = self.image_size

        duration_seconds = self.duration_seconds

        ref_image = self.ref_image

        ref_images: list[str] | Unset = UNSET
        if not isinstance(self.ref_images, Unset):
            ref_images = self.ref_images

        use_brand = self.use_brand

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        frames = self.frames

        frame_ms = self.frame_ms

        complexity: str | Unset = UNSET
        if not isinstance(self.complexity, Unset):
            complexity = self.complexity.value

        background: str | Unset = UNSET
        if not isinstance(self.background, Unset):
            background = self.background.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "prompt": prompt,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if aspect_ratio is not UNSET:
            field_dict["aspect_ratio"] = aspect_ratio
        if image_size is not UNSET:
            field_dict["image_size"] = image_size
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if ref_image is not UNSET:
            field_dict["ref_image"] = ref_image
        if ref_images is not UNSET:
            field_dict["ref_images"] = ref_images
        if use_brand is not UNSET:
            field_dict["use_brand"] = use_brand
        if format_ is not UNSET:
            field_dict["format"] = format_
        if frames is not UNSET:
            field_dict["frames"] = frames
        if frame_ms is not UNSET:
            field_dict["frame_ms"] = frame_ms
        if complexity is not UNSET:
            field_dict["complexity"] = complexity
        if background is not UNSET:
            field_dict["background"] = background

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = GenerationCreateType(d.pop("type"))

        prompt = d.pop("prompt")

        model = d.pop("model", UNSET)

        aspect_ratio = d.pop("aspect_ratio", UNSET)

        image_size = d.pop("image_size", UNSET)

        duration_seconds = d.pop("duration_seconds", UNSET)

        ref_image = d.pop("ref_image", UNSET)

        ref_images = cast(list[str], d.pop("ref_images", UNSET))

        use_brand = d.pop("use_brand", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: GenerationCreateFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = GenerationCreateFormat(_format_)

        frames = d.pop("frames", UNSET)

        frame_ms = d.pop("frame_ms", UNSET)

        _complexity = d.pop("complexity", UNSET)
        complexity: GenerationCreateComplexity | Unset
        if isinstance(_complexity, Unset):
            complexity = UNSET
        else:
            complexity = GenerationCreateComplexity(_complexity)

        _background = d.pop("background", UNSET)
        background: GenerationCreateBackground | Unset
        if isinstance(_background, Unset):
            background = UNSET
        else:
            background = GenerationCreateBackground(_background)

        generation_create = cls(
            type_=type_,
            prompt=prompt,
            model=model,
            aspect_ratio=aspect_ratio,
            image_size=image_size,
            duration_seconds=duration_seconds,
            ref_image=ref_image,
            ref_images=ref_images,
            use_brand=use_brand,
            format_=format_,
            frames=frames,
            frame_ms=frame_ms,
            complexity=complexity,
            background=background,
        )

        generation_create.additional_properties = d
        return generation_create

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
