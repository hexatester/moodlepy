from typing import List, Optional

from moodle.attr import dataclass, field
from moodle.base.responses import ResponsesFactory


@dataclass
class MoodleWarning:
    item: Optional[str]
    itemid: Optional[int]
    warningcode: str
    message: str

    def __str__(self) -> str:
        return self.message


@dataclass
class MoodleWarnings(ResponsesFactory[MoodleWarning]):
    warnings: List[MoodleWarning] = field(factory=list)

    @property
    def items(self) -> List[MoodleWarning]:
        return self.warnings
