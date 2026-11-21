from enum import StrEnum


class HermosoTagEventsSentObject(StrEnum):
    HERMOSO_TAG_EVENTS_SENT = "hermoso_tag_events_sent"

    def __str__(self) -> str:
        return str(self.value)
