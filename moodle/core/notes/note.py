from dataclasses import dataclass
from typing import Optional


@dataclass
class Note:
    """Note to create
    Constructor arguments:
    params: userid (int): id of the user the note is about
    params: publishstate (str): 'personal', 'course' or 'site'
    params: courseid (int): course id of the note (in Moodle a note can only be created into a course, even for site and personal notes)
    params: text (str): the text of the message - text or HTML
    params: format (int): Default untuk "1" text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
    params: clientnoteid (Optional[str]): your own client id for the note. If this id is provided, the fail message id will be returned to you
    """
    userid: int
    publishstate: str
    courseid: int
    text: str
    format: int = 1
    clientnoteid: Optional[str] = None

    @dataclass
    class Result:
        """Result when creating notes
        Constructor arguments:
        params: clientnoteid (Optional[str]): your own id for the note
        params: noteid (int): ID of the created note when successful, -1 when failed
        params: errormessage (Optional[str]): error message - if failed
        """
        clientnoteid: Optional[str]
        noteid: int
        errormessage: Optional[str]
