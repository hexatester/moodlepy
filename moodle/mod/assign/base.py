from datetime import datetime
from typing import List, Optional, Union
from moodle import BaseMoodle
from moodle.utils.helper import from_dict
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
        res = self.moodle.post(
            'mod_assign_get_assignments',
            courseids=courseids,
            capabilities=capabilities,
            includenotenrolledcourses=includenotenrolledcourses,
        )
        return from_dict(Assignments, res)

    def get_grades(self,
                   assignmentids: List[int],
                   since: Union[datetime, int] = 0) -> Grades:
        res = self.moodle.post(
            'mod_assign_get_grades',
            assignmentids=assignmentids,
            since=since,
        )
        return from_dict(Grades, res)

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
        return [from_dict(Participant, data) for data in res] if res else []

    def lock_submissions(self, assignmentid: int,
                         userids: List[int]) -> List[Warning]:
        res = self.moodle.post(
            'mod_assign_lock_submissions',
            assignmentid=assignmentid,
            userids=userids,
        )
        return [from_dict(Warning, data) for data in res] if res else []

    def reveal_identities(self, assignmentid: int) -> List[Warning]:
        res = self.moodle.post(
            'mod_assign_reveal_identities',
            assignmentid=assignmentid,
        )
        return [from_dict(Warning, data) for data in res] if res else []

    def revert_submissions_to_draft(self, assignmentid: int,
                                    userids: List[int]) -> List[Warning]:
        res = self.moodle.post(
            'mod_assign_revert_submissions_to_draft',
            assignmentid=assignmentid,
            userids=userids,
        )
        return [from_dict(Warning, data) for data in res] if res else []

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
        return [from_dict(Warning, data) for data in res] if res else []

    def save_user_extensions(
            self, assignmentid: int, userids: List[int],
            dates: List[Union[datetime, int]]) -> List[Warning]:
        res = self.moodle.post('mod_assign_save_user_extensions',
                               assignmentid=assignmentid,
                               userids=userids,
                               dates=dates)
        return [from_dict(Warning, data) for data in res] if res else []

    def set_user_flags(self, assignmentid: int,
                       userflags: List[UserFlag]) -> List[UserFlag.Result]:
        res = self.moodle.post('mod_assign_set_user_flags',
                               assignmentid=assignmentid,
                               userflags=userflags)
        return [from_dict(UserFlag.Result, data)
                for data in res] if res else []

    def submit_for_grading(self, assignmentid: int,
                           acceptsubmissionstatement: int) -> List[Warning]:
        res = self.moodle.post(
            'mod_assign_submit_for_grading',
            assignmentid=assignmentid,
            acceptsubmissionstatement=acceptsubmissionstatement)
        return [from_dict(Warning, data) for data in res] if res else []

    def submit_grading_form(self, assignmentid: int, userid: int,
                            jsonformdata: str) -> List[Warning]:
        res = self.moodle.post('mod_assign_submit_grading_form')
        return [from_dict(Warning, data) for data in res] if res else []

    def unlock_submissions(self, assignmentid: int,
                           userids: int) -> List[Warning]:
        res = self.moodle.post('mod_assign_unlock_submissions')
        return [from_dict(Warning, data) for data in res] if res else []

    def view_assign(self, assignid: int) -> View:
        res = self.moodle.post('mod_assign_view_assign', assignid=assignid)
        return from_dict(View, res)

    def view_grading_table(self, assignid: int) -> View:
        res = self.moodle.post('mod_assign_view_grading_table')
        return from_dict(View, res)

    def view_submission_status(self, assignid: int) -> View:
        res = self.moodle.post('mod_assign_view_submission_status')
        return from_dict(View, res)

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
