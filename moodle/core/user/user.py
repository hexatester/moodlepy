from dataclasses import dataclass, field
from typing import List, Optional

from . import UserCustomField, UserPreference


@dataclass
class User:
    """User

    Args:
        id (int): ID of the user
        username (Optional[str]): The username
        firstname (Optional[str]): The first name(s) of the user
        lastname (Optional[str]): The family name of the user
        fullname (str): The fullname of the user
        email (Optional[str]): An email address - allow email as root@localhost
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
        idnumber (Optional[str]): An arbitrary ID code number perhaps from the institution
        interests (Optional[str]): user interests (separated by commas)
        firstaccess (Optional[int]): first access to the site (0 if never)
        lastaccess (Optional[int]): last access to the site (0 if never)
        auth (Optional[str]): Auth plugins include manual, ldap, etc
        suspended (Optional[int]): Suspend user account, either false to enable user login or true to disable it
        confirmed (Optional[int]): Active user: 1 if confirmed, 0 otherwise
        lang (Optional[str]): Language code such as "en", must exist on server
        calendartype (Optional[str]): Calendar type such as "gregorian", must exist on server
        theme (Optional[str]): Theme name such as "standard", must exist on server
        timezone (Optional[str]): Timezone code such as Australia/Perth, or 99 for default
        mailformat (Optional[int]): Mail format code is 0 for plain text, 1 for HTML etc
        description (Optional[str]): User profile description
        descriptionformat (Optional[int]): int format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        city (Optional[str]): Home city of the user
        url (Optional[str]): URL of the user
        country (Optional[str]): Home country code of the user, such as AU or CZ
        profileimageurlsmall (str): User image profile URL - small version
        profileimageurl (str): User image profile URL - big version
        customfields (List[UserCustomField]): User custom fields (also known as user profile fields)
        preferences (List[UserPreference]): Users preferences
    """
    id: int
    username: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    fullname: str
    email: Optional[str]
    address: Optional[str]
    phone1: Optional[str]
    phone2: Optional[str]
    icq: Optional[str]
    skype: Optional[str]
    yahoo: Optional[str]
    aim: Optional[str]
    msn: Optional[str]
    department: Optional[str]
    institution: Optional[str]
    idnumber: Optional[str]
    interests: Optional[str]
    firstaccess: Optional[int]
    lastaccess: Optional[int]
    auth: Optional[str]
    suspended: Optional[int]
    confirmed: Optional[int]
    lang: Optional[str]
    calendartype: Optional[str]
    theme: Optional[str]
    timezone: Optional[str]
    mailformat: Optional[int]
    description: Optional[str]
    descriptionformat: Optional[int]
    city: Optional[str]
    url: Optional[str]
    country: Optional[str]
    profileimageurlsmall: str
    profileimageurl: str
    customfields: List[UserCustomField] = field(default_factory=list)
    preferences: List[UserPreference] = field(default_factory=list)
