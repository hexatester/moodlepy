from datetime import datetime
from typing import List, Optional, Union

from moodle import BaseMoodle
from . import (
    Assignments,
    Grades,
    Participant,
    PluginData,
    AdvanceGradingData,
    UserFlag,
    View,
)


class BaseAssign(BaseMoodle):
    def get_assignments(
            self,
            courseids: Optional[List[int]] = None,
            capabilities: Optional[List[str]] = None,
            includenotenrolledcourses: Optional[int] = None) -> Assignments:
        """Returns the courses and assignments for the users capability

        Args:
            courseids (Optional[List[int]], optional): 0 or more course ids. Defaults to None.
            capabilities (Optional[List[str]], optional): list of capabilities used to filter courses. Defaults to None.
            includenotenrolledcourses (Optional[int], optional): whether to return courses that the user can see even if is not enroled in. This requires the parameter courseids to not be empty. Defaults to None.

        Returns:
            Assignments: Returns the courses and assignments for the users capability
        """
        res = self.moodle.post(
            'mod_assign_get_assignments',
            courseids=courseids,
            capabilities=capabilities,
            includenotenrolledcourses=includenotenrolledcourses,
        )
        return self._tr(Assignments, **res)

    def get_grades(self,
                   assignmentids: List[int],
                   since: Union[datetime, int] = 0) -> Grades:
        """Returns grades from the assignment

        Args:
            assignmentids (List[int]): 1 or more assignment ids
            since (Union[datetime, int], optional):  timestamp, only return records where timemodified >= since. Defaults to 0.

        Returns:
            Grades: Returns grades from the assignment
        """
        res = self.moodle.post(
            'mod_assign_get_grades',
            assignmentids=assignmentids,
            since=since,
        )
        return self._tr(Grades, **res)

    def list_participants(
            self,
            assignid: int,
            groupid: int,
            filter: str,
            skip: int = 0,
            limit: int = 0,
            onlyids: Optional[int] = None,
            includeenrolments: int = 1,
            tablesort: Optional[int] = None) -> List[Participant]:
        """List the participants for a single assignment, with some summary info about their submissions.

        Args:
            assignid (int): assign instance id
            groupid (int): group id
            filter (str): search string to filter the results
            skip (int, optional): number of records to skip. Defaults to 0.
            limit (int, optional): maximum number of records to return. Defaults to 0.
            onlyids (Optional[int], optional): Do not return all user fields. Defaults to None.
            includeenrolments (int, optional): Do return courses where the user is enrolled. Defaults to 1.
            tablesort (Optional[int], optional): Apply current user table sorting preferences.. Defaults to None.

        Returns:
            List[Participant]: list of participant
        """
        res = self.moodle.post(
            'mod_assign_list_participants',
            assignid=assignid,
            groupid=groupid,
            filter=filter,
            skip=skip,
            limit=limit,
            onlyids=onlyids,
            includeenrolments=includeenrolments,
            tablesort=tablesort,
        )
        return self._trs(Participant, res)

    def lock_submissions(self, assignmentid: int,
                         userids: List[int]) -> List[Warning]:
        res = self.moodle.post(
            'mod_assign_lock_submissions',
            assignmentid=assignmentid,
            userids=userids,
        )
        return self._trs(Warning, res)

    def reveal_identities(self, assignmentid: int) -> List[Warning]:
        res = self.moodle.post(
            'mod_assign_reveal_identities',
            assignmentid=assignmentid,
        )
        return self._trs(Warning, res)

    def revert_submissions_to_draft(self, assignmentid: int,
                                    userids: List[int]) -> List[Warning]:
        res = self.moodle.post(
            'mod_assign_revert_submissions_to_draft',
            assignmentid=assignmentid,
            userids=userids,
        )
        return self._trs(Warning, res)

    def save_grade(
            self,
            assignmentid: int,
            userid: int,
            grade: float,
            attemptnumber: int,
            addattempt: int,
            workflowstate: str,
            applytoall: int,
            plugindata: Optional[PluginData] = None,
            advancedgradingdata: Optional[AdvanceGradingData] = None) -> None:
        self.moodle.post(
            'mod_assign_save_grade',
            assignmentid=assignmentid,
            userid=userid,
            grade=grade,
            attemptnumber=attemptnumber,
            addattempt=addattempt,
            workflowstate=workflowstate,
            applytoall=applytoall,
            plugindata=plugindata,
            advancedgradingdata=advancedgradingdata,
        )

    def save_grades(self, assignmentid: int, applytoall: int,
                    grades: List[Grades.Create]) -> None:
        self.moodle.post('mod_assign_save_grades',
                         assignmentid=assignmentid,
                         applytoall=applytoall,
                         grades=grades)

    def save_submission(self, assignmentid: int,
                        plugindata: PluginData) -> List[Warning]:
        res = self.moodle.post('mod_assign_save_submission',
                               assignmentid=assignmentid,
                               plugindata=plugindata)
        return self._trs(Warning, res)

    def save_user_extensions(
            self, assignmentid: int, userids: List[int],
            dates: List[Union[datetime, int]]) -> List[Warning]:
        res = self.moodle.post('mod_assign_save_user_extensions',
                               assignmentid=assignmentid,
                               userids=userids,
                               dates=dates)
        return self._trs(Warning, res)

    def set_user_flags(self, assignmentid: int,
                       userflags: List[UserFlag]) -> List[UserFlag.Result]:
        res = self.moodle.post('mod_assign_set_user_flags',
                               assignmentid=assignmentid,
                               userflags=userflags)
        return self._trs(UserFlag.Result, res)

    def submit_for_grading(self, assignmentid: int,
                           acceptsubmissionstatement: int) -> List[Warning]:
        """Submit the current students assignment for grading

        Args:
            assignmentid (int): The assignment id to operate on
            acceptsubmissionstatement (int): Accept the assignment submission statement

        Returns:
            List[Warning]: list of warnings
        """
        res = self.moodle.post(
            'mod_assign_submit_for_grading',
            assignmentid=assignmentid,
            acceptsubmissionstatement=acceptsubmissionstatement)
        return self._trs(Warning, res)

    def submit_grading_form(self, assignmentid: int, userid: int,
                            jsonformdata: str) -> List[Warning]:
        """Submit the grading form data via ajax

        Args:
            assignmentid (int): The assignment id to operate on
            userid (int): The user id the submission belongs to
            jsonformdata (str): The data from the grading form, encoded as a json array

        Returns:
            List[Warning]: list of warnings
        """
        res = self.moodle.post('mod_assign_submit_grading_form')
        return self._trs(Warning, res)

    def unlock_submissions(self, assignmentid: int,
                           userids: int) -> List[Warning]:
        res = self.moodle.post('mod_assign_unlock_submissions')
        return self._trs(Warning, res)

    def view_assign(self, assignid: int) -> View:
        res = self.moodle.post('mod_assign_view_assign', assignid=assignid)
        return self._tr(View, **res)

    def view_grading_table(self, assignid: int) -> View:
        res = self.moodle.post('mod_assign_view_grading_table')
        return self._tr(View, **res)

    def view_submission_status(self, assignid: int) -> View:
        res = self.moodle.post('mod_assign_view_submission_status')
        return self._tr(View, **res)

    def get_submissions(self):
        # TODO mod_assign_get_submissions
        res = self.moodle.post('mod_assign_get_submissions')
        return res

    def get_user_flags(self):
        # TODO mod_assign_get_user_flags
        res = self.moodle.post('mod_assign_get_user_flags')
        return res

    def get_user_mappings(self):
        # TODO mod_assign_get_user_mappings
        res = self.moodle.post('mod_assign_get_user_mappings')
        return res

    def get_submission_status(self):
        # TODO mod_assign_get_submission_status
        res = self.moodle.post('mod_assign_get_submission_status')
        return res

    def get_participant(self):
        # TODO mod_assign_get_participant
        res = self.moodle.post('mod_assign_get_participant')
        return res
