from moodle.attr import dataclass


@dataclass
class InstanceInfo:
    """Instance Info

    Args:
        id (int): Id of course enrolment instance
        courseid (int): Id of course
        type (str): Type of enrolment plugin
        name (str): Name of enrolment plugin
        status (str): Status of enrolment plugin
        passwordrequired (str): Password required for enrolment
    """

    id: int
    courseid: int
    type: str
    name: str
    status: str
    passwordrequired: str
