from enum import StrEnum


class SignupStatus(StrEnum):
    AWAITING_PAYMENT = "awaiting_payment"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
