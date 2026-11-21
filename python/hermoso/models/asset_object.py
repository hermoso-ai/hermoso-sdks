from enum import StrEnum


class AssetObject(StrEnum):
    ASSET = "asset"

    def __str__(self) -> str:
        return str(self.value)
