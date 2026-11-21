from enum import StrEnum


class ProfitSettingsObject(StrEnum):
    PROFIT_SETTINGS = "profit_settings"

    def __str__(self) -> str:
        return str(self.value)
