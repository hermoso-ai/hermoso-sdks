from enum import StrEnum


class HermosoTagUpdateAction(StrEnum):
    SERVER_KEY = "server_key"
    STRIPE = "stripe"
    UPDATE = "update"
    VERIFY = "verify"

    def __str__(self) -> str:
        return str(self.value)
