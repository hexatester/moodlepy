from typing import List

from moodle import ResponsesFactory, MoodleWarning
from moodle.attr import dataclass, fields


@dataclass
class NavigationOption:
    """Navigation Option
    Args:
        name (str): Option name
        available (int): Whether the option is available or not
    """
    name: str
    available: int

    def __str__(self):
        return self.name


@dataclass
class CourseNavigation(ResponsesFactory[NavigationOption]):
    """Course
    Args:
        id (int): Course id
        options (List[NavigationOption]): list of NavigationOption
    """
    id: int
    options: List[NavigationOption] = fields(NavigationOption)

    @property
    def items(self) -> List[NavigationOption]:
        return self.options


@dataclass
class NavigationOptions(ResponsesFactory[CourseNavigation]):
    """NavigationOptions
    Args:
        courses (List[CourseNavigation]): List of courses
        warnings (List[Warning]): list of warnings
    """
    courses: List[CourseNavigation] = fields(CourseNavigation)
    warnings: List[MoodleWarning] = fields(MoodleWarning)

    @property
    def items(self) -> List[CourseNavigation]:
        return self.courses

    def __repr__(self):
        return repr(self.courses)

    def __str__(self):
        return str(self.courses)
