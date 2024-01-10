from moodle.attr import dataclass, field
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
    siteid: int
    sitecalendartype: str
    usercalendartype: str
    theme: str
    functions: List[Function] = field(factory=list)
    advancedfeatures: List[AdvancedFeatures] = field(factory=list)
    userprivateaccesskey: Optional[str] = None
    userissiteadmin: Optional[bool] = None
