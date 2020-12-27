from dataclasses import dataclass
from typing import Optional


@dataclass
class MoodleWarning:
    item: Optional[str]
    itemid: Optional[int]
    warningcode: str
    message: str

    def __str__(self) -> str:
        return self.message
