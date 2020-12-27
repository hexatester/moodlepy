from dataclasses import dataclass
from typing import List

from moodle import MoodleWarning


@dataclass
class GeneralSuccess:
    """GeneralSuccess
    Args:
        success (int): True or False, nor 1 or 0
        warnings (List[Warning]): list of warnings
    """
    success: int
    warnings: List[MoodleWarning]

    def __bool__(self) -> bool:
        if isinstance(self.success, int):
            return self.success == 1
        elif isinstance(self.success, str):
            return self.success == '1' or self.success == 'true'
        return bool(self.success)
