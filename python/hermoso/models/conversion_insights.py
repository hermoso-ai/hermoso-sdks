from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conversion_insights_object import ConversionInsightsObject

if TYPE_CHECKING:
    from ..models.conversion_insights_cohorts_item import ConversionInsightsCohortsItem
    from ..models.conversion_insights_customers_item import (
        ConversionInsightsCustomersItem,
    )
    from ..models.conversion_insights_destinations_item import (
        ConversionInsightsDestinationsItem,
    )
    from ..models.conversion_insights_journey import ConversionInsightsJourney
    from ..models.conversion_insights_paths_item import ConversionInsightsPathsItem


T = TypeVar("T", bound="ConversionInsights")


@_attrs_define
class ConversionInsights:
    """
    Attributes:
        object_ (ConversionInsightsObject | Unset):
        view (str | Unset):
        journey (ConversionInsightsJourney | Unset):
        customers (list[ConversionInsightsCustomersItem] | Unset):
        paths (list[ConversionInsightsPathsItem] | Unset):
        cohorts (list[ConversionInsightsCohortsItem] | Unset):
        destinations (list[ConversionInsightsDestinationsItem] | Unset):
        note (str | Unset):
    """

    object_: ConversionInsightsObject | Unset = UNSET
    view: str | Unset = UNSET
    journey: ConversionInsightsJourney | Unset = UNSET
    customers: list[ConversionInsightsCustomersItem] | Unset = UNSET
    paths: list[ConversionInsightsPathsItem] | Unset = UNSET
    cohorts: list[ConversionInsightsCohortsItem] | Unset = UNSET
    destinations: list[ConversionInsightsDestinationsItem] | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        view = self.view

        journey: dict[str, Any] | Unset = UNSET
        if not isinstance(self.journey, Unset):
            journey = self.journey.to_dict()

        customers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.customers, Unset):
            customers = []
            for customers_item_data in self.customers:
                customers_item = customers_item_data.to_dict()
                customers.append(customers_item)

        paths: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.paths, Unset):
            paths = []
            for paths_item_data in self.paths:
                paths_item = paths_item_data.to_dict()
                paths.append(paths_item)

        cohorts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cohorts, Unset):
            cohorts = []
            for cohorts_item_data in self.cohorts:
                cohorts_item = cohorts_item_data.to_dict()
                cohorts.append(cohorts_item)

        destinations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.destinations, Unset):
            destinations = []
            for destinations_item_data in self.destinations:
                destinations_item = destinations_item_data.to_dict()
                destinations.append(destinations_item)

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if view is not UNSET:
            field_dict["view"] = view
        if journey is not UNSET:
            field_dict["journey"] = journey
        if customers is not UNSET:
            field_dict["customers"] = customers
        if paths is not UNSET:
            field_dict["paths"] = paths
        if cohorts is not UNSET:
            field_dict["cohorts"] = cohorts
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_insights_cohorts_item import (
            ConversionInsightsCohortsItem,
        )  # noqa: PLC0415
        from ..models.conversion_insights_customers_item import (
            ConversionInsightsCustomersItem,
        )  # noqa: PLC0415
        from ..models.conversion_insights_destinations_item import (
            ConversionInsightsDestinationsItem,
        )  # noqa: PLC0415
        from ..models.conversion_insights_journey import ConversionInsightsJourney  # noqa: PLC0415
        from ..models.conversion_insights_paths_item import ConversionInsightsPathsItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ConversionInsightsObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ConversionInsightsObject(_object_)

        view = d.pop("view", UNSET)

        _journey = d.pop("journey", UNSET)
        journey: ConversionInsightsJourney | Unset
        if isinstance(_journey, Unset):
            journey = UNSET
        else:
            journey = ConversionInsightsJourney.from_dict(_journey)

        _customers = d.pop("customers", UNSET)
        customers: list[ConversionInsightsCustomersItem] | Unset = UNSET
        if _customers is not UNSET:
            customers = []
            for customers_item_data in _customers:
                customers_item = ConversionInsightsCustomersItem.from_dict(
                    customers_item_data
                )

                customers.append(customers_item)

        _paths = d.pop("paths", UNSET)
        paths: list[ConversionInsightsPathsItem] | Unset = UNSET
        if _paths is not UNSET:
            paths = []
            for paths_item_data in _paths:
                paths_item = ConversionInsightsPathsItem.from_dict(paths_item_data)

                paths.append(paths_item)

        _cohorts = d.pop("cohorts", UNSET)
        cohorts: list[ConversionInsightsCohortsItem] | Unset = UNSET
        if _cohorts is not UNSET:
            cohorts = []
            for cohorts_item_data in _cohorts:
                cohorts_item = ConversionInsightsCohortsItem.from_dict(
                    cohorts_item_data
                )

                cohorts.append(cohorts_item)

        _destinations = d.pop("destinations", UNSET)
        destinations: list[ConversionInsightsDestinationsItem] | Unset = UNSET
        if _destinations is not UNSET:
            destinations = []
            for destinations_item_data in _destinations:
                destinations_item = ConversionInsightsDestinationsItem.from_dict(
                    destinations_item_data
                )

                destinations.append(destinations_item)

        note = d.pop("note", UNSET)

        conversion_insights = cls(
            object_=object_,
            view=view,
            journey=journey,
            customers=customers,
            paths=paths,
            cohorts=cohorts,
            destinations=destinations,
            note=note,
        )

        conversion_insights.additional_properties = d
        return conversion_insights

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
