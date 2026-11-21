from enum import StrEnum


class CloneQuoteRequestType(StrEnum):
    IMAGE = "image"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
