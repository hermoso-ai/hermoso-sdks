from enum import StrEnum


class CreditsObject(StrEnum):
    CREDITS = "credits"

    def __str__(self) -> str:
        return str(self.value)
