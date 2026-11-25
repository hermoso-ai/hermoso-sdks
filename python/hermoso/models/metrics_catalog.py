from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.metrics_catalog_object import MetricsCatalogObject
from typing import cast

if TYPE_CHECKING:
    from ..models.metrics_catalog_channels import MetricsCatalogChannels
    from ..models.metrics_catalog_entities import MetricsCatalogEntities


T = TypeVar("T", bound="MetricsCatalog")


@_attrs_define
class MetricsCatalog:
    """
    Attributes:
        object_ (MetricsCatalogObject | Unset):
        entities (MetricsCatalogEntities | Unset):
        channels (MetricsCatalogChannels | Unset):
        rules (list[str] | Unset):
    """

    object_: MetricsCatalogObject | Unset = UNSET
    entities: MetricsCatalogEntities | Unset = UNSET
    channels: MetricsCatalogChannels | Unset = UNSET
    rules: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        entities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities.to_dict()

        channels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels.to_dict()

        rules: list[str] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if entities is not UNSET:
            field_dict["entities"] = entities
        if channels is not UNSET:
            field_dict["channels"] = channels
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metrics_catalog_channels import MetricsCatalogChannels  # noqa: PLC0415
        from ..models.metrics_catalog_entities import MetricsCatalogEntities  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: MetricsCatalogObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = MetricsCatalogObject(_object_)

        _entities = d.pop("entities", UNSET)
        entities: MetricsCatalogEntities | Unset
        if isinstance(_entities, Unset):
            entities = UNSET
        else:
            entities = MetricsCatalogEntities.from_dict(_entities)

        _channels = d.pop("channels", UNSET)
        channels: MetricsCatalogChannels | Unset
        if isinstance(_channels, Unset):
            channels = UNSET
        else:
            channels = MetricsCatalogChannels.from_dict(_channels)

        rules = cast(list[str], d.pop("rules", UNSET))

        metrics_catalog = cls(
            object_=object_,
            entities=entities,
            channels=channels,
            rules=rules,
        )

        metrics_catalog.additional_properties = d
        return metrics_catalog

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
