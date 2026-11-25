from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.welcome_screen_theme import WelcomeScreenTheme


T = TypeVar("T", bound="WelcomeScreen")


@_attrs_define
class WelcomeScreen:
    """
    Attributes:
        show_by_default (bool):
        brand_name (str | Unset):
        logo_url (str | Unset): https
        headline (str | Unset):
        message (str | Unset):
        theme (WelcomeScreenTheme | Unset): background, card, text, muted, accent, buttonText as #hex
    """

    show_by_default: bool
    brand_name: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    headline: str | Unset = UNSET
    message: str | Unset = UNSET
    theme: WelcomeScreenTheme | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        show_by_default = self.show_by_default

        brand_name = self.brand_name

        logo_url = self.logo_url

        headline = self.headline

        message = self.message

        theme: dict[str, Any] | Unset = UNSET
        if not isinstance(self.theme, Unset):
            theme = self.theme.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "show_by_default": show_by_default,
            }
        )
        if brand_name is not UNSET:
            field_dict["brand_name"] = brand_name
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if headline is not UNSET:
            field_dict["headline"] = headline
        if message is not UNSET:
            field_dict["message"] = message
        if theme is not UNSET:
            field_dict["theme"] = theme

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.welcome_screen_theme import WelcomeScreenTheme  # noqa: PLC0415

        d = dict(src_dict)
        show_by_default = d.pop("show_by_default")

        brand_name = d.pop("brand_name", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        headline = d.pop("headline", UNSET)

        message = d.pop("message", UNSET)

        _theme = d.pop("theme", UNSET)
        theme: WelcomeScreenTheme | Unset
        if isinstance(_theme, Unset):
            theme = UNSET
        else:
            theme = WelcomeScreenTheme.from_dict(_theme)

        welcome_screen = cls(
            show_by_default=show_by_default,
            brand_name=brand_name,
            logo_url=logo_url,
            headline=headline,
            message=message,
            theme=theme,
        )

        welcome_screen.additional_properties = d
        return welcome_screen

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
