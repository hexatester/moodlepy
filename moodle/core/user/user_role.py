from moodle.attr import dataclass


@dataclass
class UserRole:
    """
    Args:
        roleid (int): role id
        name (str): role name
        shortname (str): role shortname
        sortorder (int): role sortorder
    """
    roleid: int
    name: str
    shortname: str
    sortorder: int
