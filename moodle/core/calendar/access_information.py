from typing import List

from moodle import MoodleWarning
from moodle.attr import dataclass, field


@dataclass
class AccessInformation:
    """Permissions/access information
    Constructor arguments:
    params: canmanageentries (int): Whether the user can manage entries.
    params: canmanageownentries (int): Whether the user can manage its own entries.
    params: canmanagegroupentries (int): Whether the user can manage group entries.
    params: warnings (List[Warning]): list of warnings
    """
    canmanageentries: int
    canmanageownentries: int
    canmanagegroupentries: int
    warnings: List[MoodleWarning] = field(factory=list)
