from dataclasses import dataclass
from typing import List
from moodle import Warning


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
    warnings: List[Warning]
