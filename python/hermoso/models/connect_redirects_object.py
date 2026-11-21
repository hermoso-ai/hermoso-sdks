from enum import StrEnum


class ConnectRedirectsObject(StrEnum):
    CONNECT_REDIRECTS = "connect_redirects"

    def __str__(self) -> str:
        return str(self.value)
