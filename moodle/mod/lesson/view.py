from dataclasses import dataclass
from typing import List
from moodle import Warning


@dataclass
class View:
    """View Lesson
    Args:
        status (int): status: true if success
        warnings (List[Warning]): list of warnings
    """
    status: int
    warnings: List[Warning]

    def __bool__(self) -> bool:
        if type(self.status) == bool:
            return bool(self.status)
        return self.status == 1
