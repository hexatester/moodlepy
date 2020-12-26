from datetime import datetime
from typing import List, Optional, Union

from moodle import BaseMoodle
from moodle.base.general import GeneralNameValue
from moodle.utils.helper import from_dict
from . import EditUserEnrolmentResponse, EnrolledUser, EnrolmentMethod


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

    def get_course_enrolment_methods(self,
                                     courseid: int) -> List[EnrolmentMethod]:
        """Get the list of course enrolment methods

        Args:
            courseid (int): Course id

        Returns:
            List[EnrolmentMethod]: list of EnrolmentMethod
        """
        datas = self.moodle.post(
            'core_enrol_get_course_enrolment_methods',
            courseid=courseid,
        )
        return [from_dict(EnrolmentMethod, data) for data in datas]

    def get_enrolled_users(
            self, courseid: int,
            options: Optional[List[GeneralNameValue]]) -> List[EnrolledUser]:
        """Get enrolled users by course id.

        Args:
            courseid (int): course id
            options (Optional[List[GeneralNameValue]]): Option names:
                                                            * withcapability (string) return only users with this capability. This option requires 'moodle/role:review' on the course context.
                                                            * groupid (integer) return only users in this group id. If the course has groups enabled and this param isn't defined, returns all the viewable users. This option requires 'moodle/site:accessallgroups' on the course context if the user doesn't belong to the group.
                                                            * onlyactive (integer) return only users with active enrolments and matching time restrictions. This option requires 'moodle/course:enrolreview' on the course context.
                                                            * userfields ('string, string, ...') return only the values of these user fields.
                                                            * limitfrom (integer) sql limit from.
                                                            * limitnumber (integer) maximum number of returned users.
                                                            * sortby (string) sort by id, firstname or lastname. For ordering like the site does, use siteorder.
                                                            * sortdirection (string) ASC or DESC

        Returns:
            List[EnrolledUser]: list of EnrolledUser
        """
        data = self.moodle.post(
            'core_enrol_get_enrolled_users',
            courseid=courseid,
            options=options,
        )
        return [from_dict(EnrolledUser, dat) for dat in data]

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
