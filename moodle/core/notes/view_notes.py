from dataclasses import dataclass
from typing import List
from moodle import MoodleWarning


@dataclass
class ViewNotes:
    """Return type for view notes
    Constructor arguments:
    params: status (int): status: true if success
    params: warnings (List[Warning]): status: list of warnings
    """
    status: int
    warnings: List[MoodleWarning]
