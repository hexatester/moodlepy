from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class CourseCategory:
    id: int  # category id
    name: str  # category name
    idnumber: Optional[str]  # category id number
    description: str  # category description
    descriptionformat: int  # description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
    parent: int  # parent category id
    sortorder: int  # category sorting order
    coursecount: int  # number of courses in this category
    visible: Optional[int]  # 1: available, 0:not available
    visibleold: Optional[int]  # 1: available, 0:not available
    timemodified: Optional[int]  # timestamp
    depth: int  # category depth
    path: str  # category path
    theme: Optional[str]  # category theme

    def __str__(self) -> str:
        return self.name

    @staticmethod
    @dataclass
    class Criteria:
        """Criteria
        Constructor arguments::
        :param key (str): The category column to search,
            expected keys (value format) are:"id" (int) the category id,
            "ids" (string) category ids separated by commas,
            "name" (string) the category name,
            "parent" (int) the parent category id,
            "idnumber" (string) category idnumber - user must have 'moodle/category:manage' to search on idnumber,
            "visible" (int) whether the returned categories must be visible or hidden.

            If the key is not passed, then the function return all categories that the user can see.
            - user must have 'moodle/category:manage' or 'moodle/category:viewhiddencategories' to search on visible,
            "theme" (string) only return the categories having this theme - user must have 'moodle/category:manage' to search on theme
        Returns:
            Criteria: Arg for core_course_get_categories
        """
        key: str
        value: Union[str, int]  # the value to match
