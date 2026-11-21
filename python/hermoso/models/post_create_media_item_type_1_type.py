from enum import StrEnum


class PostCreateMediaItemType1Type(StrEnum):
    IMAGE = "image"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
