from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.clone_quote_object import CloneQuoteObject
from typing import cast

if TYPE_CHECKING:
    from ..models.clone_quote_step import CloneQuoteStep


T = TypeVar("T", bound="CloneQuote")


@_attrs_define
class CloneQuote:
    """
    Attributes:
        object_ (CloneQuoteObject | Unset):
        type_ (str | Unset): clone_image or clone_video. This set MAY GROW.
        credits_ (float | None | Unset): The sum of every step priced in advance (`flat` and `hold` steps, plus
            `estimate` steps). Steps with `credits: null` are billed on top at their real cost.
        steps (list[CloneQuoteStep] | Unset):
        refused (None | str | Unset): Why the clone would not start. Nothing was charged.
        next_ (str | Unset): What runs it, in one sentence.
    """

    object_: CloneQuoteObject | Unset = UNSET
    type_: str | Unset = UNSET
    credits_: float | None | Unset = UNSET
    steps: list[CloneQuoteStep] | Unset = UNSET
    refused: None | str | Unset = UNSET
    next_: str | Unset = UNSET
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

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        refused: None | str | Unset
        if isinstance(self.refused, Unset):
            refused = UNSET
        else:
            refused = self.refused

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if type_ is not UNSET:
            field_dict["type"] = type_
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if steps is not UNSET:
            field_dict["steps"] = steps
        if refused is not UNSET:
            field_dict["refused"] = refused
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clone_quote_step import CloneQuoteStep  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: CloneQuoteObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = CloneQuoteObject(_object_)

        type_ = d.pop("type", UNSET)

        def _parse_credits_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        credits_ = _parse_credits_(d.pop("credits", UNSET))

        _steps = d.pop("steps", UNSET)
        steps: list[CloneQuoteStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = CloneQuoteStep.from_dict(steps_item_data)

                steps.append(steps_item)

        def _parse_refused(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refused = _parse_refused(d.pop("refused", UNSET))

        next_ = d.pop("next", UNSET)

        clone_quote = cls(
            object_=object_,
            type_=type_,
            credits_=credits_,
            steps=steps,
            refused=refused,
            next_=next_,
        )

        clone_quote.additional_properties = d
        return clone_quote

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
