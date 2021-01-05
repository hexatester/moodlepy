from moodle.attr import dataclass
from typing import List
from moodle import MoodleWarning


@dataclass
class View:
    """View Resource
    Args:
        status (int): status: true if success
        warnings (List[Warning]): list of warnings
    """
    status: int
    warnings: List[MoodleWarning]

    def __bool__(self) -> bool:
        if type(self.status) == bool:
            return bool(self.status)
        return self.status == 1
