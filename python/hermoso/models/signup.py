from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.signup_object import SignupObject
from ..models.signup_period import SignupPeriod
from ..models.signup_status import SignupStatus
from typing import cast

if TYPE_CHECKING:
    from ..models.contact_email import ContactEmail


T = TypeVar("T", bound="Signup")


@_attrs_define
class Signup:
    """
    Attributes:
        object_ (SignupObject | Unset):
        id (str | Unset): Pass this to POST /v1/signup/{id}/claim.
        status (SignupStatus | Unset): This enum MAY GROW — tolerate a member you have not seen.
        plan (str | Unset):
        period (SignupPeriod | Unset):
        checkout_url (None | str | Unset): Stripe’s hosted checkout. Present while payment is outstanding. A card is
            entered there, never here.
        expires_at (None | str | Unset): ISO-8601. When the checkout link stops working. Nothing is created and nothing
            is charged if it lapses.
        claim_token (None | str | Unset): Returned ONCE, by the create call. Store it before doing anything else — it is
            the only proof this signup is yours.
        api_key (None | str | Unset): Returned ONCE, on the claim that provisions the account (or on a re-claim inside
            24h, which revokes the previous key). Stored only as a hash — it can never be re-read.
        account_id (None | str | Unset):
        credits_ (float | None | Unset): The plan’s credits, already granted.
        email (ContactEmail | Unset):
        next_ (str | Unset): What to do now, in one sentence.
    """

    object_: SignupObject | Unset = UNSET
    id: str | Unset = UNSET
    status: SignupStatus | Unset = UNSET
    plan: str | Unset = UNSET
    period: SignupPeriod | Unset = UNSET
    checkout_url: None | str | Unset = UNSET
    expires_at: None | str | Unset = UNSET
    claim_token: None | str | Unset = UNSET
    api_key: None | str | Unset = UNSET
    account_id: None | str | Unset = UNSET
    credits_: float | None | Unset = UNSET
    email: ContactEmail | Unset = UNSET
    next_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        plan = self.plan

        period: str | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.value

        checkout_url: None | str | Unset
        if isinstance(self.checkout_url, Unset):
            checkout_url = UNSET
        else:
            checkout_url = self.checkout_url

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        claim_token: None | str | Unset
        if isinstance(self.claim_token, Unset):
            claim_token = UNSET
        else:
            claim_token = self.claim_token

        api_key: None | str | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        credits_: float | None | Unset
        if isinstance(self.credits_, Unset):
            credits_ = UNSET
        else:
            credits_ = self.credits_

        email: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if plan is not UNSET:
            field_dict["plan"] = plan
        if period is not UNSET:
            field_dict["period"] = period
        if checkout_url is not UNSET:
            field_dict["checkout_url"] = checkout_url
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if claim_token is not UNSET:
            field_dict["claim_token"] = claim_token
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if email is not UNSET:
            field_dict["email"] = email
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_email import ContactEmail  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: SignupObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = SignupObject(_object_)

        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: SignupStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SignupStatus(_status)

        plan = d.pop("plan", UNSET)

        _period = d.pop("period", UNSET)
        period: SignupPeriod | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = SignupPeriod(_period)

        def _parse_checkout_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checkout_url = _parse_checkout_url(d.pop("checkout_url", UNSET))

        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_claim_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        claim_token = _parse_claim_token(d.pop("claim_token", UNSET))

        def _parse_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))

        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))

        def _parse_credits_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        credits_ = _parse_credits_(d.pop("credits", UNSET))

        _email = d.pop("email", UNSET)
        email: ContactEmail | Unset
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = ContactEmail.from_dict(_email)

        next_ = d.pop("next", UNSET)

        signup = cls(
            object_=object_,
            id=id,
            status=status,
            plan=plan,
            period=period,
            checkout_url=checkout_url,
            expires_at=expires_at,
            claim_token=claim_token,
            api_key=api_key,
            account_id=account_id,
            credits_=credits_,
            email=email,
            next_=next_,
        )

        signup.additional_properties = d
        return signup

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
