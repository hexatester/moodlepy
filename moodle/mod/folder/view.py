from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, field


@dataclass
class View:
    """View Folder
    Args:
        status (int): status: true if success
        warnings (List[Warning]): list of warnings
    """

    status: int
    warnings: List[MoodleWarning] = field(factory=list)

    def __bool__(self) -> bool:
        if type(self.status) == bool:
            return bool(self.status)
        return self.status == 1
