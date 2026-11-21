from enum import StrEnum


class ConversionDestinationResultObject(StrEnum):
    EVENT_DESTINATION = "event_destination"

    def __str__(self) -> str:
        return str(self.value)
