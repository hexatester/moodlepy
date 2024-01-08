from datetime import datetime
from typing import List, Optional

from moodle import MoodleWarning
from moodle.attr import dataclass, field


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
    advancedgrading: List[AdvancedGrading] = field(factory=list)
    outcomes: List[Outcome] = field(factory=list)
    idnumber: Optional[str] = None
    added: Optional[datetime] = None
    score: Optional[int] = None
    indent: Optional[int] = None
    visible: Optional[int] = None
    visibleoncoursepage: Optional[int] = None
    visibleold: Optional[int] = None
    completiongradeitemnumber: Optional[int] = None
    completionview: Optional[int] = None
    completionexpected: Optional[int] = None
    showdescription: Optional[int] = None
    availability: Optional[str] = None
    grade: Optional[float] = None
    scale: Optional[str] = None
    gradepass: Optional[str] = None
    gradecat: Optional[int] = None

    def __str__(self) -> str:
        return self.name


@dataclass
class CourseModule:
    cm: Cm
    warnings: List[MoodleWarning] = field(factory=list)
