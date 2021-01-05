from typing import List

from moodle.attr import dataclass, fields
from .notification_component import NotificationComponent


@dataclass
class PreferenceComponent:
    displayname: str
    notification: List[NotificationComponent] = fields(NotificationComponent)
