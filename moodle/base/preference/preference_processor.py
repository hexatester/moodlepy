from moodle.attr import dataclass


@dataclass
class PreferenceProcessor:
    displayname: str
    name: str
    hassettings: bool
    contextid: int
    userconfigured: int
