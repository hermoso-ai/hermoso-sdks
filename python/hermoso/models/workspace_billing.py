from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.workspace_billing_object import WorkspaceBillingObject
from typing import cast

if TYPE_CHECKING:
    from ..models.workspace_billing_wallet_type_0 import WorkspaceBillingWalletType0


T = TypeVar("T", bound="WorkspaceBilling")


@_attrs_define
class WorkspaceBilling:
    """
    Attributes:
        object_ (WorkspaceBillingObject | Unset):
        brand (str | Unset):
        name (str | Unset):
        billed_separately (bool | Unset):
        external_id (None | str | Unset):
        wallet (None | Unset | WorkspaceBillingWalletType0):
        needs_confirm (bool | Unset):
        note (str | Unset):
    """

    object_: WorkspaceBillingObject | Unset = UNSET
    brand: str | Unset = UNSET
    name: str | Unset = UNSET
    billed_separately: bool | Unset = UNSET
    external_id: None | str | Unset = UNSET
    wallet: None | Unset | WorkspaceBillingWalletType0 = UNSET
    needs_confirm: bool | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workspace_billing_wallet_type_0 import WorkspaceBillingWalletType0  # noqa: PLC0415

        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        brand = self.brand

        name = self.name

        billed_separately = self.billed_separately

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        wallet: dict[str, Any] | None | Unset
        if isinstance(self.wallet, Unset):
            wallet = UNSET
        elif isinstance(self.wallet, WorkspaceBillingWalletType0):
            wallet = self.wallet.to_dict()
        else:
            wallet = self.wallet

        needs_confirm = self.needs_confirm

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if brand is not UNSET:
            field_dict["brand"] = brand
        if name is not UNSET:
            field_dict["name"] = name
        if billed_separately is not UNSET:
            field_dict["billed_separately"] = billed_separately
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if wallet is not UNSET:
            field_dict["wallet"] = wallet
        if needs_confirm is not UNSET:
            field_dict["needs_confirm"] = needs_confirm
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workspace_billing_wallet_type_0 import WorkspaceBillingWalletType0  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: WorkspaceBillingObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = WorkspaceBillingObject(_object_)

        brand = d.pop("brand", UNSET)

        name = d.pop("name", UNSET)

        billed_separately = d.pop("billed_separately", UNSET)

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_wallet(data: object) -> None | Unset | WorkspaceBillingWalletType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                wallet_type_0 = WorkspaceBillingWalletType0.from_dict(data)

                return wallet_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkspaceBillingWalletType0, data)

        wallet = _parse_wallet(d.pop("wallet", UNSET))

        needs_confirm = d.pop("needs_confirm", UNSET)

        note = d.pop("note", UNSET)

        workspace_billing = cls(
            object_=object_,
            brand=brand,
            name=name,
            billed_separately=billed_separately,
            external_id=external_id,
            wallet=wallet,
            needs_confirm=needs_confirm,
            note=note,
        )

        workspace_billing.additional_properties = d
        return workspace_billing

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
