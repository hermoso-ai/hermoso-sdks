from enum import StrEnum


class BrandObject(StrEnum):
    BRAND = "brand"

    def __str__(self) -> str:
        return str(self.value)
