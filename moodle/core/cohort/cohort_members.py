from typing import List

from moodle import ResponsesFactory
from moodle.attr import dataclass


@dataclass
class CohortMembers(ResponsesFactory[int]):
    """Cohort's Members

    Args:
        cohortid (int): cohort record id
        userids (List[int]): list of user id
    """
    cohortid: int
    userids: List[int]

    @property
    def items(self) -> List[int]:
        return self.userids
