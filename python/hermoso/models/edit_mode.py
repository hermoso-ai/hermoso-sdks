from enum import StrEnum


class EditMode(StrEnum):
    CLIP = "clip"
    PREVIEW = "preview"

    def __str__(self) -> str:
        return str(self.value)
