from enum import StrEnum


class EditQuoteObject(StrEnum):
    QUOTE = "quote"

    def __str__(self) -> str:
        return str(self.value)
