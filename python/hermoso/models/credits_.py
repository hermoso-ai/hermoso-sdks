from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.credits_object import CreditsObject
from typing import cast

if TYPE_CHECKING:
    from ..models.credits_limits_type_0 import CreditsLimitsType0


T = TypeVar("T", bound="Credits")


@_attrs_define
class Credits:
    """
    Attributes:
        object_ (CreditsObject | Unset):
        balance (float | Unset): Hermoso credits available to this workspace.
        plan (None | str | Unset):
        shared_workspace (bool | Unset): True when this key is acting inside a workspace owned by another account — the
            balance is then the owner’s pool, which is what your renders spend.
        limits (CreditsLimitsType0 | None | Unset): The monthly credit limits on the brand this key acts on (or the
            brand named by `?brand=`). The account owner can cap what a brand, or one member of a shared brand, spends in a
            UTC calendar month; when one would be passed, paid calls answer `429` with `error.code` `credit_limit` (and
            `Retry-After` until the reset). `limit: null` means no limit. Null here (with `limits_error`) means the read
            failed, never that there are no limits.
        limits_error (str | Unset): Present only when the limits could not be read.
    """

    object_: CreditsObject | Unset = UNSET
    balance: float | Unset = UNSET
    plan: None | str | Unset = UNSET
    shared_workspace: bool | Unset = UNSET
    limits: CreditsLimitsType0 | None | Unset = UNSET
    limits_error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.credits_limits_type_0 import CreditsLimitsType0  # noqa: PLC0415

        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        balance = self.balance

        plan: None | str | Unset
        if isinstance(self.plan, Unset):
            plan = UNSET
        else:
            plan = self.plan

        shared_workspace = self.shared_workspace

        limits: dict[str, Any] | None | Unset
        if isinstance(self.limits, Unset):
            limits = UNSET
        elif isinstance(self.limits, CreditsLimitsType0):
            limits = self.limits.to_dict()
        else:
            limits = self.limits

        limits_error = self.limits_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if balance is not UNSET:
            field_dict["balance"] = balance
        if plan is not UNSET:
            field_dict["plan"] = plan
        if shared_workspace is not UNSET:
            field_dict["shared_workspace"] = shared_workspace
        if limits is not UNSET:
            field_dict["limits"] = limits
        if limits_error is not UNSET:
            field_dict["limits_error"] = limits_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credits_limits_type_0 import CreditsLimitsType0  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: CreditsObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = CreditsObject(_object_)

        balance = d.pop("balance", UNSET)

        def _parse_plan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan = _parse_plan(d.pop("plan", UNSET))

        shared_workspace = d.pop("shared_workspace", UNSET)

        def _parse_limits(data: object) -> CreditsLimitsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                limits_type_0 = CreditsLimitsType0.from_dict(data)

                return limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreditsLimitsType0 | None | Unset, data)

        limits = _parse_limits(d.pop("limits", UNSET))

        limits_error = d.pop("limits_error", UNSET)

        credits_ = cls(
            object_=object_,
            balance=balance,
            plan=plan,
            shared_workspace=shared_workspace,
            limits=limits,
            limits_error=limits_error,
        )

        credits_.additional_properties = d
        return credits_

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
