from enum import StrEnum


class HermosoTagObject(StrEnum):
    HERMOSO_TAG = "hermoso_tag"

    def __str__(self) -> str:
        return str(self.value)
