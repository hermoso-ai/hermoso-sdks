from enum import StrEnum


class SignupCreatePeriod(StrEnum):
    MO = "mo"
    YR = "yr"

    def __str__(self) -> str:
        return str(self.value)
