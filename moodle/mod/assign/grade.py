from typing import List, Optional

from moodle import ResponsesFactory, MoodleWarning
from moodle.attr import dataclass, field
from . import AdvanceGradingData, PluginData


@dataclass
class Grade:
    """Grade
    Args:
        id (int): grade id
        assignment (Optional[int]): assignment id
        userid (int): student id
        attemptnumber (int): attempt number
        timecreated (int): grade creation time
        timemodified (int): grade last modified time
        grader (int): grader, -1 if grader is hidden
        grade (str): grade
        gradefordisplay (Optional[str]): grade rendered into a format suitable for display
    """

    id: int
    userid: int
    attemptnumber: int
    timecreated: int
    timemodified: int
    grader: int
    grade: str
    assignment: Optional[int] = None
    gradefordisplay: Optional[str] = None


@dataclass
class GradeAssignment(ResponsesFactory[Grade]):
    """GradeAssignment
    Args:
        assignmentid (int): assignment id
        grades (List[Grade]): grade information
    """

    assignmentid: int
    grades: List[Grade] = field(factory=list)

    @property
    def items(self) -> List[Grade]:
        return self.grades


@dataclass
class Grades(ResponsesFactory[GradeAssignment]):
    """Grades
    Args:
        assignments (List[GradeAssignment]): list of assignment grade information
        warnings (List[Warning]): list of warnings
    """

    assignments: List[GradeAssignment] = field(factory=list)
    warnings: List[MoodleWarning] = field(factory=list)

    @property
    def items(self) -> List[GradeAssignment]:
        return self.assignments

    @dataclass
    class Create:
        """Grades for create grades
        Args:
            userid (int): The student id to operate on
            grade (float): The new grade for this user. Ignored if advanced grading used
            attemptnumber (int): The attempt number (-1 means latest attempt)
            addattempt (int): Allow another attempt if manual attempt reopen method
            workflowstate (str): The next marking workflow state
            plugindata (Optional[PluginData]): default {}
            advancedgradingdata (Optional[AdvanceGradingData]): default {}
        """

        userid: int
        grade: float
        attemptnumber: int
        addattempt: int
        workflowstate: str
        plugindata: Optional[PluginData] = None
        advancedgradingdata: Optional[AdvanceGradingData] = None
