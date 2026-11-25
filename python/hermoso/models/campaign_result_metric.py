from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.campaign_result_metric_kind import CampaignResultMetricKind
from typing import cast


T = TypeVar("T", bound="CampaignResultMetric")


@_attrs_define
class CampaignResultMetric:
    """
    Attributes:
        label (str | Unset):
        kind (CampaignResultMetricKind | Unset):
        currency (str | Unset):
        formula (None | str | Unset):
    """

    label: str | Unset = UNSET
    kind: CampaignResultMetricKind | Unset = UNSET
    currency: str | Unset = UNSET
    formula: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        currency = self.currency

        formula: None | str | Unset
        if isinstance(self.formula, Unset):
            formula = UNSET
        else:
            formula = self.formula

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if kind is not UNSET:
            field_dict["kind"] = kind
        if currency is not UNSET:
            field_dict["currency"] = currency
        if formula is not UNSET:
            field_dict["formula"] = formula

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: CampaignResultMetricKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = CampaignResultMetricKind(_kind)

        currency = d.pop("currency", UNSET)

        def _parse_formula(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        formula = _parse_formula(d.pop("formula", UNSET))

        campaign_result_metric = cls(
            label=label,
            kind=kind,
            currency=currency,
            formula=formula,
        )

        campaign_result_metric.additional_properties = d
        return campaign_result_metric

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
