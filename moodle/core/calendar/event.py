from dataclasses import dataclass
from typing import Optional, List
from moodle import Warning, ResponsesFactory


@dataclass
class Event:
    """Event
    Constructor arguments:
    params: id (int): event id
    params: name (str): event name
    params: description (Optional[str]): Description
    params: format (int): description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
    params: courseid (int): course id
    params: categoryid (Optional[int]): Category id (only for category events).
    params: groupid (int): group id
    params: userid (int): user id
    params: repeatid (int): repeat id
    params: modulename (Optional[str]): module name
    params: instance (int): instance id
    params: eventtype (str): Event type
    params: timestart (int): timestart
    params: timeduration (int): time duration
    params: visible (int): visible
    params: uuid (Optional[str]): unique id of ical events
    params: sequence (int): sequence
    params: timemodified (int): time modified
    params: subscriptionid (Optional[int]): Subscription id
    """
    id: int
    name: str
    description: Optional[str]
    format: int
    courseid: int
    categoryid: Optional[int]
    groupid: Optional[int]
    userid: int
    repeatid: Optional[int]
    modulename: Optional[str]
    instance: Optional[int]
    eventtype: str
    timestart: int
    timeduration: int
    visible: int
    uuid: Optional[str]
    sequence: int
    timemodified: int
    subscriptionid: Optional[int]

    def __str__(self) -> str:
        return self.name


@dataclass
class Events(ResponsesFactory[Event]):
    events: List[Event]
    warnings: List[Warning]

    @property
    def items(self) -> List[Event]:
        return self.events

    @dataclass
    class Create:
        """Event to create
        Constructor arguments:
        params: name (str): event name
        params: description (Optional[str]): Default for "null" Description
        params: format (Optional[int]): Default for "1" description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        params: courseid (Optional[int]): Default for "0" course id
        params: groupid (Optional[int]): Default for "0" group id
        params: repeats (Optional[int]): Default for "0" number of repeats
        params: eventtype (Optional[str]): Default for "user" Event type
        params: timestart (Optional[int]): Default for "1599354090" timestart
        params: timeduration (Optional[int]): Default for "0" time duration
        params: visible (Optional[int]): Default for "1" visible
        params: sequence (Optional[int]): Default for "1" sequence
        """
        name: str
        description: Optional[str] = None
        format: Optional[int] = 1
        courseid: Optional[int] = 0
        groupid: Optional[int] = 0
        repeats: Optional[int] = 0
        eventtype: Optional[str] = 'user'
        timestart: Optional[int] = None
        timeduration: Optional[int] = 0
        visible: Optional[int] = 1
        sequence: Optional[int] = 1

    @dataclass
    class Delete:
        """Arg for Delete calendar events
        Constructor arguments:
        params: eventid (int): Event ID
        params: repeat (int): Delete comeplete series if repeated event
        """
        eventid: int
        repeat: int

    @dataclass
    class Details:
        """Event details
        Constructor arguments:
        params: eventids (List[int]): List of event ids
        params: courseids (List[int]): List of course ids for which events will be returned
        params: groupids (List[int]): List of group ids for which events should be returned
        params: categoryids (List[int]): List of category ids for which events will be returned
        """
        eventids: List[int]
        courseids: List[int]
        groupids: List[int]
        categoryids: List[int]

    @dataclass
    class Options:
        """Options
        params: userevents (int): Set to true to return current user's user events, Default for "1"
        params: siteevents (int): Set to true to return global events, Default for "1"
        params: timestart (int): Time from which events should be returned, Default for "0"
        params: timeend (int): Time to which the events should be returned. We treat 0 and null as no end, Default for "0"
        params: ignorehidden (int): Ignore hidden events or not, Default for "1"
        """
        userevents: Optional[int] = 1
        siteevents: Optional[int] = 1
        timestart: Optional[int] = 0
        timeend: Optional[int] = 0
        ignorehidden: Optional[int] = 1
