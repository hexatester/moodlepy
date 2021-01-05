from datetime import datetime
from typing import List, Optional

from moodle import MoodleWarning
from moodle.attr import dataclass, fields


@dataclass
class Outcome:
    """Outcome information

    Args:
        id (str): Outcome id
        name (str): Outcome full name
        scale (str): Scale items
    """
    id: str
    name: str
    scale: str


@dataclass
class AdvancedGrading:
    """Advanced Grading

    Args:
        area (str):Gradable area name
        method (str):Grading method
    """
    area: str
    method: str


@dataclass
class Cm:
    """Course Module

    Args:
        id (int): The course module id
        course (int): The course id
        module (int): The module type id
        name (str): The activity name
        modname (str): The module component name (forum, assign, etc..)
        instance (int): The activity instance id
        section (int): The module section id
        sectionnum (int): The module section number
        groupmode (int): Group mode
        groupingid (int): Grouping id
        completion (int): If completion is enabled
        idnumber (Optional[str]): Module id number
        added (Optional[datetime]): Time added
        score (Optional[int]): Score
        indent (Optional[int]): Indentation
        visible (Optional[int]): If visible
        visibleoncoursepage (Optional[int]): If visible on course page
        visibleold (Optional[int]): Visible old
        completiongradeitemnumber (Optional[int]): Completion grade item
        completionview (Optional[int]): Completion view setting
        completionexpected (Optional[int]): Completion time expected
        showdescription (Optional[int]): If the description is showed
        availability (Optional[str]): Availability settings
        grade (Optional[float]): Grade (max value or scale id)
        scale (Optional[str]): Scale items (if used)
        gradepass (Optional[str]): Grade to pass (float)
        gradecat (Optional[int]): Grade category
        advancedgrading (List[AdvancedGrading]): Advanced grading settings
        outcomes (List[Outcome]): Outcomes information
    """
    id: int
    course: int
    module: int
    name: str
    modname: str
    instance: int
    section: int
    sectionnum: int
    groupmode: int
    groupingid: int
    completion: int
    idnumber: Optional[str]
    added: Optional[datetime]
    score: Optional[int]
    indent: Optional[int]
    visible: Optional[int]
    visibleoncoursepage: Optional[int]
    visibleold: Optional[int]
    completiongradeitemnumber: Optional[int]
    completionview: Optional[int]
    completionexpected: Optional[int]
    showdescription: Optional[int]
    availability: Optional[str]
    grade: Optional[float]
    scale: Optional[str]
    gradepass: Optional[str]
    gradecat: Optional[int]
    advancedgrading: List[AdvancedGrading] = fields(AdvancedGrading)
    outcomes: List[Outcome] = fields(Outcome)

    def __str__(self) -> str:
        return self.name


@dataclass
class CourseModule:
    cm: Cm
    warnings: List[MoodleWarning]
