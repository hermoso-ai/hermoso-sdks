from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tool_object import ToolObject
from ..models.tool_rate_class import ToolRateClass
from typing import cast

if TYPE_CHECKING:
    from ..models.tool_input_schema import ToolInputSchema
    from ..models.tool_invoke import ToolInvoke


T = TypeVar("T", bound="Tool")


@_attrs_define
class Tool:
    """
    Attributes:
        object_ (ToolObject | Unset):
        name (str | Unset): Call it at POST /v1/tools/{name}.
        title (str | Unset):
        area (None | str | Unset): Which area of the product it belongs to. THIS SET MAY GROW — tolerate a member you
            have not seen.
        description (str | Unset): What it does, written for whoever is choosing: a person reading the index or a model
            reading the roster.
        read_only (bool | Unset): It reads and changes nothing. Read-only tools are metered on the READ rate-limit
            budget.
        destructive (bool | Unset): It can remove or overwrite something. Destructive tools carry their own confirmation
            arguments — read the schema.
        idempotent (bool | Unset): Calling it twice with the same arguments has the same effect as calling it once.
            Independent of `Idempotency-Key`, which protects a retry regardless.
        requires_connector (None | str | Unset): The third-party account this tool needs linked, or null when it needs
            none. Linking is a browser flow: an OAuth consent screen cannot be completed headlessly.
        connector_connected (bool | None | Unset): Whether that connector is linked in this workspace. NULL means the
            connections could not be read, which is NOT the same as "no" — never render it as a refusal.
        rate_class (ToolRateClass | Unset): Which rate-limit budget a call to it spends.
        price (None | str | Unset): What one call spends, in credits, before you run it: "free", a range by model for a
            raw generation tool ("0.4-32.5 credits by model and size"), "from N credits" for one that scales with length or
            work, or "credits vary: get_cost prices it". Every number is read live from the model catalog; send `get_cost:
            true` to a paying tool for the exact quote. NULL means it was not priced on this read.
        available (bool | Unset): Only with `include=all`: whether this workspace can call it right now (false on a tool
            that needs something first, see `unavailable_reason`). Absent from the default index, every row of which is
            callable.
        unavailable_reason (None | str | Unset): Only with `include=all`. `not_connected` (link `requires_connector`, at
            `connect_url`), `not_offered` (the platform is not offered on this server yet, so there is nothing to link) or
            `shopify_store` (it needs a Shopify store on the account). Null when `available` is true. THIS SET MAY GROW.
        connect_url (None | str | Unset): Only with `include=all`, and only on a `not_connected` row: the link a person
            opens to connect `requires_connector` to this brand. To have your own customer connect their account from your
            app, use POST /v1/connect-links instead.
        invoke (ToolInvoke | Unset):
        input_schema (ToolInputSchema | Unset): JSON Schema for the request body of POST /v1/tools/{name}. The body IS
            the argument object.
    """

    object_: ToolObject | Unset = UNSET
    name: str | Unset = UNSET
    title: str | Unset = UNSET
    area: None | str | Unset = UNSET
    description: str | Unset = UNSET
    read_only: bool | Unset = UNSET
    destructive: bool | Unset = UNSET
    idempotent: bool | Unset = UNSET
    requires_connector: None | str | Unset = UNSET
    connector_connected: bool | None | Unset = UNSET
    rate_class: ToolRateClass | Unset = UNSET
    price: None | str | Unset = UNSET
    available: bool | Unset = UNSET
    unavailable_reason: None | str | Unset = UNSET
    connect_url: None | str | Unset = UNSET
    invoke: ToolInvoke | Unset = UNSET
    input_schema: ToolInputSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        name = self.name

        title = self.title

        area: None | str | Unset
        if isinstance(self.area, Unset):
            area = UNSET
        else:
            area = self.area

        description = self.description

        read_only = self.read_only

        destructive = self.destructive

        idempotent = self.idempotent

        requires_connector: None | str | Unset
        if isinstance(self.requires_connector, Unset):
            requires_connector = UNSET
        else:
            requires_connector = self.requires_connector

        connector_connected: bool | None | Unset
        if isinstance(self.connector_connected, Unset):
            connector_connected = UNSET
        else:
            connector_connected = self.connector_connected

        rate_class: str | Unset = UNSET
        if not isinstance(self.rate_class, Unset):
            rate_class = self.rate_class.value

        price: None | str | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        available = self.available

        unavailable_reason: None | str | Unset
        if isinstance(self.unavailable_reason, Unset):
            unavailable_reason = UNSET
        else:
            unavailable_reason = self.unavailable_reason

        connect_url: None | str | Unset
        if isinstance(self.connect_url, Unset):
            connect_url = UNSET
        else:
            connect_url = self.connect_url

        invoke: dict[str, Any] | Unset = UNSET
        if not isinstance(self.invoke, Unset):
            invoke = self.invoke.to_dict()

        input_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_schema, Unset):
            input_schema = self.input_schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title
        if area is not UNSET:
            field_dict["area"] = area
        if description is not UNSET:
            field_dict["description"] = description
        if read_only is not UNSET:
            field_dict["read_only"] = read_only
        if destructive is not UNSET:
            field_dict["destructive"] = destructive
        if idempotent is not UNSET:
            field_dict["idempotent"] = idempotent
        if requires_connector is not UNSET:
            field_dict["requires_connector"] = requires_connector
        if connector_connected is not UNSET:
            field_dict["connector_connected"] = connector_connected
        if rate_class is not UNSET:
            field_dict["rate_class"] = rate_class
        if price is not UNSET:
            field_dict["price"] = price
        if available is not UNSET:
            field_dict["available"] = available
        if unavailable_reason is not UNSET:
            field_dict["unavailable_reason"] = unavailable_reason
        if connect_url is not UNSET:
            field_dict["connect_url"] = connect_url
        if invoke is not UNSET:
            field_dict["invoke"] = invoke
        if input_schema is not UNSET:
            field_dict["input_schema"] = input_schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_input_schema import ToolInputSchema  # noqa: PLC0415
        from ..models.tool_invoke import ToolInvoke  # noqa: PLC0415

        d = dict(src_dict)
        _object_ = d.pop("object", UNSET)
        object_: ToolObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = ToolObject(_object_)

        name = d.pop("name", UNSET)

        title = d.pop("title", UNSET)

        def _parse_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area = _parse_area(d.pop("area", UNSET))

        description = d.pop("description", UNSET)

        read_only = d.pop("read_only", UNSET)

        destructive = d.pop("destructive", UNSET)

        idempotent = d.pop("idempotent", UNSET)

        def _parse_requires_connector(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requires_connector = _parse_requires_connector(
            d.pop("requires_connector", UNSET)
        )

        def _parse_connector_connected(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        connector_connected = _parse_connector_connected(
            d.pop("connector_connected", UNSET)
        )

        _rate_class = d.pop("rate_class", UNSET)
        rate_class: ToolRateClass | Unset
        if isinstance(_rate_class, Unset):
            rate_class = UNSET
        else:
            rate_class = ToolRateClass(_rate_class)

        def _parse_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        available = d.pop("available", UNSET)

        def _parse_unavailable_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unavailable_reason = _parse_unavailable_reason(
            d.pop("unavailable_reason", UNSET)
        )

        def _parse_connect_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connect_url = _parse_connect_url(d.pop("connect_url", UNSET))

        _invoke = d.pop("invoke", UNSET)
        invoke: ToolInvoke | Unset
        if isinstance(_invoke, Unset):
            invoke = UNSET
        else:
            invoke = ToolInvoke.from_dict(_invoke)

        _input_schema = d.pop("input_schema", UNSET)
        input_schema: ToolInputSchema | Unset
        if isinstance(_input_schema, Unset):
            input_schema = UNSET
        else:
            input_schema = ToolInputSchema.from_dict(_input_schema)

        tool = cls(
            object_=object_,
            name=name,
            title=title,
            area=area,
            description=description,
            read_only=read_only,
            destructive=destructive,
            idempotent=idempotent,
            requires_connector=requires_connector,
            connector_connected=connector_connected,
            rate_class=rate_class,
            price=price,
            available=available,
            unavailable_reason=unavailable_reason,
            connect_url=connect_url,
            invoke=invoke,
            input_schema=input_schema,
        )

        tool.additional_properties = d
        return tool

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
