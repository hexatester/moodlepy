from typing import Iterator, List, Optional

from moodle import MoodleWarning, ResponsesFactory
from moodle.attr import dataclass, field


@dataclass
class CourseUpdate:
    name: str  # Name of the area updated.
    timeupdated: Optional[int]  # Last time was updated
    itemids: List[int]  # The ids of the items updated

    def __len__(self) -> int:
        return len(self.itemids)

    def __iter__(self) -> Iterator[int]:
        return iter(self.itemids)


@dataclass
class UpdateInstance:
    contextlevel: str  # The context level
    id: int  # Instance id
    updates: List[CourseUpdate] = field(factory=list)

    def __len__(self) -> int:
        return len(self.updates)

    def __iter__(self) -> Iterator[CourseUpdate]:
        return iter(self.updates)

    def __getitem__(self, slice: int) -> CourseUpdate:
        return self.updates[slice]


@dataclass
class CheckUpdate(ResponsesFactory[UpdateInstance]):
    instances: List[UpdateInstance] = field(factory=list)
    warnings: List[MoodleWarning] = field(factory=list)

    @property
    def items(self) -> List[UpdateInstance]:
        return self.instances

    @dataclass
    class ToCheck:
        """Instances to check
        Constructor arguments:
        params: contextlevel (str): The context level for the file location. Only module supported right now.
        params: id (int): Context instance id
        params: since (int): Check updates since this time stamp
        """

        contextlevel: str
        id: int
        since: int
