from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.model_object import ModelObject
from typing import cast

if TYPE_CHECKING:
    from ..models.model_credits_by_duration_type_0 import ModelCreditsByDurationType0
    from ..models.model_credits_by_size_type_0 import ModelCreditsBySizeType0


T = TypeVar("T", bound="Model")


@_attrs_define
class Model:
    """
    Attributes:
        object_ (ModelObject | Unset):
        id (str | Unset): Pass as `model` to POST /v1/generations.
        type_ (str | Unset): image or video.
        label (str | Unset):
        featured (bool | Unset): One of the models Hermoso recommends.
        default (bool | Unset): The model Hermoso marks as its best-quality pick for this type. It is NOT necessarily
            the model a request without `model` runs: that depends on the request (an on-brand image is routed to a model
            that can composite your brand’s photos). POST /v1/generations/quote with your exact body answers `label` with
            the model it would actually run, and its price.
        aspect_ratios (list[str] | Unset):
        image_sizes (list[str] | None | Unset):
        durations (list[int] | None | Unset): Video: the lengths, in seconds, this model renders in one pass.
        credits_ (float | None | Unset): Image: the list price of one render. Video: null (see credits_by_duration).
        credits_by_size (ModelCreditsBySizeType0 | None | Unset):
        credits_by_duration (ModelCreditsByDurationType0 | None | Unset):
        audio (bool | None | Unset): Video: renders its own sound.
        needs_reference (bool | Unset): Only works on a picture or clip you supply.
    """

    object_: ModelObject | Unset = UNSET
    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    label: str | Unset = UNSET
    featured: bool | Unset = UNSET
    default: bool | Unset = UNSET
    aspect_ratios: list[str] | Unset = UNSET
    image_sizes: list[str] | None | Unset = UNSET
    durations: list[int] | None | Unset = UNSET
    credits_: float | None | Unset = UNSET
    credits_by_size: ModelCreditsBySizeType0 | None | Unset = UNSET
    credits_by_duration: ModelCreditsByDurationType0 | None | Unset = UNSET
    audio: bool | None | Unset = UNSET
    needs_reference: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_credits_by_duration_type_0 import (
            ModelCreditsByDurationType0,
        )  # noqa: PLC0415
        from ..models.model_credits_by_size_type_0 import ModelCreditsBySizeType0  # noqa: PLC0415

        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        type_ = self.type_

        label = self.label

        featured = self.featured

        default = self.default

        aspect_ratios: list[str] | Unset = UNSET
        if not isinstance(self.aspect_ratios, Unset):
            aspect_ratios = self.aspect_ratios

        image_sizes: list[str] | None | Unset
        if isinstance(self.image_sizes, Unset):
            image_sizes = UNSET
        elif isinstance(self.image_sizes, list):
            image_sizes = self.image_sizes

        else:
            image_sizes = self.image_sizes

        durations: list[int] | None | Unset
        if isinstance(self.durations, Unset):
            durations = UNSET
        elif isinstance(self.durations, list):
            durations = self.durations

        else:
            durations = self.durations

        credits_: float | None | Unset
        if isinstance(self.credits_, Unset):
            credits_ = UNSET
        else:
            credits_ = self.credits_

        credits_by_size: dict[str, Any] | None | Unset
        if isinstance(self.credits_by_size, Unset):
            credits_by_size = UNSET
        elif isinstance(self.credits_by_size, ModelCreditsBySizeType0):
            credits_by_size = self.credits_by_size.to_dict()
        else:
            credits_by_size = self.credits_by_size

        credits_by_duration: dict[str, Any] | None | Unset
        if isinstance(self.credits_by_duration, Unset):
            credits_by_duration = UNSET
        elif isinstance(self.credits_by_duration, ModelCreditsByDurationType0):
            credits_by_duration = self.credits_by_duration.to_dict()
        else:
            credits_by_duration = self.credits_by_duration

        audio: bool | None | Unset
        if isinstance(self.audio, Unset):
            audio = UNSET
        else:
            audio = self.audio

        needs_reference = self.needs_reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if label is not UNSET:
            field_dict["label"] = label
        if featured is not UNSET:
            field_dict["featured"] = featured
        if default is not UNSET:
            field_dict["default"] = default
        if aspect_ratios is not UNSET:
            field_dict["aspect_ratios"] = aspect_ratios
        if image_sizes is not UNSET:
            field_dict["image_sizes"] = image_sizes
        if durations is not UNSET:
            field_dict["durations"] = durations
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if credits_by_size is not UNSET:
            field_dict["credits_by_size"] = credits_by_size
        if credits_by_duration is not UNSET:
            field_dict["credits_by_duration"] = credits_by_duration
        if audio is not UNSET:
            field_dict["audio"] = audio
        if needs_reference is not UNSET:
            field_dict["needs_reference"] = needs_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_credits_by_duration_type_0 import (
            ModelCreditsByDurationType0,
        )  # noqa: PLC0415
        from ..models.model_credits_by_size_type_0 import ModelCreditsBySizeType0  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ModelObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ModelObject(_object_)

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        label = d.pop("label", UNSET)

        featured = d.pop("featured", UNSET)

        default = d.pop("default", UNSET)

        aspect_ratios = cast(list[str], d.pop("aspect_ratios", UNSET))

        def _parse_image_sizes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_sizes_type_0 = cast(list[str], data)

                return image_sizes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        image_sizes = _parse_image_sizes(d.pop("image_sizes", UNSET))

        def _parse_durations(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                durations_type_0 = cast(list[int], data)

                return durations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        durations = _parse_durations(d.pop("durations", UNSET))

        def _parse_credits_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        credits_ = _parse_credits_(d.pop("credits", UNSET))

        def _parse_credits_by_size(
            data: object,
        ) -> ModelCreditsBySizeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credits_by_size_type_0 = ModelCreditsBySizeType0.from_dict(data)

                return credits_by_size_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelCreditsBySizeType0 | None | Unset, data)

        credits_by_size = _parse_credits_by_size(d.pop("credits_by_size", UNSET))

        def _parse_credits_by_duration(
            data: object,
        ) -> ModelCreditsByDurationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credits_by_duration_type_0 = ModelCreditsByDurationType0.from_dict(data)

                return credits_by_duration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelCreditsByDurationType0 | None | Unset, data)

        credits_by_duration = _parse_credits_by_duration(
            d.pop("credits_by_duration", UNSET)
        )

        def _parse_audio(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        audio = _parse_audio(d.pop("audio", UNSET))

        needs_reference = d.pop("needs_reference", UNSET)

        model = cls(
            object_=object_,
            id=id,
            type_=type_,
            label=label,
            featured=featured,
            default=default,
            aspect_ratios=aspect_ratios,
            image_sizes=image_sizes,
            durations=durations,
            credits_=credits_,
            credits_by_size=credits_by_size,
            credits_by_duration=credits_by_duration,
            audio=audio,
            needs_reference=needs_reference,
        )

        model.additional_properties = d
        return model

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
