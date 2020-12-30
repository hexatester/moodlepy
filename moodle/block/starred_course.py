from dataclasses import dataclass
from typing import Optional


@dataclass
class StarredCourse:
    """
    Args:
        id (int): id
        fullname (str): fullname
        shortname (str): shortname
        idnumber (str): idnumber
        summary (str): summary
        summaryformat (int): summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        startdate (int): startdate
        enddate (int): enddate
        visible (int): visible
        fullnamedisplay (str): fullnamedisplay
        viewurl (str): viewurl
        courseimage (str): courseimage
        progress (Optional[int]): progress
        hasprogress (int): hasprogress
        isfavourite (int): isfavourite
        hidden (int): hidden
        timeaccess (Optional[int]): timeaccess
        showshortname (int): showshortname
        coursecategory (str): coursecategory
    """
    id: int
    fullname: str
    shortname: str
    idnumber: str
    summary: str
    summaryformat: int
    startdate: int
    enddate: int
    visible: int
    fullnamedisplay: str
    viewurl: str
    courseimage: str
    progress: Optional[int]
    hasprogress: int
    isfavourite: int
    hidden: int
    timeaccess: Optional[int]
    showshortname: int
    coursecategory: str
