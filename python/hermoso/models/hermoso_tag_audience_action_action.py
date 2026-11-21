from enum import StrEnum


class HermosoTagAudienceActionAction(StrEnum):
    DELETE = "delete"
    PREVIEW = "preview"
    SAVE = "save"
    SYNC = "sync"

    def __str__(self) -> str:
        return str(self.value)
