from enum import StrEnum


class ConversionDestinationListObject(StrEnum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
