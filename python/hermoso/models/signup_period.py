from enum import StrEnum


class SignupPeriod(StrEnum):
    MO = "mo"
    YR = "yr"

    def __str__(self) -> str:
        return str(self.value)
