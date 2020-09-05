from dataclasses import dataclass
from typing import Iterator, List, Optional
from moodle import Warning


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
    updates: List[CourseUpdate]

    def __len__(self) -> int:
        return len(self.updates)

    def __iter__(self) -> Iterator[CourseUpdate]:
        return iter(self.updates)

    def __getitem__(self, slice: int) -> CourseUpdate:
        return self.updates[slice]


@dataclass
class CheckUpdate:
    instances: List[UpdateInstance]
    warnings: List[Warning]

    def __len__(self) -> int:
        return len(self.instances)

    def __iter__(self) -> Iterator[UpdateInstance]:
        return iter(self.instances)

    def __getitem__(self, slice: int) -> UpdateInstance:
        return self.instances[slice]
