from enum import StrEnum


class EditCreateLighting(StrEnum):
    AUTO = "auto"
    PRESERVE = "preserve"
    RELIGHT = "relight"

    def __str__(self) -> str:
        return str(self.value)
