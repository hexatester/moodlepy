from dataclasses import dataclass, field
from typing import List
from .notification_component import NotificationComponent


@dataclass
class PreferenceComponent:
    displayname: str
    notification: List[NotificationComponent] = field(default_factory=list)
