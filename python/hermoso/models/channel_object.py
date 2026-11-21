from enum import StrEnum


class ChannelObject(StrEnum):
    CHANNEL = "channel"

    def __str__(self) -> str:
        return str(self.value)
