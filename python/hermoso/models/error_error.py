from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.error_error_type import ErrorErrorType

if TYPE_CHECKING:
    from ..models.error_error_unknown_arguments_item import (
        ErrorErrorUnknownArgumentsItem,
    )


T = TypeVar("T", bound="ErrorError")


@_attrs_define
class ErrorError:
    """
    Attributes:
        type_ (ErrorErrorType): The coarse family — branch on this. New CODES land inside an existing type wherever
            possible so that branch keeps working; the enum is published for code generation, and a client should still fall
            through gracefully on a member it does not recognise.
        code (str): The specific reason. Log this. New values may appear at any time.
        message (str):
        param (str | Unset): The offending field, when there is one.
        connector (str | Unset): Present when the reason is a channel that is not connected. Reconnect in the app — an
            OAuth consent screen cannot be completed headlessly.
        credits_needed (float | Unset): On `insufficient_credits` from a recast or an edit: what the request needs.
        balance (float | Unset): On `insufficient_credits` from a recast or an edit: what this workspace has.
        unknown_arguments (list[ErrorErrorUnknownArgumentsItem] | Unset): On `invalid_arguments` from POST
            /v1/tools/{name}: each key the tool does not take, with the argument it most likely meant. Nothing was run.
        upgrade_url (str | Unset): On `real_face_needs_paid`: where to choose a paid plan.
        alternative (str | Unset): On `real_face_needs_paid`: the field that works on every plan instead
            (`person.describe`).
        person_url (str | Unset): On a recast with `person.describe` whose recast step was refused after the person was
            made: the AI person, in your Library. Send it as `person.image_url` to retry without making a new one.
    """

    type_: ErrorErrorType
    code: str
    message: str
    param: str | Unset = UNSET
    connector: str | Unset = UNSET
    credits_needed: float | Unset = UNSET
    balance: float | Unset = UNSET
    unknown_arguments: list[ErrorErrorUnknownArgumentsItem] | Unset = UNSET
    upgrade_url: str | Unset = UNSET
    alternative: str | Unset = UNSET
    person_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        code = self.code

        message = self.message

        param = self.param

        connector = self.connector

        credits_needed = self.credits_needed

        balance = self.balance

        unknown_arguments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unknown_arguments, Unset):
            unknown_arguments = []
            for unknown_arguments_item_data in self.unknown_arguments:
                unknown_arguments_item = unknown_arguments_item_data.to_dict()
                unknown_arguments.append(unknown_arguments_item)

        upgrade_url = self.upgrade_url

        alternative = self.alternative

        person_url = self.person_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "code": code,
                "message": message,
            }
        )
        if param is not UNSET:
            field_dict["param"] = param
        if connector is not UNSET:
            field_dict["connector"] = connector
        if credits_needed is not UNSET:
            field_dict["credits_needed"] = credits_needed
        if balance is not UNSET:
            field_dict["balance"] = balance
        if unknown_arguments is not UNSET:
            field_dict["unknown_arguments"] = unknown_arguments
        if upgrade_url is not UNSET:
            field_dict["upgrade_url"] = upgrade_url
        if alternative is not UNSET:
            field_dict["alternative"] = alternative
        if person_url is not UNSET:
            field_dict["person_url"] = person_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_error_unknown_arguments_item import (
            ErrorErrorUnknownArgumentsItem,
        )  # noqa: PLC0415

        d = dict(src_dict)
        type_ = ErrorErrorType(d.pop("type"))

        code = d.pop("code")

        message = d.pop("message")

        param = d.pop("param", UNSET)

        connector = d.pop("connector", UNSET)

        credits_needed = d.pop("credits_needed", UNSET)

        balance = d.pop("balance", UNSET)

        _unknown_arguments = d.pop("unknown_arguments", UNSET)
        unknown_arguments: list[ErrorErrorUnknownArgumentsItem] | Unset = UNSET
        if _unknown_arguments is not UNSET:
            unknown_arguments = []
            for unknown_arguments_item_data in _unknown_arguments:
                unknown_arguments_item = ErrorErrorUnknownArgumentsItem.from_dict(
                    unknown_arguments_item_data
                )

                unknown_arguments.append(unknown_arguments_item)

        upgrade_url = d.pop("upgrade_url", UNSET)

        alternative = d.pop("alternative", UNSET)

        person_url = d.pop("person_url", UNSET)

        error_error = cls(
            type_=type_,
            code=code,
            message=message,
            param=param,
            connector=connector,
            credits_needed=credits_needed,
            balance=balance,
            unknown_arguments=unknown_arguments,
            upgrade_url=upgrade_url,
            alternative=alternative,
            person_url=person_url,
        )

        error_error.additional_properties = d
        return error_error

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
