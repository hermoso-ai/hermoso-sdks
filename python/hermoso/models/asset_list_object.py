from enum import StrEnum


class AssetListObject(StrEnum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
