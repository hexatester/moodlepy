from moodle.attr import dataclass
from typing import List, Optional
from . import CourseEvent, DateView, Period


@dataclass
class DayView:
    """Day View
    Constructor arguments:
    params: events (List[CourseEvent]): events
    params: defaulteventcontext (int): defaulteventcontext
    params: filter_selector (str): filter_selector
    params: courseid (int): courseid
    params: categoryid (Optional[int]): categoryid
    params: neweventtimestamp (int): neweventtimestamp
    params: date (DateView): DateView
    params: periodname (str): periodname
    params: previousperiod (Period): Period
    params: nextperiodname (str): nextperiodname
    params: nextperiodlink (str): nextperiodlink
    params: nextperiod (Period): Period
    params: larrow (str): larrow
    params: rarrow (str): rarrow
    """
    events: List[CourseEvent]  # events
    defaulteventcontext: int  # defaulteventcontext
    filter_selector: str  # filter_selector
    courseid: int  # courseid
    categoryid: Optional[int]  # categoryid
    neweventtimestamp: int  # neweventtimestamp
    date: DateView
    periodname: str  # periodname
    previousperiod: Period
    nextperiodname: str  # nextperiodname
    nextperiodlink: str  # nextperiodlink
    nextperiod: Period
    larrow: str  # larrow
    rarrow: str  # rarrow
