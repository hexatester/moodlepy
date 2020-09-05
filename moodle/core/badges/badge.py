from dataclasses import dataclass
from typing import Optional, List, Iterator
from moodle import Warning


@dataclass
class BagdeEndorsement:
    id: int  # Endorsement id
    badgeid: int  # Badge id
    issuername: str  # Endorsement issuer name
    issuerurl: str  # Endorsement issuer URL
    issueremail: str  # Endorsement issuer email
    claimid: str  # Claim URL
    claimcomment: str  # Claim comment
    dateissued: int  # Date issued


@dataclass
class BagdeAlignment:
    id: Optional[int]  # Alignment id
    badgeid: Optional[int]  # Badge id
    targetName: Optional[str]  # Target name
    targetUrl: Optional[str]  # Target URL
    targetDescription: Optional[str]  # Target description
    targetFramework: Optional[str]  # Target framework
    targetCode: Optional[str]  # Target code


@dataclass
class RelatedBadge:
    id: int  # Badge id
    name: str  # Badge name
    version: Optional[str]  # Version
    language: Optional[str]  # Language
    type: Optional[int]  # Type


@dataclass
class Badge:
    id: Optional[int]  # Badge id
    name: str  # Badge name
    description: str  # Badge description
    timecreated: Optional[int]  # Time created
    timemodified: Optional[int]  # Time modified
    usercreated: Optional[int]  # User created
    usermodified: Optional[int]  # User modified
    issuername: str  # Issuer name
    issuerurl: str  # Issuer URL
    issuercontact: str  # Issuer contact
    expiredate: Optional[int]  # Expire date
    expireperiod: Optional[int]  # Expire period
    type: Optional[int]  # Type
    courseid: Optional[int]  # Course id
    message: Optional[str]  # Message
    messagesubject: Optional[str]  # Message subject
    attachment: Optional[int]  # Attachment
    notification: Optional[int]  # Whether to notify when badge is awarded
    nextcron: Optional[int]  # Next cron
    status: Optional[int]  # Status
    issuedid: Optional[int]  # Issued id
    uniquehash: str  # Unique hash
    dateissued: int  # Date issued
    dateexpire: Optional[int]  # Date expire
    visible: Optional[int]  # Visible
    email: Optional[str]  # User email
    version: Optional[str]  # Version
    language: Optional[str]  # Language
    imageauthorname: Optional[str]  # Name of the image author
    imageauthoremail: Optional[str]  # Email of the image author
    imageauthorurl: Optional[str]  # URL of the image author
    imagecaption: Optional[str]  # Caption of the image
    badgeurl: str  # Badge URL
    endorsement: Optional[BagdeEndorsement]  # Badge endorsement
    alignment: List[BagdeAlignment]  # Badge alignments
    relatedbadges: List[RelatedBadge]  # Related badges


@dataclass
class BadgeResponse:
    badges: List[Badge]
    warnings: List[Warning]  # list of warnings

    def __getitem__(self, index: int) -> Badge:
        return self.badges[index]

    def __iter__(self) -> Iterator[Badge]:
        return iter(self.badges)

    def __len__(self) -> int:
        return len(self.badges)

    def __bool__(self) -> bool:
        return bool(self.badges)
