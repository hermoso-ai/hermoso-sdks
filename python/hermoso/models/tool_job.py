from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tool_job_object import ToolJobObject


T = TypeVar("T", bound="ToolJob")


@_attrs_define
class ToolJob:
    """A handle to a render that is queued or still running, answered with HTTP 202 when `wait` was sent.

    Attributes:
        object_ (ToolJobObject | Unset):
        tool (str | Unset): The tool that was called.
        job_id (str | Unset):
        status (str | Unset): queued or running at the moment of the reply. This enum MAY GROW.
        poll (str | Unset): The path to poll: /v1/jobs/{id}. Also sent as the `Location` header.
        poll_url (str | Unset): The same, as an absolute URL.
        retry_after_seconds (int | Unset): A sensible gap between polls. Also sent as `Retry-After`.
        text (str | Unset): The tool’s own sentence about the queued render.
    """

    object_: ToolJobObject | Unset = UNSET
    tool: str | Unset = UNSET
    job_id: str | Unset = UNSET
    status: str | Unset = UNSET
    poll: str | Unset = UNSET
    poll_url: str | Unset = UNSET
    retry_after_seconds: int | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        tool = self.tool

        job_id = self.job_id

        status = self.status

        poll = self.poll

        poll_url = self.poll_url

        retry_after_seconds = self.retry_after_seconds

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if tool is not UNSET:
            field_dict["tool"] = tool
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if status is not UNSET:
            field_dict["status"] = status
        if poll is not UNSET:
            field_dict["poll"] = poll
        if poll_url is not UNSET:
            field_dict["poll_url"] = poll_url
        if retry_after_seconds is not UNSET:
            field_dict["retry_after_seconds"] = retry_after_seconds
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ToolJobObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ToolJobObject(_object_)

        tool = d.pop("tool", UNSET)

        job_id = d.pop("job_id", UNSET)

        status = d.pop("status", UNSET)

        poll = d.pop("poll", UNSET)

        poll_url = d.pop("poll_url", UNSET)

        retry_after_seconds = d.pop("retry_after_seconds", UNSET)

        text = d.pop("text", UNSET)

        tool_job = cls(
            object_=object_,
            tool=tool,
            job_id=job_id,
            status=status,
            poll=poll,
            poll_url=poll_url,
            retry_after_seconds=retry_after_seconds,
            text=text,
        )

        tool_job.additional_properties = d
        return tool_job

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
