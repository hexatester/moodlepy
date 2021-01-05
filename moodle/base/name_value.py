from moodle.attr import dataclass


@dataclass
class BaseNameValue:
    name: str
    value: str
