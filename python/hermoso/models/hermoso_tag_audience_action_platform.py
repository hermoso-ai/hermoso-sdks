from enum import StrEnum


class HermosoTagAudienceActionPlatform(StrEnum):
    GOOGLE_ADS = "google_ads"
    META = "meta"
    PINTEREST_ADS = "pinterest_ads"
    SNAPCHAT_ADS = "snapchat_ads"
    X_ADS = "x_ads"

    def __str__(self) -> str:
        return str(self.value)
