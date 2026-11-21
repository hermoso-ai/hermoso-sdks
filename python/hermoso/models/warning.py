from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.warning_in import WarningIn
from typing import cast


T = TypeVar("T", bound="Warning_")


@_attrs_define
class Warning_:
    """Something about the request that did not stop it but probably did not do what you meant. Today: a query parameter or
    body field this operation does not take, which was IGNORED. Any response, success or error, may carry `warnings`;
    read it in development and fix what it names. THIS SET OF CODES MAY GROW.

        Attributes:
            code (str | Unset): `unknown_parameter` (a query parameter) or `unknown_field` (a JSON body field).
            param (str | Unset): The name you sent.
            in_ (WarningIn | Unset):
            did_you_mean (None | str | Unset): The parameter of THIS operation you most likely meant.
            valid (list[str] | Unset): Every name this operation takes there.
            message (str | Unset):
    """

    code: str | Unset = UNSET
    param: str | Unset = UNSET
    in_: WarningIn | Unset = UNSET
    did_you_mean: None | str | Unset = UNSET
    valid: list[str] | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        param = self.param

        in_: str | Unset = UNSET
        if not isinstance(self.in_, Unset):
            in_ = self.in_.value

        did_you_mean: None | str | Unset
        if isinstance(self.did_you_mean, Unset):
            did_you_mean = UNSET
        else:
            did_you_mean = self.did_you_mean

        valid: list[str] | Unset = UNSET
        if not isinstance(self.valid, Unset):
            valid = self.valid

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if param is not UNSET:
            field_dict["param"] = param
        if in_ is not UNSET:
            field_dict["in"] = in_
        if did_you_mean is not UNSET:
            field_dict["did_you_mean"] = did_you_mean
        if valid is not UNSET:
            field_dict["valid"] = valid
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        param = d.pop("param", UNSET)

        _in_ = d.pop("in", UNSET)
        in_: WarningIn | Unset
        if isinstance(_in_, Unset):
            in_ = UNSET
        else:
            in_ = WarningIn(_in_)

        def _parse_did_you_mean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        did_you_mean = _parse_did_you_mean(d.pop("did_you_mean", UNSET))

        valid = cast(list[str], d.pop("valid", UNSET))

        message = d.pop("message", UNSET)

        warning = cls(
            code=code,
            param=param,
            in_=in_,
            did_you_mean=did_you_mean,
            valid=valid,
            message=message,
        )

        warning.additional_properties = d
        return warning

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
