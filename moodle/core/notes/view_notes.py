from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, field


@dataclass
class ViewNotes:
    """Return type for view notes
    Constructor arguments:
    params: status (int): status: true if success
    params: warnings (List[Warning]): status: list of warnings
    """

    status: int
    warnings: List[MoodleWarning] = field(factory=list)
