from enum import StrEnum


class HermosoTagAudiencesObject(StrEnum):
    HERMOSO_TAG_AUDIENCES = "hermoso_tag_audiences"

    def __str__(self) -> str:
        return str(self.value)
