from moodle.attr import dataclass, field
from typing import List
from moodle import MoodleWarning, ResponsesFactory


@dataclass
class Setting:
    """Mobile Setting
    Constructor arguments:
    params: name (str): The name of the setting
    params: value (str): The value of the setting
    """
    name: str
    value: str


@dataclass
class MobileConfig(ResponsesFactory[Setting]):
    settings: List[Setting] = field(factory=list)
    warning: List[MoodleWarning] = field(factory=list)

    @property
    def items(self) -> List[Setting]:
        return self.settings
