from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, field


@dataclass
class ViewEntry:
    """the blog_entries_viewed event.
    Constructor arguments:
    params: status (bool): status: true if success
    params: warnings (List[Warning]): list of warnings
    """
    status: bool
    warnings: List[MoodleWarning] = field(factory=list)
