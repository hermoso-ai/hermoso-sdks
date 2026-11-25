from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.automation_template_create_automations_item import (
        AutomationTemplateCreateAutomationsItem,
    )
    from ..models.automation_template_create_from import AutomationTemplateCreateFrom


T = TypeVar("T", bound="AutomationTemplateCreate")


@_attrs_define
class AutomationTemplateCreate:
    """
    Attributes:
        name (str):
        description (str | Unset):
        automations (list[AutomationTemplateCreateAutomationsItem] | Unset):
        from_ (AutomationTemplateCreateFrom | Unset):
        share (bool | Unset):
    """

    name: str
    description: str | Unset = UNSET
    automations: list[AutomationTemplateCreateAutomationsItem] | Unset = UNSET
    from_: AutomationTemplateCreateFrom | Unset = UNSET
    share: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        automations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.automations, Unset):
            automations = []
            for automations_item_data in self.automations:
                automations_item = automations_item_data.to_dict()
                automations.append(automations_item)

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        share = self.share

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if automations is not UNSET:
            field_dict["automations"] = automations
        if from_ is not UNSET:
            field_dict["from"] = from_
        if share is not UNSET:
            field_dict["share"] = share

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_template_create_automations_item import (
            AutomationTemplateCreateAutomationsItem,
        )  # noqa: PLC0415
        from ..models.automation_template_create_from import (
            AutomationTemplateCreateFrom,
        )  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _automations = d.pop("automations", UNSET)
        automations: list[AutomationTemplateCreateAutomationsItem] | Unset = UNSET
        if _automations is not UNSET:
            automations = []
            for automations_item_data in _automations:
                automations_item = AutomationTemplateCreateAutomationsItem.from_dict(
                    automations_item_data
                )

                automations.append(automations_item)

        _from_ = d.pop("from", UNSET)
        from_: AutomationTemplateCreateFrom | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = AutomationTemplateCreateFrom.from_dict(_from_)

        share = d.pop("share", UNSET)

        automation_template_create = cls(
            name=name,
            description=description,
            automations=automations,
            from_=from_,
            share=share,
        )

        automation_template_create.additional_properties = d
        return automation_template_create

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
