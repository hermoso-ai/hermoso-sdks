from enum import StrEnum


class HermosoTagInstallSite(StrEnum):
    GOOGLE_TAG_MANAGER = "google_tag_manager"
    MANUAL = "manual"
    SHOPIFY = "shopify"
    WORDPRESS = "wordpress"

    def __str__(self) -> str:
        return str(self.value)
