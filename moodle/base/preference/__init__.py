from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, field
from .preference_component import PreferenceComponent
from .preference_processor import PreferenceProcessor
from .preference_user import PreferenceUser


@dataclass
class Preference:
    userid: int
    disableall: int
    processors: List[PreferenceProcessor] = field(factory=list)
    components: List[PreferenceComponent] = field(factory=list)


@dataclass
class NotificationPreference:
    preferences: Preference
    warnings: List[MoodleWarning] = field(factory=list)


@dataclass
class MessagePreference:
    preferences: Preference
    blocknoncontacts: int
    entertosend: bool
    warnings: List[MoodleWarning] = field(factory=list)


@dataclass
class UserPreference:
    prefereces: List[PreferenceUser] = field(factory=list)
    warnings: List[MoodleWarning] = field(factory=list)
