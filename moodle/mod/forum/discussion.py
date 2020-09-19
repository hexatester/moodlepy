from dataclasses import dataclass
from typing import List, Optional, Union
from moodle import MoodleObject, ResponsesFactory, Warning


@dataclass
class File:
    """File
    Args:
        filename (Optional[str]): File name.
        filepath (Optional[str]): File path.
        filesize (Optional[int]): File size.
        fileurl (Optional[str]): Downloadable file url.
        timemodified (Optional[int]): Time modified.
        mimetype (Optional[str]): File mime type.
        isexternalfile (Optional[int]): Whether is an external file.
        repositorytype (Optional[str]): The repository type for external files.
    """
    filename: Optional[str]
    filepath: Optional[str]
    filesize: Optional[int]
    fileurl: Optional[str]
    timemodified: Optional[int]
    mimetype: Optional[str]
    isexternalfile: Optional[int]
    repositorytype: Optional[str]


@dataclass
class Discussion(MoodleObject):
    """Discussion
    Args:
        id (int): Post id
        name (str): Discussion name
        groupid (int): Group id
        timemodified (int): Time modified
        usermodified (int): The id of the user who last modified
        timestart (int): Time discussion can start
        timeend (int): Time discussion ends
        discussion (int): Discussion id
        parent (int): Parent id
        userid (int): User who started the discussion id
        created (int): Creation time
        modified (int): Time modified
        mailed (int): Mailed?
        subject (str): The post subject
        message (str): The post message
        messageformat (int): message format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        messagetrust (int): Can we trust?
        messageinlinefiles (List[File]): post message inline files
        attachment (str): Has attachments?
        attachments (List[File]): attachments
        totalscore (int): The post message total score
        mailnow (int): Mail now?
        userfullname (str): Post author full name
        usermodifiedfullname (str): Post modifier full name
        userpictureurl (str): Post author picture.
        usermodifiedpictureurl (str): Post modifier picture.
        numreplies (int): The number of replies in the discussion
        numunread (int): The number of unread discussions.
        pinned (int): Is the discussion pinned
        locked (int): Is the discussion locked
        starred (int): Is the discussion starred
        canreply (int): Can the user reply to the discussion
        canlock (int): Can the user lock the discussion
        canfavourite (int): Can the user star the discussion
    """
    id: int
    name: str
    groupid: int
    timemodified: int
    usermodified: int
    timestart: int
    timeend: int
    discussion: int
    parent: int
    userid: int
    created: int
    modified: int
    mailed: int
    subject: str
    message: str
    messageformat: int
    messagetrust: int
    messageinlinefiles: List[File]
    attachment: str
    attachments: List[File]
    totalscore: int
    mailnow: int
    userfullname: str
    usermodifiedfullname: str
    userpictureurl: str
    usermodifiedpictureurl: str
    numreplies: int
    numunread: int
    pinned: int
    locked: int
    starred: int
    canreply: int
    canlock: int
    canfavourite: int


@dataclass
class Discussions(ResponsesFactory[Discussion]):
    """Discussions
    Args:
        discussions (List[Discussion]): list of Discussion
        warnings (List[Warning]): list of Warning

    Returns:
        Discussions: List of Discussion
    """
    discussions: List[Discussion]
    warnings: List[Warning]

    @property
    def items(self) -> List[Discussion]:
        return self.discussions

    @dataclass
    class Option:
        """Discussion Option
        Args:
            name (str): The allowed keys (value format) are:
                            discussionsubscribe (bool); subscribe to the discussion?, default to true
                            discussionpinned    (bool); is the discussion pinned, default to false
                            inlineattachmentsid (int); the draft file area id for inline attachments
                            attachmentsid       (int); the draft file area id for attachments
            value (str): The value of the option, This param is validated in the external function.
        """
        name: str
        value: Union[bool, int]

    @dataclass
    class New:
        """Response of add_discussion
        Args:
            discussionid (int): New Discussion ID
            warnings (List[Warning]): list of warnings
        """
        discussionid: int
        warnings: List[Warning]

    @dataclass
    class CanAdd:
        """Response of can_add_discussion
        Args:
            status (int): True if the user can add discussions, false otherwise.
            canpindiscussions (Optional[int]): True if the user can pin discussions, false otherwise.
            cancreateattachment (Optional[int]): True if the user can add attachments, false otherwise.
            warnings (List[Warning]): list of warnings
        """
        status: int
        canpindiscussions: Optional[int]
        cancreateattachment: Optional[int]
        warnings: List[Warning]
