from enum import StrEnum


class JobCancelObject(StrEnum):
    JOB_CANCEL = "job_cancel"

    def __str__(self) -> str:
        return str(self.value)
