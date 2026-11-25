from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.ad_change_stage_args import AdChangeStageArgs


T = TypeVar("T", bound="AdChangeStage")


@_attrs_define
class AdChangeStage:
    """
    Attributes:
        tool (str): The ads tool to run later, e.g. set_meta_campaign_status.
        args (AdChangeStageArgs | Unset): Its arguments, exactly as the tool takes them (without confirm).
        note (str | Unset): Why, shown to the person who confirms.
    """

    tool: str
    args: AdChangeStageArgs | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tool = self.tool

        args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tool": tool,
            }
        )
        if args is not UNSET:
            field_dict["args"] = args
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_change_stage_args import AdChangeStageArgs  # noqa: PLC0415

        d = dict(src_dict)
        tool = d.pop("tool")

        _args = d.pop("args", UNSET)
        args: AdChangeStageArgs | Unset
        if isinstance(_args, Unset):
            args = UNSET
        else:
            args = AdChangeStageArgs.from_dict(_args)

        note = d.pop("note", UNSET)

        ad_change_stage = cls(
            tool=tool,
            args=args,
            note=note,
        )

        ad_change_stage.additional_properties = d
        return ad_change_stage

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
