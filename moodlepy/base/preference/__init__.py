from dataclasses import dataclass, field
from typing import Any, List
from .preference_component import PreferenceComponent
from .preference_processor import PreferenceProcessor


@dataclass
class Preference:
    userid: int
    disableall: int
    processors: List[PreferenceProcessor] = field(default_factory=list)
    components: List[PreferenceComponent] = field(default_factory=list)


@dataclass
class NotificationPreference:
    preferences: Preference
    warnings: List[Any] = field(default_factory=list)


@dataclass
class MessagePreference:
    preferences: Preference
    blocknoncontacts: int
    entertosend: bool
    warnings: List[Any] = field(default_factory=list)
