from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, fields


@dataclass
class InstanceInfo:
    """Instance Info

    Args:
        id (int): Id of course enrolment instance
        courseid (int): Id of course
        type (str): Type of enrolment plugin
        name (str): Name of enrolment plugin
        status (int): Is the enrolment enabled?
        passwordrequired (int): Is a password required?
    """
    id: int
    courseid: int
    type: str
    name: str
    status: int
    passwordrequired: int


@dataclass
class InstanceInfoResponse:
    """InstanceInfoResponse

    Args:
        instanceinfo (InstanceInfo): Course enrolment instance
        warnings (List[MoodleWarning]): list of warnings
    """
    instanceinfo: InstanceInfo
    warnings: List[MoodleWarning] = fields(MoodleWarning)
