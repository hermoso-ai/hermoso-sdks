from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.hermoso_tag_install_site import HermosoTagInstallSite


T = TypeVar("T", bound="HermosoTagInstall")


@_attrs_define
class HermosoTagInstall:
    """
    Attributes:
        site (HermosoTagInstallSite | Unset):
        confirm (bool | Unset):
        publish (bool | Unset):
        container_path (str | Unset):
        gtm_workspace (str | Unset):
        confirm_public_id (str | Unset):
        remove (bool | Unset):
    """

    site: HermosoTagInstallSite | Unset = UNSET
    confirm: bool | Unset = UNSET
    publish: bool | Unset = UNSET
    container_path: str | Unset = UNSET
    gtm_workspace: str | Unset = UNSET
    confirm_public_id: str | Unset = UNSET
    remove: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site: str | Unset = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.value

        confirm = self.confirm

        publish = self.publish

        container_path = self.container_path

        gtm_workspace = self.gtm_workspace

        confirm_public_id = self.confirm_public_id

        remove = self.remove

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site is not UNSET:
            field_dict["site"] = site
        if confirm is not UNSET:
            field_dict["confirm"] = confirm
        if publish is not UNSET:
            field_dict["publish"] = publish
        if container_path is not UNSET:
            field_dict["container_path"] = container_path
        if gtm_workspace is not UNSET:
            field_dict["gtm_workspace"] = gtm_workspace
        if confirm_public_id is not UNSET:
            field_dict["confirm_public_id"] = confirm_public_id
        if remove is not UNSET:
            field_dict["remove"] = remove

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _site = d.pop("site", UNSET)
        site: HermosoTagInstallSite | Unset
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = HermosoTagInstallSite(_site)

        confirm = d.pop("confirm", UNSET)

        publish = d.pop("publish", UNSET)

        container_path = d.pop("container_path", UNSET)

        gtm_workspace = d.pop("gtm_workspace", UNSET)

        confirm_public_id = d.pop("confirm_public_id", UNSET)

        remove = d.pop("remove", UNSET)

        hermoso_tag_install = cls(
            site=site,
            confirm=confirm,
            publish=publish,
            container_path=container_path,
            gtm_workspace=gtm_workspace,
            confirm_public_id=confirm_public_id,
            remove=remove,
        )

        hermoso_tag_install.additional_properties = d
        return hermoso_tag_install

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
