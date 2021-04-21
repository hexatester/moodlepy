from moodle.attr import dataclass


@dataclass
class DeleteCohort:
    """arg for core_cohort_delete_cohort_members

    Args:
        cohortid (int): cohort record id
        userid (int): user id
    """

    cohortid: int
    userid: int
