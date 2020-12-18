from dataclasses import dataclass
from typing import List

from moodle import Warning


@dataclass
class GeneralSuccess:
    """GeneralSuccess
    Args:
        success (int): True if the user was confirmed, false if he was already confirmed
        warnings (List[Warning]): list of warnings
    """
    success: int
    warnings: List[Warning]
