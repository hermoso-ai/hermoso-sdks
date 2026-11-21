from enum import StrEnum


class InboxStatsObject(StrEnum):
    INBOX_STATS = "inbox_stats"

    def __str__(self) -> str:
        return str(self.value)
