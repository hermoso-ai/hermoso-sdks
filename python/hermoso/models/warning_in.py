from enum import StrEnum


class WarningIn(StrEnum):
    BODY = "body"
    QUERY = "query"

    def __str__(self) -> str:
        return str(self.value)
