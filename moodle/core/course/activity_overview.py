from datetime import datetime
from moodle.attr import dataclass
from typing import List, Optional
from moodle import MoodleWarning, ResponsesFactory


@dataclass
class Update:
    """Update

    Args:
        name (str): Name of the area updated.
        timeupdated (Optional[datetime]): Last time was updated
        itemids (List[int]): The ids of the items updated
    """
    name: str  # Name of the area updated.
    timeupdated: Optional[datetime]  # Last time was updated
    itemids: List[int]  # The ids of the items updated

    def __str__(self):
        return self.name


@dataclass
class Instance:
    """Instance

    Args:
        contextlevel (str): The context level
        id (int): Instance id
        updates (List[Update]): updated area
    """
    contextlevel: str  # The context level
    id: int  # Instance id
    updates: List[Update]  # updated area


@dataclass
class ActivityOverview(ResponsesFactory[Instance]):
    """ActivityOverview

    Args:
        instances (List[Instance]): list of instance
        warnings (List[MoodleWarning]): list warning
    """
    instances: List[Instance]  # list of instance
    warnings: List[MoodleWarning]  # list warning

    @property
    def items(self) -> List[Instance]:
        return self.instances

    def __repr__(self):
        return repr(self.instances)
