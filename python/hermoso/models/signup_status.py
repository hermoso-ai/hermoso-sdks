from enum import StrEnum


class SignupStatus(StrEnum):
    AWAITING_PAYMENT = "awaiting_payment"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object):
        # Added by tools/sdk-generate.mjs: the API's enums grow, so an unseen value is kept rather than refused.
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = value.upper()
        member._value_ = value
        return member
