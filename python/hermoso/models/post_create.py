from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.post_create_captions_by_channel import PostCreateCaptionsByChannel
    from ..models.post_create_media_item_type_1 import PostCreateMediaItemType1
    from ..models.post_create_options import PostCreateOptions
    from ..models.post_create_targets import PostCreateTargets
    from ..models.post_create_visibility_by_channel import PostCreateVisibilityByChannel


T = TypeVar("T", bound="PostCreate")


@_attrs_define
class PostCreate:
    """
    Attributes:
        channels (list[str]): One or more channel ids from GET /v1/channels. DELIBERATELY NOT AN ENUM — the set is
            derived from what the product can publish to, and it GROWS as platform approvals land. Read it from GET
            /v1/channels rather than hard-coding it, and treat an id you have not seen as valid.
        caption (str | Unset): The post text. Per-channel length limits are enforced at create time, not discovered at
            publish time.
        title (str | Unset): The headline Pinterest and YouTube each require. Derived from the caption when omitted.
        link (str | Unset):
        media (list[PostCreateMediaItemType1 | str] | Unset): Ordered. One item is a single post; two or more are a
            carousel, in the order given. Each item is a Hermoso-hosted URL from POST /v1/media, as a bare string or as
            {url, type}.
        scheduled_at (datetime.datetime | Unset): Omit to publish immediately. Otherwise ISO-8601, at least 60 seconds
            out and within the documented horizon.
        use_queue (bool | Unset): Take the next free slot in this profile’s posting schedule instead of naming a time.
            Mutually exclusive with scheduled_at — sending both is an error, never a silent precedence.
        timezone (str | Unset): IANA zone for use_queue. Defaults to the profile’s saved zone.
        visibility (str | Unset): public (default) | unlisted | private | draft. Refused at create time where a channel
            cannot honour it, never silently downgraded at publish time.
        visibility_by_channel (PostCreateVisibilityByChannel | Unset):
        captions_by_channel (PostCreateCaptionsByChannel | Unset): Override the caption for one channel.
        targets (PostCreateTargets | Unset): Which account to post to, where the connection holds more than one. Omit
            for the default. GET /v1/channels names the field each channel uses.
        options (PostCreateOptions | Unset): Per-channel publish metadata (YouTube description, tags, categoryId,
            madeForKids, notifySubscribers, paidProductPlacement, brandPartner and a captionTrack {url|text, language, name}
            uploaded right after the video; X thread parts, Instagram alt text, and so on).
        first_comment (str | Unset): A comment the account posts on its own post right after it publishes: Facebook
            Pages, Instagram, and LinkedIn company Pages (LinkedIn needs its comments authorization, provider
            linkedin_community). Up to 2,000 characters, refused (never cut) when longer. Other channels publish the post
            without it and say so on their result. A comment that fails never undoes the post; its outcome is reported on
            the channel’s result.
    """

    channels: list[str]
    caption: str | Unset = UNSET
    title: str | Unset = UNSET
    link: str | Unset = UNSET
    media: list[PostCreateMediaItemType1 | str] | Unset = UNSET
    scheduled_at: datetime.datetime | Unset = UNSET
    use_queue: bool | Unset = UNSET
    timezone: str | Unset = UNSET
    visibility: str | Unset = UNSET
    visibility_by_channel: PostCreateVisibilityByChannel | Unset = UNSET
    captions_by_channel: PostCreateCaptionsByChannel | Unset = UNSET
    targets: PostCreateTargets | Unset = UNSET
    options: PostCreateOptions | Unset = UNSET
    first_comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_create_media_item_type_1 import PostCreateMediaItemType1  # noqa: PLC0415

        channels = self.channels

        caption = self.caption

        title = self.title

        link = self.link

        media: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item: dict[str, Any] | str
                if isinstance(media_item_data, PostCreateMediaItemType1):
                    media_item = media_item_data.to_dict()
                else:
                    media_item = media_item_data
                media.append(media_item)

        scheduled_at: str | Unset = UNSET
        if not isinstance(self.scheduled_at, Unset):
            scheduled_at = self.scheduled_at.isoformat()

        use_queue = self.use_queue

        timezone = self.timezone

        visibility = self.visibility

        visibility_by_channel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility_by_channel, Unset):
            visibility_by_channel = self.visibility_by_channel.to_dict()

        captions_by_channel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.captions_by_channel, Unset):
            captions_by_channel = self.captions_by_channel.to_dict()

        targets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = self.targets.to_dict()

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        first_comment = self.first_comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channels": channels,
            }
        )
        if caption is not UNSET:
            field_dict["caption"] = caption
        if title is not UNSET:
            field_dict["title"] = title
        if link is not UNSET:
            field_dict["link"] = link
        if media is not UNSET:
            field_dict["media"] = media
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if use_queue is not UNSET:
            field_dict["use_queue"] = use_queue
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if visibility_by_channel is not UNSET:
            field_dict["visibility_by_channel"] = visibility_by_channel
        if captions_by_channel is not UNSET:
            field_dict["captions_by_channel"] = captions_by_channel
        if targets is not UNSET:
            field_dict["targets"] = targets
        if options is not UNSET:
            field_dict["options"] = options
        if first_comment is not UNSET:
            field_dict["first_comment"] = first_comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_create_captions_by_channel import PostCreateCaptionsByChannel  # noqa: PLC0415
        from ..models.post_create_media_item_type_1 import PostCreateMediaItemType1  # noqa: PLC0415
        from ..models.post_create_options import PostCreateOptions  # noqa: PLC0415
        from ..models.post_create_targets import PostCreateTargets  # noqa: PLC0415
        from ..models.post_create_visibility_by_channel import (
            PostCreateVisibilityByChannel,
        )  # noqa: PLC0415

        d = dict(src_dict)
        channels = cast(list[str], d.pop("channels"))

        caption = d.pop("caption", UNSET)

        title = d.pop("title", UNSET)

        link = d.pop("link", UNSET)

        _media = d.pop("media", UNSET)
        media: list[PostCreateMediaItemType1 | str] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:

                def _parse_media_item(data: object) -> PostCreateMediaItemType1 | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        media_item_type_1 = PostCreateMediaItemType1.from_dict(data)

                        return media_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(PostCreateMediaItemType1 | str, data)

                media_item = _parse_media_item(media_item_data)

                media.append(media_item)

        _scheduled_at = d.pop("scheduled_at", UNSET)
        scheduled_at: datetime.datetime | Unset
        if isinstance(_scheduled_at, Unset):
            scheduled_at = UNSET
        else:
            scheduled_at = datetime.datetime.fromisoformat(_scheduled_at)

        use_queue = d.pop("use_queue", UNSET)

        timezone = d.pop("timezone", UNSET)

        visibility = d.pop("visibility", UNSET)

        _visibility_by_channel = d.pop("visibility_by_channel", UNSET)
        visibility_by_channel: PostCreateVisibilityByChannel | Unset
        if isinstance(_visibility_by_channel, Unset):
            visibility_by_channel = UNSET
        else:
            visibility_by_channel = PostCreateVisibilityByChannel.from_dict(
                _visibility_by_channel
            )

        _captions_by_channel = d.pop("captions_by_channel", UNSET)
        captions_by_channel: PostCreateCaptionsByChannel | Unset
        if isinstance(_captions_by_channel, Unset):
            captions_by_channel = UNSET
        else:
            captions_by_channel = PostCreateCaptionsByChannel.from_dict(
                _captions_by_channel
            )

        _targets = d.pop("targets", UNSET)
        targets: PostCreateTargets | Unset
        if isinstance(_targets, Unset):
            targets = UNSET
        else:
            targets = PostCreateTargets.from_dict(_targets)

        _options = d.pop("options", UNSET)
        options: PostCreateOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = PostCreateOptions.from_dict(_options)

        first_comment = d.pop("first_comment", UNSET)

        post_create = cls(
            channels=channels,
            caption=caption,
            title=title,
            link=link,
            media=media,
            scheduled_at=scheduled_at,
            use_queue=use_queue,
            timezone=timezone,
            visibility=visibility,
            visibility_by_channel=visibility_by_channel,
            captions_by_channel=captions_by_channel,
            targets=targets,
            options=options,
            first_comment=first_comment,
        )

        post_create.additional_properties = d
        return post_create

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
