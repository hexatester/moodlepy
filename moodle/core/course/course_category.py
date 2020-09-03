from dataclasses import dataclass
from moodle import MoodleObject


@dataclass
class CourseCategory(MoodleObject):
    id: int
    name: str
    description: str
    descriptionformat: int
    parent: int
    sortorder: int
    coursecount: int
    depth: int
    path: str

    def __str__(self) -> str:
        return self.name
