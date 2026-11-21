from enum import StrEnum


class ToolListObject(StrEnum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
