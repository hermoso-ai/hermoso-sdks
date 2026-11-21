from enum import StrEnum


class HermosoTagReportObject(StrEnum):
    HERMOSO_TAG_REPORT = "hermoso_tag_report"

    def __str__(self) -> str:
        return str(self.value)
