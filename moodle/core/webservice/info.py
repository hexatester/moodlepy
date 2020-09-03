from dataclasses import dataclass
from typing import List
from .advanced_feature import AdvancedFeatures
from .function import Function


@dataclass
class SiteInfo:
    sitename: str
    username: str
    firstname: str
    lastname: str
    fullname: str
    lang: str
    userid: int
    siteurl: str
    userpictureurl: str
    functions: List[Function]
    downloadfiles: int
    uploadfiles: int
    release: str
    version: str
    mobilecssurl: str
    advancedfeatures: List[AdvancedFeatures]
    usercanmanageownfiles: bool
    userquota: int
    usermaxuploadfilesize: int
    userhomepage: int
    siteid: int
    sitecalendartype: str
    usercalendartype: str
    theme: str
