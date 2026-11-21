from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.edit_mode import EditMode
from ..models.edit_object import EditObject
from typing import cast

if TYPE_CHECKING:
    from ..models.edit_preview_type_0 import EditPreviewType0
    from ..models.edit_quote import EditQuote
    from ..models.job import Job


T = TypeVar("T", bound="Edit")


@_attrs_define
class Edit:
    """
    Attributes:
        object_ (EditObject | Unset):
        dry_run (bool | Unset):
        mode (EditMode | Unset): `preview` when `preview_first_frame` was sent. This enum MAY GROW.
        status (str | Unset): `quoted`, `refused`, `previewed`, or the job's own status once queued: `queued`,
            `running`, `done`, `error`. This enum MAY GROW.
        quote (EditQuote | Unset):
        preview (EditPreviewType0 | None | Unset):
        job_id (None | str | Unset):
        job (Job | None | Unset): The queued job, as `GET /v1/jobs/{id}` answers it.
        next_ (str | Unset): What to do now, in one sentence.
    """

    object_: EditObject | Unset = UNSET
    dry_run: bool | Unset = UNSET
    mode: EditMode | Unset = UNSET
    status: str | Unset = UNSET
    quote: EditQuote | Unset = UNSET
    preview: EditPreviewType0 | None | Unset = UNSET
    job_id: None | str | Unset = UNSET
    job: Job | None | Unset = UNSET
    next_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.edit_preview_type_0 import EditPreviewType0  # noqa: PLC0415
        from ..models.job import Job  # noqa: PLC0415

        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        dry_run = self.dry_run

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        status = self.status

        quote: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quote, Unset):
            quote = self.quote.to_dict()

        preview: dict[str, Any] | None | Unset
        if isinstance(self.preview, Unset):
            preview = UNSET
        elif isinstance(self.preview, EditPreviewType0):
            preview = self.preview.to_dict()
        else:
            preview = self.preview

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        else:
            job_id = self.job_id

        job: dict[str, Any] | None | Unset
        if isinstance(self.job, Unset):
            job = UNSET
        elif isinstance(self.job, Job):
            job = self.job.to_dict()
        else:
            job = self.job

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if mode is not UNSET:
            field_dict["mode"] = mode
        if status is not UNSET:
            field_dict["status"] = status
        if quote is not UNSET:
            field_dict["quote"] = quote
        if preview is not UNSET:
            field_dict["preview"] = preview
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if job is not UNSET:
            field_dict["job"] = job
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edit_preview_type_0 import EditPreviewType0  # noqa: PLC0415
        from ..models.edit_quote import EditQuote  # noqa: PLC0415
        from ..models.job import Job  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: EditObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = EditObject(_object_)

        dry_run = d.pop("dry_run", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: EditMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = EditMode(_mode)

        status = d.pop("status", UNSET)

        _quote = d.pop("quote", UNSET)
        quote: EditQuote | Unset
        if isinstance(_quote, Unset):
            quote = UNSET
        else:
            quote = EditQuote.from_dict(_quote)

        def _parse_preview(data: object) -> EditPreviewType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                preview_type_0 = EditPreviewType0.from_dict(data)

                return preview_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditPreviewType0 | None | Unset, data)

        preview = _parse_preview(d.pop("preview", UNSET))

        def _parse_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

        def _parse_job(data: object) -> Job | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_type_1 = Job.from_dict(data)

                return job_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Job | None | Unset, data)

        job = _parse_job(d.pop("job", UNSET))

        next_ = d.pop("next", UNSET)

        edit = cls(
            object_=object_,
            dry_run=dry_run,
            mode=mode,
            status=status,
            quote=quote,
            preview=preview,
            job_id=job_id,
            job=job,
            next_=next_,
        )

        edit.additional_properties = d
        return edit

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
