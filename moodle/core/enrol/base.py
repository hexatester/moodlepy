from datetime import datetime
from typing import Union

from moodle import BaseMoodle
from moodle.utils.helper import from_dict
from . import EditUserEnrolmentResponse


class BaseEnrol(BaseMoodle):
    def edit_user_enrolment(
            self,
            courseid: int,
            ueid: int,
            status: int,
            timestart: Union[int, datetime] = 0,
            timeend: Union[int, datetime] = 0) -> EditUserEnrolmentResponse:
        """**DEPRECATED** Please do not call this function any more. External function that updates a given user enrolment

        Args:
            courseid (int): Course ID
            ueid (int): User enrolment ID
            status (int): Enrolment status
            timestart (Union[int, datetime], optional): Enrolment start timestamp. Defaults to 0.
            timeend (Union[int, datetime], optional): Enrolment end timestamp. Defaults to 0.

        Returns:
            EditUserEnrolmentResponse: Response
        """
        data = self.moodle.post(
            'core_enrol_edit_user_enrolment',
            courseid=courseid,
            ueid=ueid,
            status=status,
            timestart=timestart,
            timeend=timeend,
        )
        return from_dict(EditUserEnrolmentResponse, data)

    def get_course_enrolment_methods(self):
        data = self.moodle.post('core_enrol_get_course_enrolment_methods')
        return data

    def get_enrolled_users(self):
        data = self.moodle.post('core_enrol_get_enrolled_users')
        return data

    def get_enrolled_users_with_capability(self):
        data = self.moodle.post(
            'core_enrol_get_enrolled_users_with_capability')
        return data

    def get_potential_users(self):
        data = self.moodle.post('core_enrol_get_potential_users')
        return data

    def get_users_courses(self):
        data = self.moodle.post('core_enrol_get_users_courses')
        return data

    def search_users(self):
        data = self.moodle.post('core_enrol_search_users')
        return data

    def submit_user_enrolment_form(self):
        data = self.moodle.post('core_enrol_submit_user_enrolment_form')
        return data

    def unenrol_user_enrolment(self):
        data = self.moodle.post('core_enrol_unenrol_user_enrolment')
        return data
