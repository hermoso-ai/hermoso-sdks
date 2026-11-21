from enum import StrEnum


class PostingFrequencyObject(StrEnum):
    POSTING_FREQUENCY = "posting_frequency"

    def __str__(self) -> str:
        return str(self.value)
