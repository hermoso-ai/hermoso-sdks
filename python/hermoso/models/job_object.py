from enum import StrEnum


class JobObject(StrEnum):
    JOB = "job"

    def __str__(self) -> str:
        return str(self.value)
