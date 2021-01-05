from moodle.attr import dataclass
from datetime import datetime
from typing import Optional, Union


@dataclass
class Enrolment:
    """Enrolment

    Args:
        roleid (int): Role to assign to the user
        userid (int): The user that is going to be enrolled
        courseid (int): The course to enrol the user role in
        timestart (Optional[Union[datetime, int]]): Timestamp when the enrolment start
        timeend (Optional[Union[datetime, int]]): Timestamp when the enrolment end
        suspend (Optional[int]): set to 1 to suspend the enrolment
    """
    roleid: int
    userid: int
    courseid: int
    timestart: Optional[Union[datetime, int]]
    timeend: Optional[Union[datetime, int]]
    suspend: Optional[int]
