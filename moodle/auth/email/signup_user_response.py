from dataclasses import dataclass
from moodle import Warning
from typing import List


@dataclass
class SignupUserResponse:
    """SignupUser
    Args:
        success (int): True if the user was created false otherwise
        warnings (List[Warning]): list of warnings
    """
    success: int
    warnings: List[Warning]
