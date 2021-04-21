from datetime import datetime
from typing import List, Optional

from moodle.attr import dataclass, field


@dataclass
class ContentInfo:
    """Content Info
    Args:
        filescount (int): Total number of files.
        filessize (int): Total files size.
        lastmodified (datetime): Last time files were modified.
        mimetypes (List[str]): Files mime types.
        repositorytype (Optional[str]): The repository type for the main file.
    """

    filescount: int
    filessize: int
    lastmodified: datetime
    mimetypes: List[str] = field(factory=list)
    repositorytype: Optional[str] = None


@dataclass
class Tag:
    """Tag
    Args
        id (int): Tag id.
        name (str): Tag name.
        rawname (str): The raw, unnormalised name for the tag as entered by users.
        isstandard (int): Whether this tag is standard.
        tagcollid (int): Tag collection id.
        taginstanceid (int): Tag instance id.
        taginstancecontextid (int): Context the tag instance belongs to.
        itemid (int): Id of the record tagged.
        ordering (int): Tag ordering.
        flag (int): Whether the tag is flagged as inappropriate.
    """

    id: int
    name: str
    rawname: str
    isstandard: int
    tagcollid: int
    taginstanceid: int
    taginstancecontextid: int
    itemid: int
    ordering: int
    flag: int


@dataclass
class Content:
    """Content
    Args:
        type (str): a file or a folder or external link
        filename (str): filename
        filepath (Optional[str]): filepath
        filesize (int): filesize
        fileurl (Optional[str]): downloadable file url
        content (Optional[str]): Raw content, will be used when type is content
        timecreated (Optional[datetime]): Time created
        timemodified (Optional[datetime]): Time modified
        sortorder (Optional[int]): Content sort order
        mimetype (Optional[str]): File mime type.
        isexternalfile (Optional[int]): Whether is an external file.
        repositorytype (Optional[str]): The repository type for external files.
        userid (Optional[int]): User who added this content to moodle
        author (Optional[str]): Content owner
        license (Optional[str]): Content license
        tags (List[Tag]): Tags
    """

    type: str
    filename: str
    filepath: Optional[str]
    filesize: int
    fileurl: Optional[str]
    timecreated: Optional[datetime]
    timemodified: Optional[datetime]
    sortorder: Optional[int]
    userid: Optional[int]
    author: Optional[str]
    license: Optional[str]
    mimetype: Optional[str] = None
    isexternalfile: Optional[int] = None
    content: Optional[str] = None
    repositorytype: Optional[str] = None
    tags: List[Tag] = field(factory=list)


@dataclass
class Completion:
    """Completion
    Args:
        state (int): Completion state value: 0 means incomplete, 1 complete, 2 complete pass, 3 complete fail
        timecompleted (datetime): Timestamp for completion status.
        overrideby (int): The user id who has overriden the status.
        valueused (Optional[bool]): Whether the completion status affects the availability of another activity.
    """

    state: int
    timecompleted: datetime
    overrideby: Optional[int]
    valueused: Optional[bool]


@dataclass
class Module:
    """Module
    Args:
        id (int): activity id
        url (Optional[str]): activity url
        name (str): activity module name
        instance (Optional[int]): instance id
        description (Optional[str]): activity description
        visible (Optional[int]): is the module visible
        uservisible (Optional[int]): Is the module visible for the user?
        availabilityinfo (Optional[str]): Availability information.
        visibleoncoursepage (Optional[int]): is the module visible on course page
        modicon (str): activity icon url
        modname (str): activity module type
        modplural (str): activity module plural name
        availability (Optional[str]): module availability settings
        indent (int): number of identation in the site
        onclick (Optional[str]): Onclick action.
        afterlink (Optional[str]): After link info to be displayed.
        customdata (Optional[str]): Custom data (JSON encoded).
        completion (Optional[int]): Type of completion tracking: 0 means none, 1 manual, 2 automatic.
        completiondata (Optional[Completion]): Module completion data.
        contents (List[Content]): list of Content
        contentsinfo (Optional[ContentInfo]): Contents summary information.
    """

    id: int
    name: str
    instance: Optional[int]
    visible: Optional[int]
    uservisible: Optional[int]
    visibleoncoursepage: Optional[int]
    modicon: str
    modname: str
    modplural: str
    indent: int
    onclick: Optional[str]
    afterlink: Optional[str]
    customdata: Optional[str]
    completion: Optional[int]
    url: Optional[str] = None
    description: Optional[str] = None
    availability: Optional[str] = None
    completiondata: Optional[Completion] = None
    availabilityinfo: Optional[str] = None
    contents: List[Content] = field(factory=list)
    contentsinfo: Optional[ContentInfo] = None


@dataclass
class Section:
    """Section
    Args:
        id: (int): Section ID
        name: (str): Section name
        visible: (Optional[int]): is the section visible
        summary: (str): Section description
        summaryformat: (int): summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        section: (Optional[int]): Section number inside the course
        hiddenbynumsections: (Optional[int]): Whether is a section hidden in the course format
        uservisible: (Optional[int]): Is the section visible for the user?
        availabilityinfo: (Optional[str]): Availability information.
        modules: (List[Module]): list of module
    """

    id: int
    name: str
    visible: Optional[int]
    summary: str
    summaryformat: int
    section: Optional[int]
    hiddenbynumsections: Optional[int]
    uservisible: Optional[int]
    availabilityinfo: Optional[str] = None
    modules: List[Module] = field(factory=list)
