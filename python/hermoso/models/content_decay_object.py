from enum import StrEnum


class ContentDecayObject(StrEnum):
    CONTENT_DECAY = "content_decay"

    def __str__(self) -> str:
        return str(self.value)
