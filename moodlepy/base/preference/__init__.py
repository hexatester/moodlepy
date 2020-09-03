from dataclasses import dataclass, field
from typing import List
from .preference_component import PreferenceComponent
from .preference_processor import PreferenceProcessor


@dataclass
class Preference:
    userid: int
    disableall: int
    processors: List[PreferenceProcessor] = field(default_factory=list)
    components: List[PreferenceComponent] = field(default_factory=list)


@dataclass
class NotificationPreference(Preference):
    pass


@dataclass
class MessagePreference(Preference):
    pass
