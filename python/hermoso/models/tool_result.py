from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tool_result_object import ToolResultObject
from typing import cast

if TYPE_CHECKING:
    from ..models.tool_result_data_type_0 import ToolResultDataType0
    from ..models.tool_result_ignored_arguments_item import (
        ToolResultIgnoredArgumentsItem,
    )
    from ..models.tool_result_images_item import ToolResultImagesItem


T = TypeVar("T", bound="ToolResult")


@_attrs_define
class ToolResult:
    """
    Attributes:
        object_ (ToolResultObject | Unset):
        tool (str | Unset):
        text (str | Unset): The tool’s answer as a sentence — what a model would read. Always present.
        data (None | ToolResultDataType0 | Unset): The structured result, when the tool produces one; null when its
            answer is only prose. Its shape is the tool’s own and moves with the tool.
        images (list[ToolResultImagesItem] | Unset): Present only when the tool returned pictures for a model to look at
            (view_images, video_frames, a finished image): each as base64 with its mimeType, ready to hand to a vision
            model.
        ignored_arguments (list[ToolResultIgnoredArgumentsItem] | Unset): Present when the call ran WITHOUT keys the
            tool does not take: each one, with the argument it most likely meant. The text starts with the same news, and
            data.ignoredArguments carries it too.
    """

    object_: ToolResultObject | Unset = UNSET
    tool: str | Unset = UNSET
    text: str | Unset = UNSET
    data: None | ToolResultDataType0 | Unset = UNSET
    images: list[ToolResultImagesItem] | Unset = UNSET
    ignored_arguments: list[ToolResultIgnoredArgumentsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_result_data_type_0 import ToolResultDataType0  # noqa: PLC0415

        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        tool = self.tool

        text = self.text

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, ToolResultDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        ignored_arguments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ignored_arguments, Unset):
            ignored_arguments = []
            for ignored_arguments_item_data in self.ignored_arguments:
                ignored_arguments_item = ignored_arguments_item_data.to_dict()
                ignored_arguments.append(ignored_arguments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if tool is not UNSET:
            field_dict["tool"] = tool
        if text is not UNSET:
            field_dict["text"] = text
        if data is not UNSET:
            field_dict["data"] = data
        if images is not UNSET:
            field_dict["images"] = images
        if ignored_arguments is not UNSET:
            field_dict["ignored_arguments"] = ignored_arguments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_result_data_type_0 import ToolResultDataType0  # noqa: PLC0415
        from ..models.tool_result_ignored_arguments_item import (
            ToolResultIgnoredArgumentsItem,
        )  # noqa: PLC0415
        from ..models.tool_result_images_item import ToolResultImagesItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ToolResultObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ToolResultObject(_object_)

        tool = d.pop("tool", UNSET)

        text = d.pop("text", UNSET)

        def _parse_data(data: object) -> None | ToolResultDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = ToolResultDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolResultDataType0 | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        _images = d.pop("images", UNSET)
        images: list[ToolResultImagesItem] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = ToolResultImagesItem.from_dict(images_item_data)

                images.append(images_item)

        _ignored_arguments = d.pop("ignored_arguments", UNSET)
        ignored_arguments: list[ToolResultIgnoredArgumentsItem] | Unset = UNSET
        if _ignored_arguments is not UNSET:
            ignored_arguments = []
            for ignored_arguments_item_data in _ignored_arguments:
                ignored_arguments_item = ToolResultIgnoredArgumentsItem.from_dict(
                    ignored_arguments_item_data
                )

                ignored_arguments.append(ignored_arguments_item)

        tool_result = cls(
            object_=object_,
            tool=tool,
            text=text,
            data=data,
            images=images,
            ignored_arguments=ignored_arguments,
        )

        tool_result.additional_properties = d
        return tool_result

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
