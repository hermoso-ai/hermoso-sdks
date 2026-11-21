from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.signup_create_period import SignupCreatePeriod


T = TypeVar("T", bound="SignupCreate")


@_attrs_define
class SignupCreate:
    """
    Attributes:
        plan (str): A PAID plan id — see GET /v1/signup/plans-equivalent on hermoso.ai/pricing, currently starter, pro
            or studio. The free plan is refused here by name: this path provisions an account only against a completed
            payment.
        email (str): REQUIRED: a real mailbox for the human this account belongs to. A verification link is emailed
            there; the account works before it is clicked, and verifying only decides whether we may mail the address
            (receipts, low-credit alerts, replies to bug reports). It is NEVER the account identity: it cannot sign in to
            this account, and it can never link or merge this account with one that already uses the address. Hermoso
            synthetic addresses are refused (400 `email_invalid`).
        period (SignupCreatePeriod | Unset): Billing cadence. Defaults to `mo`.
    """

    plan: str
    email: str
    period: SignupCreatePeriod | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan = self.plan

        email = self.email

        period: str | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan": plan,
                "email": email,
            }
        )
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plan = d.pop("plan")

        email = d.pop("email")

        _period = d.pop("period", UNSET)
        period: SignupCreatePeriod | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = SignupCreatePeriod(_period)

        signup_create = cls(
            plan=plan,
            email=email,
            period=period,
        )

        signup_create.additional_properties = d
        return signup_create

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
