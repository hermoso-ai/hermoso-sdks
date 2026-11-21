from enum import StrEnum


class BrandListObject(StrEnum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
