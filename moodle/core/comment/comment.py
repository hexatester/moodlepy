from typing import Optional, List

from moodle import ResponsesFactory, MoodleWarning
from moodle.attr import dataclass, fields


@dataclass
class Comment:
    """Comment

    Args:
        id (int): Comment ID
        content (str): The content text formatted
        format (int): content format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        timecreated (int): Time created (timestamp)
        strftimeformat (str): Time format
        profileurl (str): URL profile
        fullname (str): fullname
        time (str): Time in human format
        avatar (str): HTML user picture
        userid (int): User ID
        delete (Optional[int]): Permission to delete=true/false
    """
    id: int
    content: str
    format: int
    timecreated: int
    strftimeformat: str
    profileurl: str
    fullname: str
    time: str
    avatar: str
    userid: int
    delete: Optional[int]


@dataclass
class Comments(ResponsesFactory[Comment]):
    """List of Comments

    Args:
        comments (List[Comment]): list of Comments
        count (Optional[int]): Total number of comments.
        perpage (Optional[int]): Number of comments per page.
        canpost (Optional[int]): Whether the user can post in this comment area.
        warnings (List[MoodleWarning]): list of MoodleWarnings
    """
    comments: List[Comment] = fields(Comment)
    count: Optional[int] = None
    perpage: Optional[int] = None
    canpost: Optional[int] = None
    warnings: List[MoodleWarning] = fields(MoodleWarning)

    @property
    def items(self) -> List[Comment]:
        return self.comments

    @dataclass
    class Create:
        """Adds a comment or comments.

        Args:
            contextlevel (str): contextlevel system, course, user...
            instanceid (int): the id of item associated with the contextlevel
            component (str): component
            content (str): component
            itemid (int): associated id
            area (str, optional): string comment area. Default to ""
        """
        contextlevel: str
        instanceid: int
        component: str
        content: str
        itemid: int
        area: str = ""
