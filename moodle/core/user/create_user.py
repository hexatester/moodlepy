from typing import List, Optional

from moodle.attr import dataclass, field
from . import UserCustomField, UserPreference


@dataclass
class CreateUser:
    """Create User

    Args:
        createpassword (Optional[int]): True if password should be created and mailed to user.
        username (str): Username policy is defined in Moodle security config.
        auth (str): Default to "manual" #Auth plugins include manual, ldap, etc
        password (Optional[str]): Plain text password consisting of any characters
        firstname (str): The first name(s) of the user
        lastname (str): The family name of the user
        email (str): A valid and unique email address
        maildisplay (Optional[int]): Email display
        city (Optional[str]): Home city of the user
        country (Optional[str]): Home country code of the user, such as AU or CZ
        timezone (Optional[str]): Timezone code such as Australia/Perth, or 99 for default
        description (Optional[str]): User profile description, no HTML
        firstnamephonetic (Optional[str]): The first name(s) phonetically of the user
        lastnamephonetic (Optional[str]): The family name phonetically of the user
        middlename (Optional[str]): The middle name of the user
        alternatename (Optional[str]): The alternate name of the user
        interests (Optional[str]): User interests (separated by commas)
        url (Optional[str]): User web page
        icq (Optional[str]): ICQ number
        skype (Optional[str]): Skype ID
        aim (Optional[str]): AIM ID
        yahoo (Optional[str]): Yahoo ID
        msn (Optional[str]): MSN ID
        idnumber (str): Default to "" An arbitrary ID code number perhaps from the institution
        institution (Optional[str]): institution
        department (Optional[str]): department
        phone1 (Optional[str]): Phone 1
        phone2 (Optional[str]): Phone 2
        address (Optional[str]): Postal address
        lang (str): Default to "en" #Language code such as "en", must exist on server
        calendartype (str): Default to "gregorian" Calendar type such as "gregorian", must exist on server
        theme (Optional[str]): Theme name such as "standard", must exist on server
        mailformat (Optional[int]): Mail format code is 0 for plain text, 1 for HTML etc
        customfields (List[UserCustomField]): User custom fields (also known as user profil fields)
        preferences (List[UserPreference]): User preferences
    """

    username: str
    auth: str
    firstname: str
    lastname: str
    email: str
    idnumber: str
    lang: str = "en"
    calendartype: str = "gregorian"
    createpassword: Optional[int] = None
    password: Optional[str] = None
    maildisplay: Optional[int] = None
    city: Optional[str] = None
    country: Optional[str] = None
    timezone: Optional[str] = None
    description: Optional[str] = None
    firstnamephonetic: Optional[str] = None
    lastnamephonetic: Optional[str] = None
    middlename: Optional[str] = None
    alternatename: Optional[str] = None
    interests: Optional[str] = None
    url: Optional[str] = None
    icq: Optional[str] = None
    skype: Optional[str] = None
    aim: Optional[str] = None
    yahoo: Optional[str] = None
    msn: Optional[str] = None
    institution: Optional[str] = None
    department: Optional[str] = None
    phone1: Optional[str] = None
    phone2: Optional[str] = None
    address: Optional[str] = None
    theme: Optional[str] = None
    mailformat: Optional[int] = None
    customfields: List[UserCustomField] = field(factory=list)
    preferences: List[UserPreference] = field(factory=list)

    @dataclass
    class Response:
        """Response for CreateUser

        Args:
            id (int): user id
            username (string): user name
        """

        id: int
        username: str
