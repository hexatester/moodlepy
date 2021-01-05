from typing import Optional

from moodle.attr import dataclass


@dataclass
class MoodleWarning:
    item: Optional[str]
    itemid: Optional[int]
    warningcode: str
    message: str

    def __str__(self) -> str:
        return self.message
