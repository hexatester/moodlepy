from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional
from moodle import Warning, ResponsesFactory


@dataclass
class Update:
    name: str  # Name of the area updated.
    timeupdated: Optional[datetime]  # Last time was updated
    itemids: List[int]  # The ids of the items updated


@dataclass
class Instance:
    contextlevel: str  # The context level
    id: int  # Instance id
    updates: List[Update]  # updated area


@dataclass
class ActivityOverview(ResponsesFactory[Instance]):
    instances: List[Instance]  # list of instance
    warnings: List[Warning]  # list warning

    @property
    def items(self) -> List[Instance]:
        return self.instances
