from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_object import PostObject
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.post_captions_by_channel_type_0 import PostCaptionsByChannelType0
    from ..models.post_media_item import PostMediaItem
    from ..models.post_options import PostOptions
    from ..models.post_results_type_0_item import PostResultsType0Item
    from ..models.post_targets import PostTargets
    from ..models.post_visibility_by_channel_type_0 import PostVisibilityByChannelType0


T = TypeVar("T", bound="Post")


@_attrs_define
class Post:
    """
    Attributes:
        object_ (PostObject | Unset):
        id (str | Unset):
        status (str | Unset): scheduled | processing | published | partially_published | failed | indeterminate. THIS
            SET MAY GROW — tolerate an unknown value. `indeterminate` means a restart interrupted the send and we cannot say
            whether it published: check the channel rather than assuming either way. `failed` is only ever used when we know
            nothing published.
        scheduled_at (datetime.datetime | None | Unset):
        created_at (datetime.datetime | None | Unset):
        channels (list[str] | Unset):
        caption (str | Unset):
        title (str | Unset):
        title_effective (str | Unset): The headline actually going out — derived from the caption when you named none.
        link (str | Unset):
        media (list[PostMediaItem] | Unset):
        captions_by_channel (None | PostCaptionsByChannelType0 | Unset):
        visibility (str | Unset):
        visibility_by_channel (None | PostVisibilityByChannelType0 | Unset):
        targets (PostTargets | Unset): Which account this goes to, per channel (Page, board, LinkedIn Page, Business
            listing). Unset means the connection’s default.
        options (PostOptions | Unset):
        results (list[PostResultsType0Item] | None | Unset): Per-channel outcome once fired. A partial failure is normal
            and is reported here — the top-level status then says `partially_published`, never a flat `failed`.
        retry_of (None | str | Unset):
        status_detail (None | str | Unset): Present when the status alone would mislead. Set for `indeterminate`.
        content_lost (bool | Unset):
    """

    object_: PostObject | Unset = UNSET
    id: str | Unset = UNSET
    status: str | Unset = UNSET
    scheduled_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    channels: list[str] | Unset = UNSET
    caption: str | Unset = UNSET
    title: str | Unset = UNSET
    title_effective: str | Unset = UNSET
    link: str | Unset = UNSET
    media: list[PostMediaItem] | Unset = UNSET
    captions_by_channel: None | PostCaptionsByChannelType0 | Unset = UNSET
    visibility: str | Unset = UNSET
    visibility_by_channel: None | PostVisibilityByChannelType0 | Unset = UNSET
    targets: PostTargets | Unset = UNSET
    options: PostOptions | Unset = UNSET
    results: list[PostResultsType0Item] | None | Unset = UNSET
    retry_of: None | str | Unset = UNSET
    status_detail: None | str | Unset = UNSET
    content_lost: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_captions_by_channel_type_0 import PostCaptionsByChannelType0  # noqa: PLC0415
        from ..models.post_visibility_by_channel_type_0 import (
            PostVisibilityByChannelType0,
        )  # noqa: PLC0415

        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        status = self.status

        scheduled_at: None | str | Unset
        if isinstance(self.scheduled_at, Unset):
            scheduled_at = UNSET
        elif isinstance(self.scheduled_at, datetime.datetime):
            scheduled_at = self.scheduled_at.isoformat()
        else:
            scheduled_at = self.scheduled_at

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        channels: list[str] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels

        caption = self.caption

        title = self.title

        title_effective = self.title_effective

        link = self.link

        media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        captions_by_channel: dict[str, Any] | None | Unset
        if isinstance(self.captions_by_channel, Unset):
            captions_by_channel = UNSET
        elif isinstance(self.captions_by_channel, PostCaptionsByChannelType0):
            captions_by_channel = self.captions_by_channel.to_dict()
        else:
            captions_by_channel = self.captions_by_channel

        visibility = self.visibility

        visibility_by_channel: dict[str, Any] | None | Unset
        if isinstance(self.visibility_by_channel, Unset):
            visibility_by_channel = UNSET
        elif isinstance(self.visibility_by_channel, PostVisibilityByChannelType0):
            visibility_by_channel = self.visibility_by_channel.to_dict()
        else:
            visibility_by_channel = self.visibility_by_channel

        targets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = self.targets.to_dict()

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        results: list[dict[str, Any]] | None | Unset
        if isinstance(self.results, Unset):
            results = UNSET
        elif isinstance(self.results, list):
            results = []
            for results_type_0_item_data in self.results:
                results_type_0_item = results_type_0_item_data.to_dict()
                results.append(results_type_0_item)

        else:
            results = self.results

        retry_of: None | str | Unset
        if isinstance(self.retry_of, Unset):
            retry_of = UNSET
        else:
            retry_of = self.retry_of

        status_detail: None | str | Unset
        if isinstance(self.status_detail, Unset):
            status_detail = UNSET
        else:
            status_detail = self.status_detail

        content_lost = self.content_lost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if channels is not UNSET:
            field_dict["channels"] = channels
        if caption is not UNSET:
            field_dict["caption"] = caption
        if title is not UNSET:
            field_dict["title"] = title
        if title_effective is not UNSET:
            field_dict["title_effective"] = title_effective
        if link is not UNSET:
            field_dict["link"] = link
        if media is not UNSET:
            field_dict["media"] = media
        if captions_by_channel is not UNSET:
            field_dict["captions_by_channel"] = captions_by_channel
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if visibility_by_channel is not UNSET:
            field_dict["visibility_by_channel"] = visibility_by_channel
        if targets is not UNSET:
            field_dict["targets"] = targets
        if options is not UNSET:
            field_dict["options"] = options
        if results is not UNSET:
            field_dict["results"] = results
        if retry_of is not UNSET:
            field_dict["retry_of"] = retry_of
        if status_detail is not UNSET:
            field_dict["status_detail"] = status_detail
        if content_lost is not UNSET:
            field_dict["content_lost"] = content_lost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_captions_by_channel_type_0 import PostCaptionsByChannelType0  # noqa: PLC0415
        from ..models.post_media_item import PostMediaItem  # noqa: PLC0415
        from ..models.post_options import PostOptions  # noqa: PLC0415
        from ..models.post_results_type_0_item import PostResultsType0Item  # noqa: PLC0415
        from ..models.post_targets import PostTargets  # noqa: PLC0415
        from ..models.post_visibility_by_channel_type_0 import (
            PostVisibilityByChannelType0,
        )  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: PostObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = PostObject(_object_)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        def _parse_scheduled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_at_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_at = _parse_scheduled_at(d.pop("scheduled_at", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        channels = cast(list[str], d.pop("channels", UNSET))

        caption = d.pop("caption", UNSET)

        title = d.pop("title", UNSET)

        title_effective = d.pop("title_effective", UNSET)

        link = d.pop("link", UNSET)

        _media = d.pop("media", UNSET)
        media: list[PostMediaItem] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = PostMediaItem.from_dict(media_item_data)

                media.append(media_item)

        def _parse_captions_by_channel(
            data: object,
        ) -> None | PostCaptionsByChannelType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                captions_by_channel_type_0 = PostCaptionsByChannelType0.from_dict(data)

                return captions_by_channel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostCaptionsByChannelType0 | Unset, data)

        captions_by_channel = _parse_captions_by_channel(
            d.pop("captions_by_channel", UNSET)
        )

        visibility = d.pop("visibility", UNSET)

        def _parse_visibility_by_channel(
            data: object,
        ) -> None | PostVisibilityByChannelType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                visibility_by_channel_type_0 = PostVisibilityByChannelType0.from_dict(
                    data
                )

                return visibility_by_channel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostVisibilityByChannelType0 | Unset, data)

        visibility_by_channel = _parse_visibility_by_channel(
            d.pop("visibility_by_channel", UNSET)
        )

        _targets = d.pop("targets", UNSET)
        targets: PostTargets | Unset
        if isinstance(_targets, Unset):
            targets = UNSET
        else:
            targets = PostTargets.from_dict(_targets)

        _options = d.pop("options", UNSET)
        options: PostOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = PostOptions.from_dict(_options)

        def _parse_results(data: object) -> list[PostResultsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                results_type_0 = []
                _results_type_0 = data
                for results_type_0_item_data in _results_type_0:
                    results_type_0_item = PostResultsType0Item.from_dict(
                        results_type_0_item_data
                    )

                    results_type_0.append(results_type_0_item)

                return results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PostResultsType0Item] | None | Unset, data)

        results = _parse_results(d.pop("results", UNSET))

        def _parse_retry_of(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retry_of = _parse_retry_of(d.pop("retry_of", UNSET))

        def _parse_status_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_detail = _parse_status_detail(d.pop("status_detail", UNSET))

        content_lost = d.pop("content_lost", UNSET)

        post = cls(
            object_=object_,
            id=id,
            status=status,
            scheduled_at=scheduled_at,
            created_at=created_at,
            channels=channels,
            caption=caption,
            title=title,
            title_effective=title_effective,
            link=link,
            media=media,
            captions_by_channel=captions_by_channel,
            visibility=visibility,
            visibility_by_channel=visibility_by_channel,
            targets=targets,
            options=options,
            results=results,
            retry_of=retry_of,
            status_detail=status_detail,
            content_lost=content_lost,
        )

        post.additional_properties = d
        return post

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
