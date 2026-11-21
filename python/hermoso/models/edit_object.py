from enum import StrEnum


class EditObject(StrEnum):
    EDIT = "edit"

    def __str__(self) -> str:
        return str(self.value)
