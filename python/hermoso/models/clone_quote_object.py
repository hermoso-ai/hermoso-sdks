from enum import StrEnum


class CloneQuoteObject(StrEnum):
    QUOTE = "quote"

    def __str__(self) -> str:
        return str(self.value)
