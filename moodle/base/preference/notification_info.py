from moodle.attr import dataclass


@dataclass
class NotificationInfo:
    name: str
    displayname: str
    checked: bool
