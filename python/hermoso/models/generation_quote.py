from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.generation_quote_object import GenerationQuoteObject
from typing import cast


T = TypeVar("T", bound="GenerationQuote")


@_attrs_define
class GenerationQuote:
    """
    Attributes:
        object_ (GenerationQuoteObject | Unset):
        type_ (str | Unset):
        credits_ (float | None | Unset): What the render reserves. null when it would not start (see `refused`).
        likely_credits (float | None | Unset): Present when the hold covers an optional step (a label repair) that
            usually does not run: the likely charge, `credits` being the most it can be.
        label (None | str | Unset): The model or pipeline that will render it.
        refused (None | str | Unset): Why the render would not start. Nothing was charged.
        reference_images (list[str] | Unset): Image only: the pictures the render will use, exactly as it attaches them.
            With `use_brand` on these are the profile’s own saved product photos (up to three) and its logo when the prompt
            asks for one; empty when none is on file.
        reference_note (None | str | Unset): Image only: a sentence about those pictures when there is one to say (a
            photo left out, a lineup, the logo).
    """

    object_: GenerationQuoteObject | Unset = UNSET
    type_: str | Unset = UNSET
    credits_: float | None | Unset = UNSET
    likely_credits: float | None | Unset = UNSET
    label: None | str | Unset = UNSET
    refused: None | str | Unset = UNSET
    reference_images: list[str] | Unset = UNSET
    reference_note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        type_ = self.type_

        credits_: float | None | Unset
        if isinstance(self.credits_, Unset):
            credits_ = UNSET
        else:
            credits_ = self.credits_

        likely_credits: float | None | Unset
        if isinstance(self.likely_credits, Unset):
            likely_credits = UNSET
        else:
            likely_credits = self.likely_credits

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        refused: None | str | Unset
        if isinstance(self.refused, Unset):
            refused = UNSET
        else:
            refused = self.refused

        reference_images: list[str] | Unset = UNSET
        if not isinstance(self.reference_images, Unset):
            reference_images = self.reference_images

        reference_note: None | str | Unset
        if isinstance(self.reference_note, Unset):
            reference_note = UNSET
        else:
            reference_note = self.reference_note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if type_ is not UNSET:
            field_dict["type"] = type_
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if likely_credits is not UNSET:
            field_dict["likely_credits"] = likely_credits
        if label is not UNSET:
            field_dict["label"] = label
        if refused is not UNSET:
            field_dict["refused"] = refused
        if reference_images is not UNSET:
            field_dict["reference_images"] = reference_images
        if reference_note is not UNSET:
            field_dict["reference_note"] = reference_note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: GenerationQuoteObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = GenerationQuoteObject(_object_)

        type_ = d.pop("type", UNSET)

        def _parse_credits_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        credits_ = _parse_credits_(d.pop("credits", UNSET))

        def _parse_likely_credits(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        likely_credits = _parse_likely_credits(d.pop("likely_credits", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_refused(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refused = _parse_refused(d.pop("refused", UNSET))

        reference_images = cast(list[str], d.pop("reference_images", UNSET))

        def _parse_reference_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference_note = _parse_reference_note(d.pop("reference_note", UNSET))

        generation_quote = cls(
            object_=object_,
            type_=type_,
            credits_=credits_,
            likely_credits=likely_credits,
            label=label,
            refused=refused,
            reference_images=reference_images,
            reference_note=reference_note,
        )

        generation_quote.additional_properties = d
        return generation_quote

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
