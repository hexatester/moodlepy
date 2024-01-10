from typing import List, Optional

from moodle.attr import dataclass


@dataclass
class MoodleWarning:
    warningcode: str
    message: str
    item: Optional[str] = None
    itemid: Optional[int] = None

    def __str__(self) -> str:
        return self.message


@dataclass
class MoodleWarnings:
    warnings: List[MoodleWarning]
