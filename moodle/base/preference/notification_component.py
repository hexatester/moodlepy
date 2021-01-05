from moodle.attr import dataclass
from typing import List
from .notification_processor import NotificationProcessor


@dataclass
class NotificationComponent:
    displayname: str
    preferencekey: str
    processors: List[NotificationProcessor]
