from typing import List

from moodle import BaseMoodle, MoodleWarning
from . import (
    Cohort,
    Cohorts,
    CreateCohort,
    UpdateCohort,
    DeleteCohort,
    CohortMembers,
    AddCohortMember,
)


class BaseCohort(BaseMoodle):
    def add_cohort_members(
            self, members: List[AddCohortMember]) -> List[MoodleWarning]:
        """Adds cohort members.

        Args:
            members (List[AddCohortMember]): list of AddCohortMember

        Returns:
            List[MoodleWarning]: list of MoodleWarning, if any
        """
        data = self.moodle.get(
            'core_cohort_add_cohort_members',
            members=members,
        )
        warnings = dict(data).get('warnings', list())
        warnings = warnings if warnings else list()
        return [self._tr(MoodleWarning, **dat) for dat in data]

    def create_cohorts(self, cohorts: List[CreateCohort]) -> List[Cohort]:
        """Creates new cohorts.

        Args:
            cohorts (List[CreateCohort]): list of CreateCohort

        Returns:
            List[Cohort]: list of Cohort
        """
        data = self.moodle.get('core_cohort_create_cohorts', cohorts=cohorts)
        return [self._tr(Cohort, **dat) for dat in data]

    def delete_cohort_members(self, members: List[DeleteCohort]) -> None:
        """Deletes cohort members.

        Args:
            members (List[DeleteCohort]): list of DeleteCohort or {cohortid:int, userid:int}
        """
        self.moodle.get('core_cohort_delete_cohort_members', members=members)

    def delete_cohorts(self, cohortids: List[int]) -> None:
        """Deletes all specified cohorts.

        Args:
            cohortids (List[int]): list of cohort ID
        """
        self.moodle.get('core_cohort_delete_cohorts', cohortids=cohortids)

    def get_cohort_members(self, cohortids: List[int]) -> List[CohortMembers]:
        """Returns cohort members.

        Args:
            cohortids (List[int]): list of Cohort ID

        Returns:
            List[CohortMembers]: list of CohortMembers
        """
        data = self.moodle.get(
            'core_cohort_get_cohort_members',
            cohortids=cohortids,
        )
        return [self._tr(CohortMembers, **dat) for dat in data]

    def get_cohorts(self, cohortids: List[int]) -> List[Cohort]:
        data = self.moodle.get('core_cohort_get_cohorts', cohortids=cohortids)
        return [self._tr(Cohort, **dat) for dat in data]

    def search_cohorts(
        self,
        query: str,
        contextid: int = 0,
        contextlevel: str = "",
        instanceid: int = 0,
        includes: str = "parents",
        limitfrom: int = 0,
        limitnum: int = 25,
    ) -> Cohorts:
        """Search for cohorts.

        Args:
            query (str): Query string
            contextid (int, optional): Context ID. Either use this value, or level and instanceid.. Defaults to 0.
            contextlevel (str, optional): Context level. To be used with instanceid.. Defaults to "".
            instanceid (int, optional): Context instance ID. To be used with level. Defaults to 0.
            includes (str, optional): What other contexts to fetch the frameworks from. (all, parents, self). Defaults to "parents".
            limitfrom (int, optional): limitfrom we are fetching the records from. Defaults to 0.
            limitnum (int, optional): Number of records to fetch. Defaults to 25.

        Returns:
            Cohorts: list of Cohort
        """
        context = {
            "contextid": contextid,
            "contextlevel": contextlevel,
            "instanceid": instanceid,
        }
        data = self.moodle.get(
            'core_cohort_search_cohorts',
            query=query,
            context=context,
            includes=includes,
            limitfrom=limitfrom,
            limitnum=limitnum,
        )
        return self._tr(Cohorts, **data)

    def update_cohorts(self, cohorts: List[UpdateCohort]) -> None:
        """Updates existing cohorts.

        Args:
            cohorts (List[UpdateCohort]): list of UpdateCohort
        """
        self.moodle.get('core_cohort_update_cohorts', cohorts=cohorts)
