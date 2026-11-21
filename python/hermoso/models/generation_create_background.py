from enum import StrEnum


class GenerationCreateBackground(StrEnum):
    TRANSPARENT = "transparent"

    def __str__(self) -> str:
        return str(self.value)
