from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.recast_object import RecastObject
from typing import cast

if TYPE_CHECKING:
    from ..models.job import Job
    from ..models.recast_quote import RecastQuote
    from ..models.recast_subject_type_0 import RecastSubjectType0
    from ..models.recast_voice_type_0 import RecastVoiceType0
    from ..models.recast_window_type_0 import RecastWindowType0


T = TypeVar("T", bound="Recast")


@_attrs_define
class Recast:
    """
    Attributes:
        object_ (RecastObject | Unset):
        dry_run (bool | Unset):
        status (str | Unset): `quoted` (a dry run), `refused` (a dry run that would not start), or the job's own status
            once queued: `queued`, `running`, `done`, `error`. This enum MAY GROW.
        quote (RecastQuote | Unset):
        engine (None | str | Unset): The model that will render it.
        window (None | RecastWindowType0 | Unset): The part of the video that is recast, in seconds.
        source_seconds (float | None | Unset): The whole video's length.
        subject (None | RecastSubjectType0 | Unset):
        voice (None | RecastVoiceType0 | Unset):
        notes (list[str] | Unset): Plain sentences worth showing: a window that was cut, a recast done in passes and the
            cut second to watch, a face that is small in a shot.
        person_url (None | str | Unset): With `person.describe` on a real call: the AI person that was made. It is in
            your Library; send it as `person.image_url` to reuse them.
        job_id (None | str | Unset):
        job (Job | None | Unset): The queued job, as `GET /v1/jobs/{id}` answers it. Poll that until `done`; `url` is
            the video.
    """

    object_: RecastObject | Unset = UNSET
    dry_run: bool | Unset = UNSET
    status: str | Unset = UNSET
    quote: RecastQuote | Unset = UNSET
    engine: None | str | Unset = UNSET
    window: None | RecastWindowType0 | Unset = UNSET
    source_seconds: float | None | Unset = UNSET
    subject: None | RecastSubjectType0 | Unset = UNSET
    voice: None | RecastVoiceType0 | Unset = UNSET
    notes: list[str] | Unset = UNSET
    person_url: None | str | Unset = UNSET
    job_id: None | str | Unset = UNSET
    job: Job | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.job import Job  # noqa: PLC0415
        from ..models.recast_subject_type_0 import RecastSubjectType0  # noqa: PLC0415
        from ..models.recast_voice_type_0 import RecastVoiceType0  # noqa: PLC0415
        from ..models.recast_window_type_0 import RecastWindowType0  # noqa: PLC0415

        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        dry_run = self.dry_run

        status = self.status

        quote: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quote, Unset):
            quote = self.quote.to_dict()

        engine: None | str | Unset
        if isinstance(self.engine, Unset):
            engine = UNSET
        else:
            engine = self.engine

        window: dict[str, Any] | None | Unset
        if isinstance(self.window, Unset):
            window = UNSET
        elif isinstance(self.window, RecastWindowType0):
            window = self.window.to_dict()
        else:
            window = self.window

        source_seconds: float | None | Unset
        if isinstance(self.source_seconds, Unset):
            source_seconds = UNSET
        else:
            source_seconds = self.source_seconds

        subject: dict[str, Any] | None | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        elif isinstance(self.subject, RecastSubjectType0):
            subject = self.subject.to_dict()
        else:
            subject = self.subject

        voice: dict[str, Any] | None | Unset
        if isinstance(self.voice, Unset):
            voice = UNSET
        elif isinstance(self.voice, RecastVoiceType0):
            voice = self.voice.to_dict()
        else:
            voice = self.voice

        notes: list[str] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes

        person_url: None | str | Unset
        if isinstance(self.person_url, Unset):
            person_url = UNSET
        else:
            person_url = self.person_url

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if status is not UNSET:
            field_dict["status"] = status
        if quote is not UNSET:
            field_dict["quote"] = quote
        if engine is not UNSET:
            field_dict["engine"] = engine
        if window is not UNSET:
            field_dict["window"] = window
        if source_seconds is not UNSET:
            field_dict["source_seconds"] = source_seconds
        if subject is not UNSET:
            field_dict["subject"] = subject
        if voice is not UNSET:
            field_dict["voice"] = voice
        if notes is not UNSET:
            field_dict["notes"] = notes
        if person_url is not UNSET:
            field_dict["person_url"] = person_url
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if job is not UNSET:
            field_dict["job"] = job

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job import Job  # noqa: PLC0415
        from ..models.recast_quote import RecastQuote  # noqa: PLC0415
        from ..models.recast_subject_type_0 import RecastSubjectType0  # noqa: PLC0415
        from ..models.recast_voice_type_0 import RecastVoiceType0  # noqa: PLC0415
        from ..models.recast_window_type_0 import RecastWindowType0  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: RecastObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = RecastObject(_object_)

        dry_run = d.pop("dry_run", UNSET)

        status = d.pop("status", UNSET)

        _quote = d.pop("quote", UNSET)
        quote: RecastQuote | Unset
        if isinstance(_quote, Unset):
            quote = UNSET
        else:
            quote = RecastQuote.from_dict(_quote)

        def _parse_engine(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        engine = _parse_engine(d.pop("engine", UNSET))

        def _parse_window(data: object) -> None | RecastWindowType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_0 = RecastWindowType0.from_dict(data)

                return window_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecastWindowType0 | Unset, data)

        window = _parse_window(d.pop("window", UNSET))

        def _parse_source_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        source_seconds = _parse_source_seconds(d.pop("source_seconds", UNSET))

        def _parse_subject(data: object) -> None | RecastSubjectType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_type_0 = RecastSubjectType0.from_dict(data)

                return subject_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecastSubjectType0 | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        def _parse_voice(data: object) -> None | RecastVoiceType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_type_0 = RecastVoiceType0.from_dict(data)

                return voice_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecastVoiceType0 | Unset, data)

        voice = _parse_voice(d.pop("voice", UNSET))

        notes = cast(list[str], d.pop("notes", UNSET))

        def _parse_person_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_url = _parse_person_url(d.pop("person_url", UNSET))

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

        recast = cls(
            object_=object_,
            dry_run=dry_run,
            status=status,
            quote=quote,
            engine=engine,
            window=window,
            source_seconds=source_seconds,
            subject=subject,
            voice=voice,
            notes=notes,
            person_url=person_url,
            job_id=job_id,
            job=job,
        )

        recast.additional_properties = d
        return recast

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
