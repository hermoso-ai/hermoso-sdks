from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="CloneQuoteStep")


@_attrs_define
class CloneQuoteStep:
    """
    Attributes:
        step (str | Unset): read_layout, render, copy_and_check, plan or render_video. This set MAY GROW.
        label (str | Unset): The step in plain words.
        credits_ (float | None | Unset): Its price, or null when it is billed at real cost or priced later.
        likely_credits (float | None | Unset): For a `hold` that covers an optional step (a label repair): the likely
            charge.
        basis (str | Unset): flat, hold, estimate, metered or later. This set MAY GROW.
    """

    step: str | Unset = UNSET
    label: str | Unset = UNSET
    credits_: float | None | Unset = UNSET
    likely_credits: float | None | Unset = UNSET
    basis: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step

        label = self.label

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

        basis = self.basis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if step is not UNSET:
            field_dict["step"] = step
        if label is not UNSET:
            field_dict["label"] = label
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if likely_credits is not UNSET:
            field_dict["likely_credits"] = likely_credits
        if basis is not UNSET:
            field_dict["basis"] = basis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        step = d.pop("step", UNSET)

        label = d.pop("label", UNSET)

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

        basis = d.pop("basis", UNSET)

        clone_quote_step = cls(
            step=step,
            label=label,
            credits_=credits_,
            likely_credits=likely_credits,
            basis=basis,
        )

        clone_quote_step.additional_properties = d
        return clone_quote_step

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
