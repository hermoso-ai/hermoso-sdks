from enum import StrEnum


class ConnectLinkObject(StrEnum):
    CONNECT_LINK = "connect_link"

    def __str__(self) -> str:
        return str(self.value)
