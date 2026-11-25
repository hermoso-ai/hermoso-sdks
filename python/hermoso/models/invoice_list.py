from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invoice_list_object import InvoiceListObject

if TYPE_CHECKING:
    from ..models.invoice_list_invoices_item import InvoiceListInvoicesItem
    from ..models.invoice_list_receipts_item import InvoiceListReceiptsItem


T = TypeVar("T", bound="InvoiceList")


@_attrs_define
class InvoiceList:
    """
    Attributes:
        object_ (InvoiceListObject | Unset):
        invoices (list[InvoiceListInvoicesItem] | Unset):
        receipts (list[InvoiceListReceiptsItem] | Unset):
        note (str | Unset):
    """

    object_: InvoiceListObject | Unset = UNSET
    invoices: list[InvoiceListInvoicesItem] | Unset = UNSET
    receipts: list[InvoiceListReceiptsItem] | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        invoices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invoices, Unset):
            invoices = []
            for invoices_item_data in self.invoices:
                invoices_item = invoices_item_data.to_dict()
                invoices.append(invoices_item)

        receipts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.receipts, Unset):
            receipts = []
            for receipts_item_data in self.receipts:
                receipts_item = receipts_item_data.to_dict()
                receipts.append(receipts_item)

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if invoices is not UNSET:
            field_dict["invoices"] = invoices
        if receipts is not UNSET:
            field_dict["receipts"] = receipts
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_list_invoices_item import InvoiceListInvoicesItem  # noqa: PLC0415
        from ..models.invoice_list_receipts_item import InvoiceListReceiptsItem  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: InvoiceListObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = InvoiceListObject(_object_)

        _invoices = d.pop("invoices", UNSET)
        invoices: list[InvoiceListInvoicesItem] | Unset = UNSET
        if _invoices is not UNSET:
            invoices = []
            for invoices_item_data in _invoices:
                invoices_item = InvoiceListInvoicesItem.from_dict(invoices_item_data)

                invoices.append(invoices_item)

        _receipts = d.pop("receipts", UNSET)
        receipts: list[InvoiceListReceiptsItem] | Unset = UNSET
        if _receipts is not UNSET:
            receipts = []
            for receipts_item_data in _receipts:
                receipts_item = InvoiceListReceiptsItem.from_dict(receipts_item_data)

                receipts.append(receipts_item)

        note = d.pop("note", UNSET)

        invoice_list = cls(
            object_=object_,
            invoices=invoices,
            receipts=receipts,
            note=note,
        )

        invoice_list.additional_properties = d
        return invoice_list

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
