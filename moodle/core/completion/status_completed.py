from dataclasses import dataclass
from typing import List
from moodle import MoodleWarning


@dataclass
class StatusCompletion:
    """Status Completion
    Args:
        status (int): status, true if success
        warnings (List[Warning]): list of warnings
    """
    status: int
    warnings: List[MoodleWarning]
