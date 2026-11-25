from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.boost_automation_create_every import BoostAutomationCreateEvery
from ..models.boost_automation_create_launch import BoostAutomationCreateLaunch

if TYPE_CHECKING:
    from ..models.boost_automation_create_boost import BoostAutomationCreateBoost
    from ..models.boost_automation_create_filter import BoostAutomationCreateFilter


T = TypeVar("T", bound="BoostAutomationCreate")


@_attrs_define
class BoostAutomationCreate:
    """
    Attributes:
        channel (str): facebook or instagram today. NOT AN ENUM: a channel boost automations reach later is another
            value here; the server refuses one it cannot boost, by name.
        ad_account_id (str):
        filter_ (BoostAutomationCreateFilter):
        boost (BoostAutomationCreateBoost):
        name (str | Unset):
        every (BoostAutomationCreateEvery | Unset):
        launch (BoostAutomationCreateLaunch | Unset):
    """

    channel: str
    ad_account_id: str
    filter_: BoostAutomationCreateFilter
    boost: BoostAutomationCreateBoost
    name: str | Unset = UNSET
    every: BoostAutomationCreateEvery | Unset = UNSET
    launch: BoostAutomationCreateLaunch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        ad_account_id = self.ad_account_id

        filter_ = self.filter_.to_dict()

        boost = self.boost.to_dict()

        name = self.name

        every: str | Unset = UNSET
        if not isinstance(self.every, Unset):
            every = self.every.value

        launch: str | Unset = UNSET
        if not isinstance(self.launch, Unset):
            launch = self.launch.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
                "adAccountId": ad_account_id,
                "filter": filter_,
                "boost": boost,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if every is not UNSET:
            field_dict["every"] = every
        if launch is not UNSET:
            field_dict["launch"] = launch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boost_automation_create_boost import BoostAutomationCreateBoost  # noqa: PLC0415
        from ..models.boost_automation_create_filter import BoostAutomationCreateFilter  # noqa: PLC0415

        d = dict(src_dict)
        channel = d.pop("channel")

        ad_account_id = d.pop("adAccountId")

        filter_ = BoostAutomationCreateFilter.from_dict(d.pop("filter"))

        boost = BoostAutomationCreateBoost.from_dict(d.pop("boost"))

        name = d.pop("name", UNSET)

        _every = d.pop("every", UNSET)
        every: BoostAutomationCreateEvery | Unset
        if isinstance(_every, Unset):
            every = UNSET
        else:
            every = BoostAutomationCreateEvery(_every)

        _launch = d.pop("launch", UNSET)
        launch: BoostAutomationCreateLaunch | Unset
        if isinstance(_launch, Unset):
            launch = UNSET
        else:
            launch = BoostAutomationCreateLaunch(_launch)

        boost_automation_create = cls(
            channel=channel,
            ad_account_id=ad_account_id,
            filter_=filter_,
            boost=boost,
            name=name,
            every=every,
            launch=launch,
        )

        boost_automation_create.additional_properties = d
        return boost_automation_create

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
