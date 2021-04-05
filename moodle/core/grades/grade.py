from typing import List

from moodle.attr import dataclass, field


@dataclass
class Grade:
    """Grade

    Args:
        userid (int): Student ID
        grade (float): Student grade
        locked (int): 0 means not locked, > 1 is a date to lock until
        hidden (int): 0 means not hidden, 1 hidden, > 1 is a date to hide until
        overridden (int): 0 means not overridden, > 1 means overridden
        feedback (str): Feedback from the grader
        feedbackformat (int): The format of the feedback
        usermodified (int): The ID of the last user to modify this student grade
        datesubmitted (int): A timestamp indicating when the student submitted the activity
        dategraded (int): A timestamp indicating when the assignment was grades
        str_grade (str): A string representation of the grade
        str_long_grade (str): A nicely formatted string representation of the grade
        str_feedback (str): A formatted string representation of the feedback from the grader
    """
    userid: int
    grade: float
    locked: int
    hidden: int
    overridden: int
    feedback: str
    feedbackformat: int
    usermodified: int
    datesubmitted: int
    dategraded: int
    str_grade: str
    str_long_grade: str
    str_feedback: str


@dataclass
class GradeItem:
    """Item of Grades

    Args:
        activityid (str): The ID of the activity or "course" for the course grade item
        itemnumber (int): Will be 0 unless the module has multiple grades
        scaleid (int): The ID of the custom scale or 0
        name (str): The module name
        grademin (float): Minimum grade
        grademax (float): Maximum grade
        gradepass (float): The passing grade threshold
        locked (int): 0 means not locked, > 1 is a date to lock until
        hidden (int): 0 means not hidden, > 1 is a date to hide until
        grades (List[Grade]): list of Grade
    """
    activityid: str
    itemnumber: int
    scaleid: int
    name: str
    grademin: float
    grademax: float
    gradepass: float
    locked: int
    hidden: int
    grades: List[Grade] = field(factory=list)


@dataclass
class OutCome:
    """OutCome of Grades

    Args:
        activityid (str): The ID of the activity or "course" for the course grade item
        itemnumber (int): Will be 0 unless the module has multiple grades
        scaleid (int): The ID of the custom scale or 0
        name (str): The module name
        locked (int): 0 means not locked, > 1 is a date to lock until
        hidden (int): 0 means not hidden, > 1 is a date to hide until
        grades (List[Grade]): list of Grade
    """
    activityid: str
    itemnumber: int
    scaleid: int
    name: str
    locked: int
    hidden: int
    grades: List[Grade] = field(factory=list)


@dataclass
class Grades:
    """Grades

    Args:
        items (List[GradeItem]): An array of items associated with the grade items
        outcomes (List[OutCome]): An array of outcomes associated with the grade items
    """
    items: List[GradeItem] = field(factory=list)
    outcomes: List[OutCome] = field(factory=list)
