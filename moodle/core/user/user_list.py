from moodle.attr import dataclass


@dataclass
class UserList:
    """User List

    Args:
        userid (int): userid
        courseid (int): courseid
    """

    userid: int
    courseid: int
