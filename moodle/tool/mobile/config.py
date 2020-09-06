from dataclasses import dataclass
from typing import List
from moodle import Warning, ResponsesFactory


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
    settings: List[Setting]
    warning: List[Warning]

    @property
    def items(self) -> List[Setting]:
        return self.settings
