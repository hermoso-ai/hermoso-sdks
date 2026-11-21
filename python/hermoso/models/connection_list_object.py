from enum import StrEnum


class ConnectionListObject(StrEnum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
