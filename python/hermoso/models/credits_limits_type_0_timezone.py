from enum import StrEnum


class CreditsLimitsType0Timezone(StrEnum):
    UTC = "UTC"

    def __str__(self) -> str:
        return str(self.value)
