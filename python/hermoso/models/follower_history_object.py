from enum import StrEnum


class FollowerHistoryObject(StrEnum):
    FOLLOWER_HISTORY = "follower_history"

    def __str__(self) -> str:
        return str(self.value)
