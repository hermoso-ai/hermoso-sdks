from enum import StrEnum


class ConnectLinkStatus(StrEnum):
    CANCELLED = "cancelled"
    CONNECTED = "connected"
    EXPIRED = "expired"
    FAILED = "failed"
    OPENED = "opened"
    PENDING = "pending"
    REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
