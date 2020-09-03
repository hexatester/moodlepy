from dataclasses import dataclass
from typing import List
from moodle import BaseNameValue, Warning


@dataclass
class Setting(BaseNameValue):
    pass


@dataclass
class MobileConfig:
    settings: List[Setting]
    warning: List[Warning]
