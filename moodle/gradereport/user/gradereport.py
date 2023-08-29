from moodle.attr import dataclass, field
from typing import List, Optional


@dataclass
class GradeItem:
    """Grade Item

    Args:
        id (int): Grade item id
        itemname (string): Grade item name
        itemtype (string): Grade item type
        itemmodule (string): Grade item module
        iteminstance (int): Grade item instance
        itemnumber (int): Grade item item number
        idnumber (string): Grade item idnumber
        categoryid (int): Grade item category id
        outcomeid (int): Outcome id
        scaleid (int): Scale id
        locked (Optional[int]): Grade item for user locked?
        cmid (Optional[int]): Course module id (if type mod)
        weightraw (Optional[int]): Weight raw
        weightformatted (Optional[string]): Weight
        status (Optional[string]): Status
        graderaw (Optional[int]): Grade raw
        gradedatesubmitted (Optional[int]): Grade submit date
        gradedategraded (Optional[int]): Grade graded date
        gradehiddenbydate (Optional[int]): Grade hidden by date?
        gradeneedsupdate (Optional[int]): Grade needs update?
        gradeishidden (Optional[int]): Grade is hidden?
        gradeislocked (Optional[int]): Grade is locked?
        gradeisoverridden (Optional[int]): Grade overridden?
        gradeformatted (Optional[string]): The grade formatted
        grademin (Optional[int]): Grade min
        grademax (Optional[int]): Grade max
        rangeformatted (Optional[string]): Range formatted
        percentageformatted (Optional[string]): Percentage
        lettergradeformatted (Optional[string]): Letter grade
        rank (Optional[int]): Rank in the course
        numusers (Optional[int]): Num users in course
        averageformatted (Optional[string]): Grade average
        feedback (Optional[string]): Grade feedback
        feedbackformat (Optional[int]): feedback format
         (1 = HTML, 0 = MOODLE, 2 = PLAIN, or 4 = MARKDOWN

    """

    feedback: str
    feedbackformat: int
    gradeformatted: str
    gradehiddenbydate: bool
    gradeishidden: bool
    gradeislocked: bool
    gradeisoverridden: bool
    grademax: int
    grademin: int
    gradeneedsupdate: bool
    id: int
    idnumber: str
    iteminstance: int
    itemmodule: str
    itemname: str
    itemtype: str
    locked: bool
    percentageformatted: str
    rangeformatted: str
    categoryid: Optional[int] = None
    cmid: Optional[int] = None
    gradedategraded: Optional[int] = None
    gradedatesubmitted: Optional[int] = None
    graderaw: Optional[int] = None
    itemnumber: Optional[int] = None
    outcomeid: Optional[int] = None
    scaleid: Optional[int] = None
    weightformatted: Optional[str] = None
    weightraw: Optional[int] = None


@dataclass
class UserGrade:
    """User Grade

    Args:
        courseid (int): course id
        courseidnumber (string): course idnumber
        gradeitems (List[GradeItem]): Grade items
        maxdepth (int): table max depth (needed for printing it)
        userfullname (string): user fullname
        userid (int): user id
        useridnumber (string): user idnumber
    """

    courseid: int
    courseidnumber: str
    gradeitems: List[GradeItem]
    maxdepth: int
    userfullname: str
    userid: int
    useridnumber: str


@dataclass
class GradeReport:
    """Grade Report

    Args:
        usergrades (List[UserGrade]): List of user grades
        warnings (List[Warning]): List of warnings
    """

    usergrades: List[UserGrade] = field(factory=list)
    warnings: List[Warning] = field(factory=list)
