from typing import List

from moodle import ResponsesFactory
from moodle.attr import dataclass, field


@dataclass
class CohortMembers(ResponsesFactory[int]):
    """Cohort's Members

    Args:
        cohortid (int): cohort record id
        userids (List[int]): list of user id
    """
    cohortid: int
    userids: List[int] = field(factory=list)

    @property
    def items(self) -> List[int]:
        return self.userids
