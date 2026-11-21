from enum import StrEnum


class PostListObject(StrEnum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
