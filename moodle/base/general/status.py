from dataclasses import dataclass
from typing import List

from moodle import MoodleWarning


@dataclass
class GeneralStatus:
    """GeneralStatus
    Args:
        success (int): True or False, nor 1 or 0
        warnings (List[Warning]): list of warnings
    """
    status: int
    warnings: List[MoodleWarning]
