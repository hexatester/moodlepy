from moodle.attr import dataclass


@dataclass
class RecentlyAccessedItem:
    """Recently Accessed Item

    Args:
        id (int): id
        courseid (int): courseid
        cmid (int): cmid
        userid (int): userid
        modname (str): modname
        name (str): name
        coursename (str): coursename
        timeaccess (int): timeaccess
        viewurl (str): viewurl
        courseviewurl (str): courseviewurl
        icon (str): icon
    """
    id: int
    courseid: int
    cmid: int
    userid: int
    modname: str
    name: str
    coursename: str
    timeaccess: int
    viewurl: str
    courseviewurl: str
    icon: str
