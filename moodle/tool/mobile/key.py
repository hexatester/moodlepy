from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, field


@dataclass
class Key:
    """Autologin key
    params: key (str): Auto-login key for a single usage with time expiration.
    params: autologinurl (str): Auto-login URL.
    params: warnings (List[Warning]): list of warnings
    """
    key: str
    autologinurl: str
    warnings: List[MoodleWarning] = field(factory=list)

    def __str__(self) -> str:
        return self.key
