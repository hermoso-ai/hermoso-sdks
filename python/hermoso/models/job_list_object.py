from enum import StrEnum


class JobListObject(StrEnum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
