from dataclasses import dataclass, field
from typing import List
from moodle import MoodleWarning


@dataclass
class ViewEntry:
    """the blog_entries_viewed event.
    Constructor arguments:
    params: status (bool): status: true if success
    params: warnings (List[Warning]): list of warnings
    """
    status: bool
    warnings: List[MoodleWarning] = field(default_factory=list)
