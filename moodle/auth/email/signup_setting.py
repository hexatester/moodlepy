from typing import Optional, List

from moodle import MoodleWarning
from moodle.attr import dataclass, field


@dataclass
class ProfileField:
    """ProfileField
    Args:
        id (Optional[int]): Profile field id
        shortname (Optional[str]): Profile field shortname
        name (Optional[str]): Profield field name
        datatype (Optional[str]): Profield field datatype
        description (Optional[str]): Profield field description
        descriptionformat (int): description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        categoryid (Optional[int]): Profield field category id
        categoryname (Optional[str]): Profield field category name
        sortorder (Optional[int]): Profield field sort order
        required (Optional[int]): Profield field required
        locked (Optional[int]): Profield field locked
        visible (Optional[int]): Profield field visible
        forceunique (Optional[int]): Profield field unique
        signup (Optional[int]): Profield field in signup form
        defaultdata (Optional[str]): Profield field default data
        defaultdataformat (int): defaultdata format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        param1 (Optional[str]): Profield field settings
        param2 (Optional[str]): Profield field settings
        param3 (Optional[str]): Profield field settings
        param4 (Optional[str]): Profield field settings
        param5 (Optional[str]): Profield field settings
    """

    descriptionformat: int
    defaultdataformat: int
    id: Optional[int] = None
    shortname: Optional[str] = None
    name: Optional[str] = None
    datatype: Optional[str] = None
    description: Optional[str] = None
    categoryid: Optional[int] = None
    categoryname: Optional[str] = None
    sortorder: Optional[int] = None
    required: Optional[int] = None
    locked: Optional[int] = None
    visible: Optional[int] = None
    forceunique: Optional[int] = None
    signup: Optional[int] = None
    defaultdata: Optional[str] = None
    param1: Optional[str] = None
    param2: Optional[str] = None
    param3: Optional[str] = None
    param4: Optional[str] = None
    param5: Optional[str] = None


@dataclass
class SignupSetting:
    """SignupSetting
    Args:
        namefields (List[str]): The order of the name fields
        passwordpolicy (Optional[str]): Password policy
        sitepolicy (Optional[str]): Site policy
        sitepolicyhandler (Optional[str]): Site policy handler
        defaultcity (Optional[str]): Default city
        country (Optional[str]): Default country
        profilefields (List[ProfileField]): Required profile fields
        recaptchapublickey (Optional[str]): Recaptcha public key
        recaptchachallengehash (Optional[str]): Recaptcha challenge hash
        recaptchachallengeimage (Optional[str]): Recaptcha challenge noscript image
        recaptchachallengejs (Optional[str]): Recaptcha challenge js url
        warnings (List[Warning]): list of warnings
    """

    namefields: List[str] = field(factory=list)
    passwordpolicy: Optional[str] = None
    sitepolicy: Optional[str] = None
    sitepolicyhandler: Optional[str] = None
    defaultcity: Optional[str] = None
    country: Optional[str] = None
    profilefields: List[ProfileField] = field(factory=list)
    recaptchapublickey: Optional[str] = None
    recaptchachallengehash: Optional[str] = None
    recaptchachallengeimage: Optional[str] = None
    recaptchachallengejs: Optional[str] = None
    warnings: List[MoodleWarning] = field(factory=list)
