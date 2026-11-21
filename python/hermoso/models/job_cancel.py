from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.job_cancel_object import JobCancelObject

if TYPE_CHECKING:
    from ..models.job import Job


T = TypeVar("T", bound="JobCancel")


@_attrs_define
class JobCancel:
    """
    Attributes:
        object_ (JobCancelObject | Unset):
        outcome (str | Unset): `cancelled`: it had not started, it is stopped and nothing was charged. `requested`: it
            is starting; it stops before it reaches a model if it can, and is charged nothing if it does. `too_late`: it has
            already reached the model, so it finishes, is charged as usual and lands in the Library. `finished`: it had
            already ended. This enum MAY GROW.
        message (str | Unset): A plain sentence for the person who asked to cancel.
        job (Job | Unset):
    """

    object_: JobCancelObject | Unset = UNSET
    outcome: str | Unset = UNSET
    message: str | Unset = UNSET
    job: Job | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        outcome = self.outcome

        message = self.message

        job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = self.job.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if message is not UNSET:
            field_dict["message"] = message
        if job is not UNSET:
            field_dict["job"] = job

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job import Job  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: JobCancelObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = JobCancelObject(_object_)

        outcome = d.pop("outcome", UNSET)

        message = d.pop("message", UNSET)

        _job = d.pop("job", UNSET)
        job: Job | Unset
        if isinstance(_job, Unset):
            job = UNSET
        else:
            job = Job.from_dict(_job)

        job_cancel = cls(
            object_=object_,
            outcome=outcome,
            message=message,
            job=job,
        )

        job_cancel.additional_properties = d
        return job_cancel

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
