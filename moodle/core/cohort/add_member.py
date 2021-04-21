from moodle.attr import dataclass
from . import CohortType, UserType


@dataclass
class AddCohortMember:
    """Adds cohort members arg

    Args:
        cohorttype (CohortType): Cohort type
        usertype (UserType): Cohort Usertype
    """

    cohorttype: CohortType
    usertype: UserType
