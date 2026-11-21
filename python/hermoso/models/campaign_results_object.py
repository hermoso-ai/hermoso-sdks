from enum import StrEnum


class CampaignResultsObject(StrEnum):
    CAMPAIGN_RESULTS = "campaign_results"

    def __str__(self) -> str:
        return str(self.value)
