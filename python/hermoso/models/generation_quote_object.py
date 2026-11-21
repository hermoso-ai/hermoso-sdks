from enum import StrEnum


class GenerationQuoteObject(StrEnum):
    QUOTE = "quote"

    def __str__(self) -> str:
        return str(self.value)
