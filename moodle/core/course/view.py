from dataclasses import dataclass
from typing import List
from moodle import Warning


@dataclass
class ViewCourse:
    status: int  # status: true if success
    warnings: List[Warning]  # list of warnings
