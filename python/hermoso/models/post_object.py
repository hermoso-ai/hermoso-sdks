from enum import StrEnum


class PostObject(StrEnum):
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
