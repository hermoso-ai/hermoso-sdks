from enum import StrEnum


class ToolObject(StrEnum):
    TOOL = "tool"

    def __str__(self) -> str:
        return str(self.value)
