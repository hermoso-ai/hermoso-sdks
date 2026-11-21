from enum import StrEnum


class SignupObject(StrEnum):
    SIGNUP = "signup"

    def __str__(self) -> str:
        return str(self.value)
