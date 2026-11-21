from enum import StrEnum


class MediaObject(StrEnum):
    MEDIA = "media"

    def __str__(self) -> str:
        return str(self.value)
