from typing import List, Optional

from moodle.attr import dataclass


@dataclass
class MoodleWarning:
    item: Optional[str]
    itemid: Optional[int]
    warningcode: str
    message: str

    def __str__(self) -> str:
        return self.message


@dataclass
class MoodleWarnings:
    warnings: List[MoodleWarning]
