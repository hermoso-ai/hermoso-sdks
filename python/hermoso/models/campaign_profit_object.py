from enum import StrEnum


class CampaignProfitObject(StrEnum):
    CAMPAIGN_PROFIT = "campaign_profit"

    def __str__(self) -> str:
        return str(self.value)
