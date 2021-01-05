from moodle.attr import dataclass
from typing import List
from moodle import MoodleWarning


@dataclass
class MobilePublicConfig:
    wwwroot: str
    httpswwwroot: str
    sitename: str
    guestlogin: int
    rememberusername: int
    authloginviaemail: int
    registerauth: str
    forgottenpasswordurl: str
    authinstructions: str
    authnoneenabled: int
    enablewebservices: int
    enablemobilewebservice: int
    maintenanceenabled: int
    maintenancemessage: str
    logourl: str
    compactlogourl: str
    typeoflogin: int
    launchurl: str
    mobilecssurl: str
    tool_mobile_disabledfeatures: str
    country: str
    agedigitalconsentverification: bool
    autolang: int
    lang: str
    langmenu: int
    langlist: str
    locale: str
    warnings: List[MoodleWarning]
