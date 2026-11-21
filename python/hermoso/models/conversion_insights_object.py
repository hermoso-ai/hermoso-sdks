from enum import StrEnum


class ConversionInsightsObject(StrEnum):
    CONVERSION_INSIGHTS = "conversion_insights"

    def __str__(self) -> str:
        return str(self.value)
