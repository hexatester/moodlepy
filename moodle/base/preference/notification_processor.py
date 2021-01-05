from moodle.attr import dataclass
from .notification_info import NotificationInfo


@dataclass
class NotificationProcessor:
    displayname: str
    name: str
    locked: bool
    userconfigured: int
    loggedin: NotificationInfo
    loggedoff: NotificationInfo
