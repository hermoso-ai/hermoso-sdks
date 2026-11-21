from enum import StrEnum


class RecastQuoteObject(StrEnum):
    QUOTE = "quote"

    def __str__(self) -> str:
        return str(self.value)
