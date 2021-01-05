from attr import attrib
from typing import List, Optional

from moodle import MoodleWarning, ResponsesFactory
from moodle.attr import dataclass, fields


@dataclass
class BlogSummaryFiles:
    """Summary file
    Constructor arguments:
    param: filename (Optional[str]): File name.
    param: filepath (Optional[str]): File path.
    param: filesize (Optional[int]): File size.
    param: fileurl (Optional[str]): Downloadable file url.
    param: timemodified (Optional[int]): Time modified.
    param: mimetype (Optional[str]): File mime type.
    param: isexternalfile (Optional[int]): Whether is an external file.
    param: repositorytype (Optional[str]): The repository type for the external files.
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
class BlogAttachmentFile:
    """Attachment File
    Constructor arguments:
    param: filename: (Optional[str]): File name.
    param: filepath: (Optional[str]): File path.
    param: filesize: (Optional[int]): File size.
    param: fileurl: (Optional[str]): Downloadable file url.
    param: timemodified: (Optional[int]): Time modified.
    param: mimetype: (Optional[str]): File mime type.
    param: isexternalfile: (Optional[int]): Whether is an external file.
    param: repositorytype: (Optional[str]): The repository type for the external files.
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
class BlogTag:
    """Tag
    Constructor arguments:
    param: id: (int): Tag id.
    param: name: (str): Tag name.
    param: rawname: (str): The raw, unnormalised name for the tag as entered by users.
    param: isstandard: (int): Whether this tag is standard.
    param: tagcollid: (int): Tag collection id.
    param: taginstanceid: (int): Tag instance id.
    param: taginstancecontextid: (int): Context the tag instance belongs to.
    param: itemid: (int): Id of the record tagged.
    param: ordering: (int): Tag ordering.
    param: flag: (int): Whether the tag is flagged as inappropriate.
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
class BlogEntry:
    """Blog Entry
    Constructor arguments:
    params: id: (int): Post/entry id.
    params: module: (str): Where it was published the post (blog, blog_external...).
    params: userid: (int): Post author.
    params: courseid: (int): Course where the post was created.
    params: groupid: (int): Group post was created for.
    params: moduleid: (int): Module id where the post was created (not used anymore).
    params: coursemoduleid: (int): Course module id where the post was created.
    params: subject: (str): Post subject.
    params: summary: (str): Post summary.
    params: summaryformat: (int): Default for "1" # summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
    params: content: (str): Post content.
    params: uniquehash: (str): Post unique hash.
    params: rating: (int): Post rating.
    params: format: (int): Post content format.
    params: attachment: (str): Post atachment.
    params: publishstate: (str): Post publish state.
    params: lastmodified: (int): When it was last modified.
    params: created: (int): When it was created.
    params: usermodified: (int): User that updated the post.
    params: summaryfiles: (List[BlogSummaryFiles]): summaryfiles
    params: attachmentfiles: (List[BlogAttachmentFile]): attachmentfiles
    params: tags: (List[BlogTag]): Tags.
    """
    id: int
    module: str
    userid: int
    courseid: int
    groupid: int
    moduleid: int
    coursemoduleid: int
    subject: str
    summary: str
    summaryformat: int
    content: Optional[str]
    uniquehash: str
    rating: int
    format: int
    attachment: str
    publishstate: str
    lastmodified: int
    created: int
    usermodified: Optional[int]
    summaryfiles: List[BlogSummaryFiles] = fields(BlogSummaryFiles)
    attachmentfiles: List[BlogAttachmentFile] = fields(BlogAttachmentFile)
    tags: List[BlogTag] = fields(BlogTag)


@dataclass
class BlogEntries(ResponsesFactory[BlogEntry]):
    """Blog entries.
    Constructor arguments:
    params: entries: (List[BlogEntry]): list of BlogEntry.
    params: totalentries: (int): The total number of entries found.
    params: warnings: (List[Warning]): list of warnings.

    Returns:
        BlogEntries: Returns blog entries.
    """
    entries: List[BlogEntry] = fields(BlogEntry)
    totalentries: int = attrib(default=0)
    warnings: List[MoodleWarning] = fields(MoodleWarning)

    @property
    def items(self) -> List[BlogEntry]:
        return self.entries

    @dataclass
    class Filter:
        """Parameters to filter blog listings.
        Constructor arguments:
        params: name (str): The expected keys (value format) are:
                                tag      PARAM_NOTAGS blog tag
                                tagid    PARAM_INT    blog tag id
                                userid   PARAM_INT    blog author (userid)
                                cmid    PARAM_INT    course module id
                                entryid  PARAM_INT    entry id
                                groupid  PARAM_INT    group id
                                courseid PARAM_INT    course id
                                search   PARAM_RAW    search term
        params: value (str): The value of the filter.
        """
        name: str
        value: str
