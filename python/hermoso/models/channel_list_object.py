from enum import StrEnum


class ChannelListObject(StrEnum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
