from typing import List, Optional, Union

from moodle import MoodleWarning, ResponsesFactory
from moodle.attr import dataclass, field


@dataclass
class AuthorUrls:
    """Author's urls
    Args:
        profile (Optional[str]): The URL for the use profile page
        profileimage (Optional[str]): The URL for the use profile image
    """

    profile: Optional[str] = None
    profileimage: Optional[str] = None


@dataclass
class GroupUrls:
    """Group's urls
    Args:
        image (Optional[str]): image
    """

    image: Optional[str] = None


@dataclass
class Group:
    """Group
    Args:
        id (int): id
        name (str): name
        urls (GroupUrls): urls
    """

    id: int
    name: str
    urls: GroupUrls


@dataclass
class PlagiarismHtml:
    """The HTML source for the Plagiarism Response
    Args:
        plagiarism (Optional[str]): The HTML source for the Plagiarism Response
    """

    plagiarism: Optional[str] = None


@dataclass
class AttachmentUrls:
    """Attachment's urls
    Args:
        export (Optional[str]): The URL used to export the attachment
    """

    export: Optional[str] = None


@dataclass
class TagUrls:
    """Tag's urls
    Args:
        view (str): The URL to view the tag
    """

    view: str


@dataclass
class RatingScaleItem:
    """Rating's Scale item
    Args:
        value (int): Scale value/option id.
        name (str): Scale name.
    """

    value: int
    name: str


@dataclass
class Rating:
    """Rating
    Args:
        itemid (int): Item id.
        scaleid (Optional[int]): Scale id.
        userid (Optional[int]): User who rated id.
        aggregate (Optional[float]): Aggregated ratings grade.
        aggregatestr (Optional[str]): Aggregated ratings as string.
        aggregatelabel (Optional[str]): The aggregation label.
        count (Optional[int]): Ratings count (used when aggregating).
        rating (Optional[int]): The rating the user gave.
        canrate (Optional[int]): Whether the user can rate the item.
        canviewaggregate (Optional[int]): Whether the user can view the aggregated grade.
    """

    itemid: int
    scaleid: Optional[int] = None
    userid: Optional[int] = None
    aggregate: Optional[float] = None
    aggregatestr: Optional[str] = None
    aggregatelabel: Optional[str] = None
    count: Optional[int] = None
    rating: Optional[int] = None
    canrate: Optional[int] = None
    canviewaggregate: Optional[int] = None


@dataclass
class RatingScale:
    """Rating's Scale
    Args:
        id (int): Scale id.
        courseid (Optional[int]): Course id.
        name (Optional[str]): Scale name (when a real scale is used).
        max (int): Max value for the scale.
        isnumeric (int): Whether is a numeric scale.
        items (List[RatingScaleItem]): Scale items. Only returned for not numerical scales.
    """

    id: int
    max: int
    isnumeric: int
    courseid: Optional[int] = None
    name: Optional[str] = None
    items: List[RatingScaleItem] = field(factory=list)


@dataclass
class RatingInfo:
    """Rating Info of Post
    Args:
        contextid (int): Context id.
        component (str): Context name.
        ratingarea (str): Rating area name.
        canviewall (Optional[int]): Whether the user can view all the individual ratings.
        canviewany (Optional[int]): Whether the user can view aggregate of ratings of others.
        scales (List[RatingScale]): Different scales used information
        ratings (List[Rating]): The ratings
    """

    contextid: int
    component: str
    ratingarea: str
    canviewall: Optional[int] = None
    canviewany: Optional[int] = None
    scales: List[RatingScale] = field(factory=list)
    ratings: List[Rating] = field(factory=list)


@dataclass
class Html:
    """Html source for post
    Args:
        rating (Optional[str]): The HTML source to rate the post
        taglist (Optional[str]): The HTML source to view the list of tags
        authorsubheading (Optional[str]): The HTML source to view the author details
    """

    rating: Optional[str] = None
    taglist: Optional[str] = None
    authorsubheading: Optional[str] = None


@dataclass
class Tag:
    """Tag of Post
    Args:
        id (int): The ID of the Tag
        tagid (int): The tagid
        isstandard (int): Whether this is a standard tag
        displayname (str): The display name of the tag
        flag (int): Wehther this tag is flagged
        urls (TagUrls): The URL to view the tag
    """

    id: int
    tagid: int
    isstandard: int
    displayname: str
    flag: int
    urls: TagUrls


@dataclass
class Attachment:
    """Attachment of Post
    Args:
        contextid (int): contextid
        component (str): component
        filearea (str): filearea
        itemid (int): itemid
        filepath (str): filepath
        filename (str): filename
        isdir (int): isdir
        isimage (int): isimage
        timemodified (int): timemodified
        timecreated (int): timecreated
        filesize (int): filesize
        author (str): author
        license (str): license
        filenameshort (str): filenameshort
        filesizeformatted (str): filesizeformatted
        icon (str): icon
        timecreatedformatted (str): timecreatedformatted
        timemodifiedformatted (str): timemodifiedformatted
        url (str): url
        urls (AttachmentUrls): export url
        html (PlagiarismHtml): The HTML source for the Plagiarism Response
    """

    contextid: int
    component: str
    filearea: str
    itemid: int
    filepath: str
    filename: str
    isdir: int
    isimage: int
    timemodified: int
    timecreated: int
    filesize: int
    author: str
    license: str
    filenameshort: str
    filesizeformatted: str
    icon: str
    timecreatedformatted: str
    timemodifiedformatted: str
    url: str
    urls: AttachmentUrls
    html: PlagiarismHtml


