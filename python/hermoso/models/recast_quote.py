from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.recast_quote_object import RecastQuoteObject
from typing import cast

if TYPE_CHECKING:
    from ..models.recast_step import RecastStep


T = TypeVar("T", bound="RecastQuote")


@_attrs_define
class RecastQuote:
    """
    Attributes:
        object_ (RecastQuoteObject | Unset):
        credits_ (float | None | Unset): The whole price: the sum of `steps`. An estimate: a real call reserves it and
            is charged its actual cost, usually within a few percent. null when it would not start (see `refused`).
        likely_credits (float | None | Unset):
        refused (None | str | Unset): Why it would not start. Nothing was charged.
        steps (list[RecastStep] | Unset):
    """

    object_: RecastQuoteObject | Unset = UNSET
    credits_: float | None | Unset = UNSET
    likely_credits: float | None | Unset = UNSET
    refused: None | str | Unset = UNSET
    steps: list[RecastStep] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

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

        refused: None | str | Unset
        if isinstance(self.refused, Unset):
            refused = UNSET
        else:
            refused = self.refused

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if likely_credits is not UNSET:
            field_dict["likely_credits"] = likely_credits
        if refused is not UNSET:
            field_dict["refused"] = refused
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recast_step import RecastStep  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: RecastQuoteObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = RecastQuoteObject(_object_)

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

        def _parse_refused(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refused = _parse_refused(d.pop("refused", UNSET))

        _steps = d.pop("steps", UNSET)
        steps: list[RecastStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = RecastStep.from_dict(steps_item_data)

                steps.append(steps_item)

        recast_quote = cls(
            object_=object_,
            credits_=credits_,
            likely_credits=likely_credits,
            refused=refused,
            steps=steps,
        )

        recast_quote.additional_properties = d
        return recast_quote

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
