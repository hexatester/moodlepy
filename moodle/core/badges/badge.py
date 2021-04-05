from typing import Optional, List

from moodle.attr import dataclass, field
from moodle import MoodleWarning, ResponsesFactory


@dataclass
class BagdeEndorsement:
    """Bagde Endorsement
    Constructor arguments:
        id (int): Endorsement id
        badgeid (int): Badge id
        issuername (str): Endorsement issuer name
        issuerurl (str): Endorsement issuer URL
        issueremail (str): Endorsement issuer email
        claimid (str): Claim URL
        claimcomment (str): Claim comment
        dateissued (int): Date issued
    """
    id: int
    badgeid: int
    issuername: str
    issuerurl: str
    issueremail: str
    claimid: str
    claimcomment: str
    dateissued: int


@dataclass
class BagdeAlignment:
    """Bagde Alignment
    Constructor arguments:
        id (Optional[int]): Alignment id
        badgeid (Optional[int]): Badge id
        targetName (Optional[str]): Target name
        targetUrl (Optional[str]): Target URL
        targetDescription (Optional[str]): Target description
        targetFramework (Optional[str]): Target framework
        targetCode (Optional[str]): Target code
    """
    id: Optional[int]
    badgeid: Optional[int]
    targetName: Optional[str]
    targetUrl: Optional[str]
    targetDescription: Optional[str]
    targetFramework: Optional[str]
    targetCode: Optional[str]


@dataclass
class RelatedBadge:
    """Related Badge
    Constructor arguments:
        id (int): Badge id
        name (str): Badge name
        version (Optional[str]): Version
        language (Optional[str]): Language
        type (Optional[int]): Type
    """
    id: int
    name: str
    version: Optional[str]
    language: Optional[str]
    type: Optional[int]


@dataclass
class Badge:
    """Badge
    Constructor arguments:
        id (Optional[int]): Badge id
        name (str): Badge name
        description (str): Badge description
        timecreated (Optional[int]): Time created
        timemodified (Optional[int]): Time modified
        usercreated (Optional[int]): User created
        usermodified (Optional[int]): User modified
        issuername (str): Issuer name
        issuerurl (str): Issuer URL
        issuercontact (str): Issuer contact
        expiredate (Optional[int]): Expire date
        expireperiod (Optional[int]): Expire period
        type (Optional[int]): Type
        courseid (Optional[int]): Course id
        message (Optional[str]): Message
        messagesubject (Optional[str]): Message subject
        attachment (Optional[int]): Attachment
        notification (Optional[int]): Whether to notify when badge is awarded
        nextcron (Optional[int]): Next cron
        status (Optional[int]): Status
        issuedid (Optional[int]): Issued id
        uniquehash (str): Unique hash
        dateissued (int): Date issued
        dateexpire (Optional[int]): Date expire
        visible (Optional[int]): Visible
        email (Optional[str]): User email
        version (Optional[str]): Version
        language (Optional[str]): Language
        imageauthorname (Optional[str]): Name of the image author
        imageauthoremail (Optional[str]): Email of the image author
        imageauthorurl (Optional[str]): URL of the image author
        imagecaption (Optional[str]): Caption of the image
        badgeurl (str): Badge URL
        endorsement (Optional[BagdeEndorsement]): Badge endorsement
        alignment (List[BagdeAlignment]): Badge alignments
        relatedbadges (List[RelatedBadge]): Related badges
    """
    id: Optional[int]
    name: str
    description: str
    timecreated: Optional[int]
    timemodified: Optional[int]
    usercreated: Optional[int]
    usermodified: Optional[int]
    issuername: str
    issuerurl: str
    issuercontact: str
    expiredate: Optional[int]
    expireperiod: Optional[int]
    type: Optional[int]
    courseid: Optional[int]
    message: Optional[str]
    messagesubject: Optional[str]
    attachment: Optional[int]
    notification: Optional[int]
    nextcron: Optional[int]
    status: Optional[int]
    issuedid: Optional[int]
    uniquehash: str
    dateissued: int
    dateexpire: Optional[int]
    visible: Optional[int]
    email: Optional[str]
    version: Optional[str]
    language: Optional[str]
    imageauthorname: Optional[str]
    imageauthoremail: Optional[str]
    imageauthorurl: Optional[str]
    imagecaption: Optional[str]
    badgeurl: str
    endorsement: Optional[BagdeEndorsement] = None
    alignment: List[BagdeAlignment] = field(factory=list)
    relatedbadges: List[RelatedBadge] = field(factory=list)


@dataclass
class BadgeResponse(ResponsesFactory[Badge]):
    """BadgeResponse
    Constructor arguments:
        badges (List[Badge]): list of Badge
        warnings (List[Warning]): list of warnings
    """
    badges: List[Badge] = field(factory=list)
    warnings: List[MoodleWarning] = field(factory=list)

    @property
    def items(self) -> List[Badge]:
        return self.badges
