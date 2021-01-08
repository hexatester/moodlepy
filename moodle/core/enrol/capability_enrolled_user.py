from typing import List

from moodle.attr import dataclass, fields
from . import EnrolledUser


@dataclass
class CapabilityEnrolledUser:
    """Capability with Enrolled Users

    Args:
        courseid (int): Course ID number in the Moodle course table
        capability (str): Capability name
        users (List[EnrolledUser]): List of users that are enrolled in the course and have the specified capability
    """
    courseid: int
    capability: str
    users: List[EnrolledUser] = fields(EnrolledUser)
