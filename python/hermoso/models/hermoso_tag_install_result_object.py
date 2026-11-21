from enum import StrEnum


class HermosoTagInstallResultObject(StrEnum):
    HERMOSO_TAG_INSTALL = "hermoso_tag_install"

    def __str__(self) -> str:
        return str(self.value)
