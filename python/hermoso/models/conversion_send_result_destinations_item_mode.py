from enum import StrEnum


class ConversionSendResultDestinationsItemMode(StrEnum):
    LIVE = "live"
    SKIP = "skip"
    TEST = "test"
    VALIDATE = "validate"

    def __str__(self) -> str:
        return str(self.value)
