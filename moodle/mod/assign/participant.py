from typing import List, Optional

from moodle.attr import dataclass, field


@dataclass
class CustomField:
    """Custom Field

    Args:
        type (str): The type of the custom field - text field, checkbox...
        value (str): The value of the custom field
        name (str): The name of the custom field
        shortname (str): The shortname of the custom field - to be able to build the field class in the code
    """

    type: str
    value: str
    name: str
    shortname: str


@dataclass
class Preference:
    """Preference

    Args:
        name (str): The name of the preferences
        value (str): The value of the preference
    """

    name: str
    value: str


@dataclass
class Group:
    """Group

    Args:
        id (int): group id
        name (str): group name
        description (str): group description
    """

    id: int
    name: str
    description: str


@dataclass
class Role:
    """Role

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


@dataclass
class EnrolledCourse:
    """Enrolled Course

    Args:
        id (int): Id of the course
        fullname (str): Fullname of the course
        shortname (str): Shortname of the course
    """

    id: int
    fullname: str
    shortname: str


@dataclass
class Participant:
    """Participant

    Args:
        id (int): ID of the user
        username (Optional[str]): The username
        firstname (Optional[str]): The first name(s) of the user
        lastname (Optional[str]): The family name of the user
        fullname (str): The fullname of the user
        email (Optional[str]): Email address
        address (Optional[str]): Postal address
        phone1 (Optional[str]): Phone 1
        phone2 (Optional[str]): Phone 2
        icq (Optional[str]): icq number
        skype (Optional[str]): skype id
        yahoo (Optional[str]): yahoo id
        aim (Optional[str]): aim id
        msn (Optional[str]): msn number
        department (Optional[str]): department
        institution (Optional[str]): institution
        idnumber (Optional[str]): The idnumber of the user
        interests (Optional[str]): user interests (separated by commas)
        firstaccess (Optional[int]): first access to the site (0 if never)
        lastaccess (Optional[int]): last access to the site (0 if never)
        suspended (Optional[int]): Suspend user account, either false to enable user login or true to disable it
        description (Optional[str]): User profile description
        descriptionformat (Optional[int]): int format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        city (Optional[str]): Home city of the user
        url (Optional[str]): URL of the user
        country (Optional[str]): Home country code of the user, such as AU or CZ
        profileimageurlsmall (Optional[str]): User image profile URL - small version
        profileimageurl (Optional[str]): User image profile URL - big version
        customfields (List[CustomField]): User custom fields (also known as user profile fields)
        preferences (List[Preference]): Users preferences
        recordid (int): record id
        groups (List[Group]): user groups
        roles (List[Role]): user roles
        enrolledcourses (List[EnrolledCourse]): Courses where the user is enrolled - limited by which courses the user is able to see
        submitted (int): have they submitted their assignment
        requiregrading (int): is their submission waiting for grading
        grantedextension (int): have they been granted an extension
        groupid (Optional[int]): for group assignments this is the group id
        groupname (Optional[str]): for group assignments this is the group name
    """

    id: int
    fullname: str
    recordid: int
    submitted: int
    requiregrading: int
    grantedextension: int
    username: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    phone1: Optional[str] = None
    phone2: Optional[str] = None
    icq: Optional[str] = None
    skype: Optional[str] = None
    yahoo: Optional[str] = None
    aim: Optional[str] = None
    msn: Optional[str] = None
    department: Optional[str] = None
    institution: Optional[str] = None
    idnumber: Optional[str] = None
    interests: Optional[str] = None
    firstaccess: Optional[int] = None
    lastaccess: Optional[int] = None
    suspended: Optional[int] = None
    description: Optional[str] = None
    descriptionformat: Optional[int] = None
    city: Optional[str] = None
    url: Optional[str] = None
    country: Optional[str] = None
    profileimageurlsmall: Optional[str] = None
    profileimageurl: Optional[str] = None
    groupid: Optional[int] = None
    groupname: Optional[str] = None
    customfields: List[CustomField] = field(factory=list)
    preferences: List[Preference] = field(factory=list)
    groups: List[Group] = field(factory=list)
    roles: List[Role] = field(factory=list)
    enrolledcourses: List[EnrolledCourse] = field(factory=list)
