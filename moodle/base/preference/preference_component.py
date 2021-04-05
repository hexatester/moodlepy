from typing import List

from moodle.attr import dataclass, field
from .notification_component import NotificationComponent


@dataclass
class PreferenceComponent:
    displayname: str
    notification: List[NotificationComponent] = field(factory=list)
