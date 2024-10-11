from typing import Optional, List

from moodle import ResponsesFactory
from moodle.attr import dataclass, field


@dataclass
class CourseEventIcon:
    """Icon
    Constructor arguments:
    params: key (str): key
    params: component (str): component
    params: alttext (str): alttext
    """

    key: str
    component: str
    alttext: str


@dataclass
class CourseEventCategory:
    """Category
    Constructor arguments:
    params: id (int): id
    params: name (str): name
    params: idnumber (str): idnumber
    params: description (Optional[str]): description
    params: parent (int): parent
    params: coursecount (int): coursecount
    params: visible (int): visible
    params: timemodified (int): timemodified
    params: depth (int): depth
    params: nestedname (str): nestedname
    params: url (str): url
    """

    id: int
    name: str
    idnumber: str
    parent: int
    coursecount: int
    visible: int
    timemodified: int
    depth: int
    nestedname: str
    url: str
    description: Optional[str] = None

    def __str__(self) -> str:
        return self.name


@dataclass
class CourseEventCourse:
    """Course
    Constructor arguments:
    params: id (int): id
    params: fullname (str): fullname
    params: shortname (str): shortname
    params: idnumber (str): idnumber
    params: summary (str): summary
    params: summaryformat (int): summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
    params: startdate (int): startdate
    params: enddate (int): enddate
    params: visible (int): visible
    params: fullnamedisplay (str): fullnamedisplay
    params: viewurl (str): viewurl
    params: courseimage (str): courseimage
    params: progress (Optional[int]): progress
    params: hasprogress (int): hasprogress
    params: isfavourite (int): isfavourite
    params: hidden (int): hidden
    params: timeaccess (Optional[int]): timeaccess
    params: showshortname (int): showshortname
    params: coursecategory (str): coursecategory
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
    hasprogress: int
    isfavourite: int
    hidden: int
    showshortname: int
    coursecategory: str
    progress: Optional[int] = None
    timeaccess: Optional[int] = None

    def __str__(self) -> str:
        return self.fullname


@dataclass
class CourseEventSubscription:
    """Subscription
    Constructor arguments:
    params: displayeventsource (int): displayeventsource
    params: subscriptionname (Optional[str]): subscriptionname
    params: subscriptionurl (Optional[str]): subscriptionurl
    """

    displayeventsource: int
    subscriptionname: Optional[str] = None
    subscriptionurl: Optional[str] = None

    def __str__(self) -> str:
        return self.subscriptionname or repr(self)


@dataclass
class CourseEventAction:
    """Action
    Constructor arguments:
    params: name (str): name
    params: url (str): url
    params: itemcount (int): itemcount
    params: actionable (int): actionable
    params: showitemcount (int): showitemcount
    """

    name: str
    url: str
    itemcount: int
    actionable: int
    showitemcount: int

    def __str__(self) -> str:
        return self.name


@dataclass
class CourseEvent:
    """Course Event
    Constructor arguments:
    params: id (int): id
    params: name (str): name
    params: description (Optional[str]): description
    params: descriptionformat (int): Default untuk "1" description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
    params: location (Optional[str]): location
    params: categoryid (Optional[int]): categoryid
    params: groupid (Optional[int]): groupid
    params: userid (Optional[int]): userid
    params: repeatid (Optional[int]): repeatid
    params: eventcount (Optional[int]): eventcount
    params: modulename (Optional[str]): modulename
    params: instance (Optional[int]): instance
    params: eventtype (str): eventtype
    params: timestart (int): timestart
    params: timeduration (int): timeduration
    params: timesort (int): timesort
    params: visible (int): visible
    params: timemodified (int): timemodified
    params: icon (CourseEventIcon)
    params: category (CourseEventCategory)
    params: course (CourseEventCourse)
    params: subscription (CourseEventSubscription)
    params: canedit (int): canedit
    params: candelete (int): candelete
    params: deleteurl (str): deleteurl
    params: editurl (str): editurl
    params: viewurl (str): viewurl
    params: formattedtime (str): formattedtime
    params: isactionevent (int): isactionevent
    params: iscourseevent (int): iscourseevent
    params: iscategoryevent (int): iscategoryevent
    params: groupname (Optional[str]): groupname
    params: normalisedeventtype (str): normalisedeventtype
    params: normalisedeventtypetext (str): normalisedeventtypetext
    params: url (str): url
    params: action (Optional[CourseEventAction])
    params: islastday (int): islastday
    params: popupname (str): popupname
    params: mindaytimestamp (Optional[int]): mindaytimestamp
    params: mindayerror (Optional[str]): mindayerror
    params: maxdaytimestamp (Optional[int]): maxdaytimestamp
    params: maxdayerror (Optional[str]): maxdayerror
    params: draggable (int): draggable
    """

    id: int
    name: str
    descriptionformat: int
    eventtype: str
    timestart: int
    timeduration: int
    timesort: int
    visible: int
    timemodified: int
    icon: CourseEventIcon
    category: CourseEventCategory
    course: CourseEventCourse
    subscription: CourseEventSubscription
    canedit: int
    candelete: int
    deleteurl: str
    editurl: str
    viewurl: str
    formattedtime: str
    isactionevent: int
    iscourseevent: int
    iscategoryevent: int
    normalisedeventtype: str
    normalisedeventtypetext: str
    url: str
    islastday: int
    popupname: str
    draggable: int
    description: Optional[str] = None
    location: Optional[str] = None
    categoryid: Optional[int] = None
    groupid: Optional[int] = None
    userid: Optional[int] = None
    repeatid: Optional[int] = None
    eventcount: Optional[int] = None
    modulename: Optional[str] = None
    instance: Optional[int] = None
    groupname: Optional[str] = None
    action: Optional[CourseEventAction] = None
    mindaytimestamp: Optional[int] = None
    mindayerror: Optional[str] = None
    maxdaytimestamp: Optional[int] = None
    maxdayerror: Optional[str] = None

    def __str__(self) -> str:
        return self.name


@dataclass
class CourseEvents(ResponsesFactory[CourseEvent]):
    """List of [CourseEvent]"""

    firstid: int
    lastid: int
    events: List[CourseEvent] = field(factory=list)

    @property
    def items(self) -> List[CourseEvent]:
        return self.events

    @dataclass
    class EventForm:
        """Result submit form data for event form
        parms: event (CourseEvent): Resulted event
        parms: validationerror (Optional[int]): Default untuk "" Invalid form data
        """

        event: CourseEvent
        validationerror: Optional[int] = None


@dataclass
class ActionEventCourses(ResponsesFactory[CourseEvents]):
    """Calendar action events by courses

    Constructor arguments:
    params: groupedbycourse (List[CourseEvents]): Collection of course events

    Returns:
        ActionEventCourses: ActionEventCourses
    """

    groupedbycourse: List[CourseEvents] = field(factory=list)

    @property
    def items(self) -> List[CourseEvents]:
        return self.groupedbycourse
