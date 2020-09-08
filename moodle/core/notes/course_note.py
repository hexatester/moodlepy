from dataclasses import dataclass
from datetime import datetime


@dataclass
class CourseNote:
    """Course Note
    Constructor arguments:
    params: id (int): id of this note
    params: courseid (int): id of the course
    params: userid (int): user id
    params: content (str): the content text formated
    params: format (int): content format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
    params: created (int): time created (timestamp)
    params: lastmodified (int): time of last modification (timestamp)
    params: usermodified (int): user id of the creator of this note
    params: publishstate (str): state of the note (i.e. draft, public, site)
    """
    id: int
    courseid: int
    userid: int
    content: str
    format: int
    created: int
    lastmodified: datetime
    usermodified: int
    publishstate: str
