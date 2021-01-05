from moodle.attr import dataclass


@dataclass
class PreferenceUser:
    name: str
    value: str
