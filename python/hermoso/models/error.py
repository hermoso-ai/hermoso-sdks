from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.error_error import ErrorError
    from ..models.warning import Warning_


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """
    Attributes:
        error (ErrorError):
        request_id (None | str | Unset):
        warnings (list[Warning_] | Unset): Present when the request also carried a parameter or field this operation
            does not take. Often the reason for the error (a misnamed field reads as a missing one).
    """

    error: ErrorError
    request_id: None | str | Unset = UNSET
    warnings: list[Warning_] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        request_id: None | str | Unset
        if isinstance(self.request_id, Unset):
            request_id = UNSET
        else:
            request_id = self.request_id

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_error import ErrorError  # noqa: PLC0415
        from ..models.warning import Warning_  # noqa: PLC0415

        d = dict(src_dict)
        error = ErrorError.from_dict(d.pop("error"))

        def _parse_request_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_id = _parse_request_id(d.pop("request_id", UNSET))

        _warnings = d.pop("warnings", UNSET)
        warnings: list[Warning_] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = Warning_.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        error = cls(
            error=error,
            request_id=request_id,
            warnings=warnings,
        )

        error.additional_properties = d
        return error

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
