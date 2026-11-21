from enum import StrEnum


class BestTimeObject(StrEnum):
    BEST_TIME = "best_time"

    def __str__(self) -> str:
        return str(self.value)
