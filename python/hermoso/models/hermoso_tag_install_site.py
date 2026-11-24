from enum import StrEnum


class HermosoTagInstallSite(StrEnum):
    GOOGLE_TAG_MANAGER = "google_tag_manager"
    MANUAL = "manual"
    SHOPIFY = "shopify"
    WORDPRESS = "wordpress"

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
