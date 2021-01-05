from moodle.attr import dataclass
from moodle import MoodleWarning
from typing import Optional, List


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
    id: Optional[int]
    shortname: Optional[str]
    name: Optional[str]
    datatype: Optional[str]
    description: Optional[str]
    descriptionformat: int
    categoryid: Optional[int]
    categoryname: Optional[str]
    sortorder: Optional[int]
    required: Optional[int]
    locked: Optional[int]
    visible: Optional[int]
    forceunique: Optional[int]
    signup: Optional[int]
    defaultdata: Optional[str]
    defaultdataformat: int
    param1: Optional[str]
    param2: Optional[str]
    param3: Optional[str]
    param4: Optional[str]
    param5: Optional[str]


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
    namefields: List[str]
    passwordpolicy: Optional[str]
    sitepolicy: Optional[str]
    sitepolicyhandler: Optional[str]
    defaultcity: Optional[str]
    country: Optional[str]
    profilefields: List[ProfileField]
    recaptchapublickey: Optional[str]
    recaptchachallengehash: Optional[str]
    recaptchachallengeimage: Optional[str]
    recaptchachallengejs: Optional[str]
    warnings: List[MoodleWarning]
