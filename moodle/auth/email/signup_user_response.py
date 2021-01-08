from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, fields


@dataclass
class SignupUserResponse:
    """SignupUser
    Args:
        success (int): True if the user was created false otherwise
        warnings (List[Warning]): list of warnings
    """
    success: int
    warnings: List[MoodleWarning] = fields(MoodleWarning)
