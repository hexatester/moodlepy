from typing import List

from moodle.attr import dataclass, fields
from .notification_processor import NotificationProcessor


@dataclass
class NotificationComponent:
    displayname: str
    preferencekey: str
    processors: List[NotificationProcessor] = fields(NotificationProcessor)
