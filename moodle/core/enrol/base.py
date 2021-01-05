from datetime import datetime
from typing import List, Optional, Union

from moodle import BaseMoodle
from moodle.core.course import CourseCapability
from moodle.core.user import User
from moodle.base.general import GeneralNameValue
from . import EditUserEnrolmentResponse, EnrolledUser, CapabilityEnrolledUser, EnrolmentMethod


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
        return EditUserEnrolmentResponse(**data)  # type: ignore

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
        return [EnrolmentMethod(**data) for data in datas]  # type: ignore

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
        return [EnrolledUser(**dat) for dat in data]  # type: ignore

    def get_enrolled_users_with_capability(
            self, coursecapabilities: List[CourseCapability],
            options: List[GeneralNameValue]) -> List[CapabilityEnrolledUser]:
        """For each course and capability specified, return a list of the users that are enrolled in the course and have that capability

        Args:
            coursecapabilities (List[CourseCapability]): course id and associated capability name
            options (List[GeneralNameValue]): Option names:
                                                * groupid (integer) return only users in this group id. Requires 'moodle/site:accessallgroups' .
                                                * onlyactive (integer) only users with active enrolments. Requires 'moodle/course:enrolreview' .
                                                * userfields ('string, string, ...') return only the values of these user fields.
                                                * limitfrom (integer) sql limit from.
                                                * limitnumber (integer) max number of users per course and capability.

        Returns:
            List[CapabilityEnrolledUser]: list of the users that are enrolled in the course and have that capability
        """
        data = self.moodle.post(
            'core_enrol_get_enrolled_users_with_capability',
            coursecapabilities=coursecapabilities,
            options=options,
        )
        return [CapabilityEnrolledUser(**dat) for dat in data]  # type: ignore

    def get_potential_users(self, courseid: int, enrolid: int, search: str,
                            searchanywhere: int, page: int,
                            perpage: int) -> List[User]:
        """Get the list of potential users to enrol

        Args:
            courseid (int): course id
            enrolid (int): enrolment id
            search (str): query
            searchanywhere (int): find a match anywhere, or only at the beginning
            page (int): Page number
            perpage (int): Number per page

        Returns:
            List[User]: list of User
        """
        data = self.moodle.post(
            'core_enrol_get_potential_users',
            courseid=courseid,
            enrolid=enrolid,
            search=search,
            searchanywhere=searchanywhere,
            page=page,
            perpage=perpage,
        )
        return [User(**dat) for dat in data]  # type: ignore

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
