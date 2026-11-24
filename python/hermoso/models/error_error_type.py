from enum import StrEnum


class ErrorErrorType(StrEnum):
    API_ERROR = "api_error"
    AUTHENTICATION_ERROR = "authentication_error"
    CONNECTOR_ERROR = "connector_error"
    INSUFFICIENT_CREDITS = "insufficient_credits"
    INVALID_REQUEST_ERROR = "invalid_request_error"
    PERMISSION_ERROR = "permission_error"
    RATE_LIMIT_ERROR = "rate_limit_error"

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
