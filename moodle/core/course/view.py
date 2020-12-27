from dataclasses import dataclass
from typing import List
from moodle import MoodleWarning


@dataclass
class ViewCourse:
    status: int  # status: true if success
    warnings: List[MoodleWarning]  # list of warnings
