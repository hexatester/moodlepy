from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, fields
from .preference_component import PreferenceComponent
from .preference_processor import PreferenceProcessor
from .preference_user import PreferenceUser


@dataclass
class Preference:
    userid: int
    disableall: int
    processors: List[PreferenceProcessor] = fields(PreferenceProcessor)
    components: List[PreferenceComponent] = fields(PreferenceComponent)


@dataclass
class NotificationPreference:
    preferences: Preference
    warnings: List[MoodleWarning] = fields(MoodleWarning)


@dataclass
class MessagePreference:
    preferences: Preference
    blocknoncontacts: int
    entertosend: bool
    warnings: List[MoodleWarning] = fields(MoodleWarning)


@dataclass
class UserPreference:
    prefereces: List[PreferenceUser] = fields(PreferenceUser)
    warnings: List[MoodleWarning] = fields(MoodleWarning)
