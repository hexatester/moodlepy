from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, fields


@dataclass
class ViewNotes:
    """Return type for view notes
    Constructor arguments:
    params: status (int): status: true if success
    params: warnings (List[Warning]): status: list of warnings
    """
    status: int
    warnings: List[MoodleWarning] = fields(MoodleWarning)
