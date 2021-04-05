from typing import List

from moodle import MoodleWarning, ResponsesFactory
from moodle.attr import dataclass, field


@dataclass
class AllowedEventTypes(ResponsesFactory[str]):
    """The type of events a user can create in the given course.

    Args:
        allowedeventtypes (List[str]): list of allowed event type
        warnings (List[Warning]): list of MoodleWarning
    """
    allowedeventtypes: List[str] = field(factory=list)
    warnings: List[MoodleWarning] = field(factory=list)
