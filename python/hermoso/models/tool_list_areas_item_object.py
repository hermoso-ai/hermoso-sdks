from enum import StrEnum


class ToolListAreasItemObject(StrEnum):
    TOOL_AREA = "tool_area"

    def __str__(self) -> str:
        return str(self.value)
