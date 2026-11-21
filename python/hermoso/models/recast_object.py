from enum import StrEnum


class RecastObject(StrEnum):
    RECAST = "recast"

    def __str__(self) -> str:
        return str(self.value)