@dataclass
class PostUrls:
    """Post's urls
    Args:
        view (Optional[str]): The URL used to view the post
        viewisolated (Optional[str]): The URL used to view the post in isolation
        viewparent (Optional[str]): The URL used to view the parent of the post
        edit (Optional[str]): The URL used to edit the post
        delete (Optional[str]): The URL used to delete the post
        split (Optional[str]): The URL used to split the discussion with the selected post being the first post in the new discussion
        reply (Optional[str]): The URL used to reply to the post
        export (Optional[str]): The URL used to export the post
        markasread (Optional[str]): The URL used to mark the post as read
        markasunread (Optional[str]): The URL used to mark the post as unread
        discuss (Optional[str]): discuss
    """

    view: Optional[str] = None
    viewisolated: Optional[str] = None
    viewparent: Optional[str] = None
    edit: Optional[str] = None
    delete: Optional[str] = None
    split: Optional[str] = None
    reply: Optional[str] = None
    export: Optional[str] = None
    markasread: Optional[str] = None
    markasunread: Optional[str] = None
    discuss: Optional[str] = None


@dataclass
class Capability:
    """Capability of Post
    Args:
        view (int): Whether the user can view the post
        edit (int): Whether the user can edit the post
        delete (int): Whether the user can delete the post
        split (int): Whether the user can split the post
        reply (int): Whether the user can reply to the post
        selfenrol (int): Whether the user can self enrol into the course
        export (int): Whether the user can export the post
        controlreadstatus (int): Whether the user can control the read status of the post
        canreplyprivately (int): Whether the user can post a private reply
    """

    view: int
    edit: int
    delete: int
    split: int
    reply: int
    selfenrol: int
    export: int
    controlreadstatus: int
    canreplyprivately: int


@dataclass
class Author:
    """Author of Post
    Args:
        id (Optional[int]): id
        fullname (Optional[str]): fullname
        groups (List[Group]): groups
        urls (AuthorUrls): images
    """

    urls: AuthorUrls
    id: Optional[int] = None
    fullname: Optional[str] = None
    groups: List[Group] = field(factory=list)


@dataclass
class Post:
    """Post
    Args:
        id (int): id
        subject (str): subject
        replysubject (str): replysubject
        message (str): message
        messageformat (int): message format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        author (Author): Author
        discussionid (int): discussionid
        hasparent (int): hasparent
        parentid (Optional[int]): parentid
        timecreated (int): timecreated
        unread (Optional[int]): unread
        isdeleted (int): isdeleted
        isprivatereply (int): isprivatereply
        haswordcount (int): haswordcount
        wordcount (Optional[int]): wordcount
        capabilities (Capability): Capability
        urls (PostUrls): PostUrls
        attachments (List[Attachment]): attachments
        tags (List[Tag]): tags
        html (Html): html source
        ratinginfo (Optional[RatingInfo]): Rating information
    """

    id: int
    subject: str
    replysubject: str
    message: str
    messageformat: int
    author: Author
    discussionid: int
    hasparent: int
    timecreated: int
    isdeleted: int
    isprivatereply: int
    haswordcount: int
    capabilities: Capability
    urls: PostUrls
    html: Html
    parentid: Optional[int] = None
    unread: Optional[int] = None
    wordcount: Optional[int] = None
    ratinginfo: Optional[RatingInfo] = None
    attachments: List[Attachment] = field(factory=list)
    tags: List[Tag] = field(factory=list)


@dataclass
class Message:
    """Warning Message
    Args:
        type (str): The classification to be used in the client side
        message (str): untranslated english message to explain the warning
    """

    type: str
    message: str


@dataclass
class NewPost:
    """Response
    Args:
        postid (int): new post id
        warnings (List[Warning]): list of warnings
        post (Post): post object
        messages (List[Message]): list of warning messages
    """

    postid: int
    post: Post
    warnings: List[MoodleWarning] = field(factory=list)
    messages: List[Message] = field(factory=list)


@dataclass
class Posts(ResponsesFactory[Post]):
    """List of Post
    Args:
        posts (List[Post]): list of Post
        warnings (List[Warning]): list of Warning
    """

    posts: List[Post] = field(factory=list)
    warnings: List[MoodleWarning] = field(factory=list)

    @property
    def items(self) -> List[Post]:
        return self.posts

    @dataclass
    class Option:
        """Option for add_discussion_post
        Args:
            name (str): The allowed keys (value format) are:
                            discussionsubscribe (bool); subscribe to the discussion?, default to true
                            private             (bool); make this reply private to the author of the parent post, default to false.
                            inlineattachmentsid (int); the draft file area id for inline attachments
                            attachmentsid       (int); the draft file area id for attachments
                            topreferredformat   (bool); convert the message & messageformat to FORMAT_HTML, defaults to false
            value (str): the value of the option, this param is validated in the external function.
        """

        name: str
        value: Union[bool, int]
