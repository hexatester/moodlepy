from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, field


@dataclass
class GeneralStatus:
    """GeneralStatus
    Args:
        success (int): True or False, nor 1 or 0
        warnings (List[Warning]): list of warnings
    """

    status: int
    warnings: List[MoodleWarning] = field(factory=list)
