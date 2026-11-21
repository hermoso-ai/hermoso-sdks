from enum import StrEnum


class DeletedObject(StrEnum):
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
