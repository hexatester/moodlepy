from dataclasses import dataclass
from typing import List
from moodle import Warning


@dataclass
class View:
    """View Response
    Args:
        status (int): status: true if success
        warnings (List[Warning]): list of warnings
    """
    status: int
    warnings: List[Warning]
