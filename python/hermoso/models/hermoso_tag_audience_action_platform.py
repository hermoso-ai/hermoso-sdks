from enum import StrEnum


class HermosoTagAudienceActionPlatform(StrEnum):
    GOOGLE_ADS = "google_ads"
    META = "meta"
    PINTEREST_ADS = "pinterest_ads"
    SNAPCHAT_ADS = "snapchat_ads"
    X_ADS = "x_ads"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object):
        # Added by tools/sdk-generate.mjs: the API's enums grow, so an unseen value is kept rather than refused.
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = value.upper()
        member._value_ = value
        return member
