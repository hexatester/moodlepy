from dataclasses import dataclass
from typing import List
from moodle import Warning, ResponsesFactory


@dataclass
class AllowedEventTypes(ResponsesFactory[str]):
    """The type of events a user can create in the given course.
    Constructor arguments:
    allowedeventtypes: List[str]
    warnings: List[Warning]
    """
    allowedeventtypes: List[str]
    warnings: List[Warning]
