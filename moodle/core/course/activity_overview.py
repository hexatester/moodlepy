from datetime import datetime
from moodle.attr import dataclass
from typing import List, Optional
from moodle import MoodleWarning, ResponsesFactory


@dataclass
class Update:
    name: str  # Name of the area updated.
    itemids: List[int]  # The ids of the items updated
    timeupdated: Optional[datetime] = None  # Last time was updated


@dataclass
class Instance:
    contextlevel: str  # The context level
    id: int  # Instance id
    updates: List[Update]  # updated area


@dataclass
class ActivityOverview(ResponsesFactory[Instance]):
    instances: List[Instance]  # list of instance
    warnings: List[MoodleWarning]  # list warning

    @property
    def items(self) -> List[Instance]:
        return self.instances
