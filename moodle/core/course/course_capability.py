from typing import List

from moodle.attr import dataclass, field


@dataclass
class CourseCapability:
    """Course Capability

    Args:
        courseid (int): Course ID number in the Moodle course table
        capabilities (List[str]): Capability name, such as mod/forum:viewdiscussion
    """
    courseid: int
    capabilities: List[str] = field(factory=list)
