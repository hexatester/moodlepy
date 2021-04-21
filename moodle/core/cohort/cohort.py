from typing import List, Optional

from moodle import ResponsesFactory
from moodle.attr import dataclass, field


@dataclass
class Cohort:
    """Cohort

    Args:
        id (int): ID of the cohort
        name (str): cohort name
        idnumber (str): cohort idnumber
        description (str): cohort description
        descriptionformat (int): description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        visible (int): cohort visible
        theme (Optional[str]): cohort theme
    """

    id: int
    name: str
    idnumber: str
    description: str
    descriptionformat: int
    visible: int
    theme: Optional[str]


@dataclass
class Cohorts(ResponsesFactory[Cohort]):
    """List of Cohort"""

    cohorts: List[Cohort] = field(factory=list)

    @property
    def items(self) -> List[Cohort]:
        return self.cohorts
