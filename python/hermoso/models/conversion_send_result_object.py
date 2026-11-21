from enum import StrEnum


class ConversionSendResultObject(StrEnum):
    CONVERSION_SEND = "conversion_send"

    def __str__(self) -> str:
        return str(self.value)
