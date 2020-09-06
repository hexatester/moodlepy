from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Category:
    """Category

    Constructor arguments:
    params: id (int): category id
    params: name (str): category name
    params: idnumber (Optional[str]): category id number
    params: description (str): category description
    params: descriptionformat (int): description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
    params: parent (int): parent category id
    params: sortorder (int): category sorting order
    params: coursecount (int): number of courses in this category
    params: visible (Optional[int]): 1: available, 0:not available
    params: visibleold (Optional[int]): 1: available, 0:not available
    params: timemodified (Optional[int]): timestamp
    params: depth (int): category depth
    params: path (str): category path
    params: theme (Optional[str]): category theme

    Returns:
        Category: Category
    """
    id: int
    name: str
    idnumber: Optional[str]
    description: str
    descriptionformat: int
    parent: int
    sortorder: int
    coursecount: int
    visible: Optional[int]
    visibleold: Optional[int]
    timemodified: Optional[int]
    depth: int
    path: str
    theme: Optional[str]

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
        value: Union[str, int]
