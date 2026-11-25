from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.campaign_result_metrics_object import CampaignResultMetricsObject
from typing import cast

if TYPE_CHECKING:
    from ..models.campaign_result_metrics_formulas_item import (
        CampaignResultMetricsFormulasItem,
    )
    from ..models.campaign_result_metrics_metrics_item import (
        CampaignResultMetricsMetricsItem,
    )


T = TypeVar("T", bound="CampaignResultMetrics")


@_attrs_define
class CampaignResultMetrics:
    """
    Attributes:
        object_ (CampaignResultMetricsObject | Unset):
        metrics (list[CampaignResultMetricsMetricsItem] | Unset):
        formulas (list[CampaignResultMetricsFormulasItem] | Unset):
        result_events (list[str] | Unset):
        note (str | Unset):
    """

    object_: CampaignResultMetricsObject | Unset = UNSET
    metrics: list[CampaignResultMetricsMetricsItem] | Unset = UNSET
    formulas: list[CampaignResultMetricsFormulasItem] | Unset = UNSET
    result_events: list[str] | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        metrics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)

        formulas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.formulas, Unset):
            formulas = []
            for formulas_item_data in self.formulas:
                formulas_item = formulas_item_data.to_dict()
                formulas.append(formulas_item)

        result_events: list[str] | Unset = UNSET
        if not isinstance(self.result_events, Unset):
            result_events = self.result_events

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if formulas is not UNSET:
            field_dict["formulas"] = formulas
        if result_events is not UNSET:
            field_dict["result_events"] = result_events
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.campaign_result_metrics_formulas_item import (
            CampaignResultMetricsFormulasItem,
        )  # noqa: PLC0415
        from ..models.campaign_result_metrics_metrics_item import (
            CampaignResultMetricsMetricsItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: CampaignResultMetricsObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = CampaignResultMetricsObject(_object_)

        _metrics = d.pop("metrics", UNSET)
        metrics: list[CampaignResultMetricsMetricsItem] | Unset = UNSET
        if _metrics is not UNSET:
            metrics = []
            for metrics_item_data in _metrics:
                metrics_item = CampaignResultMetricsMetricsItem.from_dict(
                    metrics_item_data
                )

                metrics.append(metrics_item)

        _formulas = d.pop("formulas", UNSET)
        formulas: list[CampaignResultMetricsFormulasItem] | Unset = UNSET
        if _formulas is not UNSET:
            formulas = []
            for formulas_item_data in _formulas:
                formulas_item = CampaignResultMetricsFormulasItem.from_dict(
                    formulas_item_data
                )

                formulas.append(formulas_item)

        result_events = cast(list[str], d.pop("result_events", UNSET))

        note = d.pop("note", UNSET)

        campaign_result_metrics = cls(
            object_=object_,
            metrics=metrics,
            formulas=formulas,
            result_events=result_events,
            note=note,
        )

        campaign_result_metrics.additional_properties = d
        return campaign_result_metrics

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
