from enum import StrEnum


class ConnectionDeletedObject(StrEnum):
    CONNECTION = "connection"

    def __str__(self) -> str:
        return str(self.value)
