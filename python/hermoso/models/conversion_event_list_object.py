from enum import StrEnum


class ConversionEventListObject(StrEnum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
