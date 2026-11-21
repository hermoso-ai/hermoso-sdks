from enum import StrEnum


class GenerationCreateType(StrEnum):
    IMAGE = "image"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
