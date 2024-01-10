from typing import List, Optional

from moodle.attr import dataclass, field
from . import DateView, Period, CourseEvent


@dataclass
class Day:
    """Day
    seconds (int): seconds
    minutes (int): minutes
    hours (int): hours
    mday (int): mday
    wday (int): wday
    year (int): year
    yday (int): yday
    istoday (int): istoday
    isweekend (int): isweekend
    timestamp (int): timestamp
    neweventtimestamp (int): neweventtimestamp
    viewdaylink (Optional[str]): viewdaylink
    viewdaylinktitle (Optional[str]): viewdaylinktitle
    events (List[CourseEvent]): events
    hasevents (int): hasevents
    calendareventtypes (List[str]): calendareventtypes
    previousperiod (int): previousperiod
    nextperiod (int): nextperiod
    navigation (str): navigation
    haslastdayofevent (int): haslastdayofevent
    popovertitle (str): popovertitle
    """

    seconds: int
    minutes: int
    hours: int
    mday: int
    wday: int
    year: int
    yday: int
    istoday: int
    isweekend: int
    timestamp: int
    neweventtimestamp: int
    hasevents: int
    previousperiod: int
    nextperiod: int
    navigation: str
    haslastdayofevent: int
    popovertitle: str
    viewdaylink: Optional[str] = None
    viewdaylinktitle: Optional[str] = None
    events: List[CourseEvent] = field(factory=list)
    calendareventtypes: List[str] = field(factory=list)


@dataclass
class Week:
    """Week
    prepadding (List[int]): prepadding
    postpadding (List[int]): postpadding
    days (List[Day]): days
    """

    prepadding: List[int] = field(factory=list)
    postpadding: List[int] = field(factory=list)
    days: List[Day] = field(factory=list)


@dataclass
class DayName:
    """Day Name
    dayno (int): dayno
    shortname (str): shortname
    fullname (str): fullnames
    """

    dayno: int
    shortname: str
    fullname: str


@dataclass
class MonthlyView:
    """Monthly View
    url (str): url
    courseid (int): courseid
    categoryid (Optional[int]): categoryid
    filter_selector (Optional[str]): filter_selector
    weeks (Week): weeks
    daynames (DayName): daynames
    date (DateView): date
    periodname (str): periodname
    includenavigation (int): includenavigation
    initialeventsloaded (int): initialeventsloaded
    previousperiod (Period): previousperiod
    previousperiodlink (str): previousperiodlink
    previousperiodname (str): previousperiodname
    nextperiod (Period): nextperiod
    nextperiodname (str): nextperiodname
    nextperiodlink (str): nextperiodlink
    larrow (str): larrow
    rarrow (str): rarrow
    defaulteventcontext (int): defaulteventcontext
    """

    url: str
    courseid: int
    weeks: Week
    daynames: DayName
    date: DateView
    periodname: str
    includenavigation: int
    initialeventsloaded: int
    previousperiod: Period
    previousperiodlink: str
    previousperiodname: str
    nextperiod: Period
    nextperiodname: str
    nextperiodlink: str
    larrow: str
    rarrow: str
    defaulteventcontext: int
    categoryid: Optional[int] = None
    filter_selector: Optional[str] = None
