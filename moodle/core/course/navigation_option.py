from dataclasses import dataclass
from typing import List
from moodle import ResponsesFactory, Warning


@dataclass
class NavigationOption:
    """Navigation Option
    Args:
        name (str): Option name
        available (int): Whether the option is available or not
    """
    name: str
    available: int


@dataclass
class CourseNavigation(ResponsesFactory[NavigationOption]):
    """Course
    Args:
        id (int): Course id
        options (List[NavigationOption]): list of NavigationOption
    """
    id: int
    options: List[NavigationOption]

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
    courses: List[CourseNavigation]
    warnings: List[Warning]

    @property
    def items(self) -> List[CourseNavigation]:
        return self.courses
