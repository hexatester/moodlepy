from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, field


@dataclass
class TokenPrivateToken:
    """Token and Private Token

    Args:
        token (str): A valid WebService token for the official mobile app service.
        privatetoken (str): Private token used for auto-login processes.
        warnings (List[MoodleWarning]): list of warnings
    """

    token: str
    privatetoken: str
    warnings: List[MoodleWarning] = field(factory=list)
