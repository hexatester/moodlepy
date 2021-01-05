from moodle.attr import dataclass, fields
from typing import List, Optional
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
    downloadfiles: int
    uploadfiles: int
    release: str
    version: str
    mobilecssurl: str
    usercanmanageownfiles: bool
    userquota: int
    usermaxuploadfilesize: int
    userhomepage: int
    userprivateaccesskey: Optional[str]
    siteid: int
    sitecalendartype: str
    usercalendartype: str
    userissiteadmin: Optional[bool]
    theme: str
    functions: List[Function] = fields(Function)
    advancedfeatures: List[AdvancedFeatures] = fields(AdvancedFeatures)
