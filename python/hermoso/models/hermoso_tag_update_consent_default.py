from enum import StrEnum


class HermosoTagUpdateConsentDefault(StrEnum):
    DENIED = "denied"
    GRANTED = "granted"

    def __str__(self) -> str:
        return str(self.value)
