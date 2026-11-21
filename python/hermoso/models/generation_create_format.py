from enum import StrEnum


class GenerationCreateFormat(StrEnum):
    GIF = "gif"
    PNG = "png"
    SVG = "svg"

    def __str__(self) -> str:
        return str(self.value)
