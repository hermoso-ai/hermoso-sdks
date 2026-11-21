from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.job_object import JobObject
from typing import cast

if TYPE_CHECKING:
    from ..models.job_result_type_0 import JobResultType0


T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """
    Attributes:
        object_ (JobObject | Unset):
        id (str | Unset):
        type_ (str | Unset): What kind of work it is: video, stitch, avatar, templatead, upscale, and so on. This set
            MAY GROW.
        status (str | Unset): queued, running, done or error. `done` and `error` are final. This enum MAY GROW: keep
            polling on a value you have not seen.
        progress (float | Unset): 0 to 1, when the worker reports it.
        label (None | str | Unset):
        brand_id (str | Unset): The profile that started the job.
        created_at (None | str | Unset): ISO-8601.
        updated_at (None | str | Unset): ISO-8601. For a finished job, when it finished.
        run_at (None | str | Unset): ISO-8601, for work scheduled to start later; null for work that starts immediately.
        url (None | str | Unset): The finished file, once `status` is `done` and the job produced one. Always an
            absolute, publicly reachable URL.
        poster_url (None | str | Unset): A still for a finished video, when there is one.
        model (None | str | Unset): The model that rendered it.
        credits_used (float | None | Unset):
        error_message (None | str | Unset): Why it failed, when `status` is `error`. Named `error_message` so it can
            never be mistaken for this API’s error envelope.
        cancelled (bool | Unset): True when the job was stopped by `POST /v1/jobs/{id}/cancel` before it reached a
            model. Its `status` is `error` and nothing was charged.
        result (JobResultType0 | None | Unset): The worker’s full result. PASSTHROUGH TIER: its shape is the job type’s
            own and improves with it, like a tool’s `data`. Build on the fields above; read this for detail.
        poll (str | Unset): This job’s own path.
    """

    object_: JobObject | Unset = UNSET
    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    status: str | Unset = UNSET
    progress: float | Unset = UNSET
    label: None | str | Unset = UNSET
    brand_id: str | Unset = UNSET
    created_at: None | str | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    run_at: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    poster_url: None | str | Unset = UNSET
    model: None | str | Unset = UNSET
    credits_used: float | None | Unset = UNSET
    error_message: None | str | Unset = UNSET
    cancelled: bool | Unset = UNSET
    result: JobResultType0 | None | Unset = UNSET
    poll: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.job_result_type_0 import JobResultType0  # noqa: PLC0415

        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        type_ = self.type_

        status = self.status

        progress = self.progress

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        brand_id = self.brand_id

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        run_at: None | str | Unset
        if isinstance(self.run_at, Unset):
            run_at = UNSET
        else:
            run_at = self.run_at

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        poster_url: None | str | Unset
        if isinstance(self.poster_url, Unset):
            poster_url = UNSET
        else:
            poster_url = self.poster_url

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        credits_used: float | None | Unset
        if isinstance(self.credits_used, Unset):
            credits_used = UNSET
        else:
            credits_used = self.credits_used

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        cancelled = self.cancelled

        result: dict[str, Any] | None | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        elif isinstance(self.result, JobResultType0):
            result = self.result.to_dict()
        else:
            result = self.result

        poll = self.poll

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if progress is not UNSET:
            field_dict["progress"] = progress
        if label is not UNSET:
            field_dict["label"] = label
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if run_at is not UNSET:
            field_dict["run_at"] = run_at
        if url is not UNSET:
            field_dict["url"] = url
        if poster_url is not UNSET:
            field_dict["poster_url"] = poster_url
        if model is not UNSET:
            field_dict["model"] = model
        if credits_used is not UNSET:
            field_dict["credits_used"] = credits_used
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if result is not UNSET:
            field_dict["result"] = result
        if poll is not UNSET:
            field_dict["poll"] = poll

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_result_type_0 import JobResultType0  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: JobObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = JobObject(_object_)

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        progress = d.pop("progress", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        brand_id = d.pop("brand_id", UNSET)

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_run_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        run_at = _parse_run_at(d.pop("run_at", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_poster_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        poster_url = _parse_poster_url(d.pop("poster_url", UNSET))

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_credits_used(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        credits_used = _parse_credits_used(d.pop("credits_used", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        cancelled = d.pop("cancelled", UNSET)

        def _parse_result(data: object) -> JobResultType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_0 = JobResultType0.from_dict(data)

                return result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobResultType0 | None | Unset, data)

        result = _parse_result(d.pop("result", UNSET))

        poll = d.pop("poll", UNSET)

        job = cls(
            object_=object_,
            id=id,
            type_=type_,
            status=status,
            progress=progress,
            label=label,
            brand_id=brand_id,
            created_at=created_at,
            updated_at=updated_at,
            run_at=run_at,
            url=url,
            poster_url=poster_url,
            model=model,
            credits_used=credits_used,
            error_message=error_message,
            cancelled=cancelled,
            result=result,
            poll=poll,
        )

        job.additional_properties = d
        return job

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
