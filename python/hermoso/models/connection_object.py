from enum import StrEnum


class ConnectionObject(StrEnum):
    CONNECTION = "connection"

    def __str__(self) -> str:
        return str(self.value)
