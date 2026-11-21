from enum import StrEnum


class ToolJobObject(StrEnum):
    TOOL_JOB = "tool_job"

    def __str__(self) -> str:
        return str(self.value)
