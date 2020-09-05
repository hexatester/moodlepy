from typing import List, Optional
from moodle import BaseMoodle
from moodle.utils.helper import from_dict
from . import Course, CheckUpdate

CourseToCheck = CheckUpdate.CourseToCheck


class BaseCourse(BaseMoodle):
    def check_updates(self,
                      courseid: int,
                      tocheck: List[CourseToCheck],
                      filter: List[str] = []) -> CheckUpdate:
        """Check if there is updates affecting the user for the given course and contexts.

        Args:
            courseid (int): Course id to check
            tocheck (List[CourseToCheck]): Instances to check
            filter (List[str], optional): Check only for updates in these areas. Defaults to [].

        Returns:
            CheckUpdate: Update
        """
        res = self.moodle.post("core_course_check_updates")
        return from_dict(CheckUpdate, res)

    def create_categories(self):
        res = self.moodle.post("core_course_create_categories")
        return res

    def create_courses(self):
        res = self.moodle.post("core_course_create_courses")
        return res

    def delete_categories(self):
        res = self.moodle.post("core_course_delete_categories")
        return res

    def delete_courses(self):
        res = self.moodle.post("core_course_delete_courses")
        return res

    def delete_modules(self):
        res = self.moodle.post("core_course_delete_modules")
        return res

    def duplicate_course(self):
        res = self.moodle.post("core_course_duplicate_course")
        return res

    def edit_module(self):
        res = self.moodle.post("core_course_edit_module")
        return res

    def edit_section(self):
        res = self.moodle.post("core_course_edit_section")
        return res

    def get_activities_overview(self):
        res = self.moodle.post("core_course_get_activities_overview")
        return res

    def get_categories(self):
        res = self.moodle.post("core_course_get_categories")
        return res

    def get_contents(self):
        res = self.moodle.post("core_course_get_contents")
        return res

    def get_course_module(self):
        res = self.moodle.post("core_course_get_course_module")
        return res

    def get_course_module_by_instance(self):
        res = self.moodle.post("core_course_get_course_module_by_instance")
        return res

    def get_courses(self, ids: Optional[List[int]] = None) -> List[Course]:
        """Get course details

        Args:
            ids (List[int], optional): List of course id. If empty return all courses except front page course. Defaults to None.

        Returns:
            List[Course]: Return course details
        """
        options = {'id': ids} if ids else {}
        res = self.moodle.post("core_course_get_courses", options=options)
        return [from_dict(Course, data) for data in res] if res else []

    def get_courses_by_field(self):
        res = self.moodle.post("core_course_get_courses_by_field")
        return res

    def get_enrolled_courses_by_timeline_classification(self):
        res = self.moodle.post(
            "core_course_get_enrolled_courses_by_timeline_classification")
        return res

    def get_enrolled_users_by_cmid(self):
        res = self.moodle.post("core_course_get_enrolled_users_by_cmid")
        return res

    def get_module(self):
        res = self.moodle.post("core_course_get_module")
        return res

    def get_recent_courses(self):
        res = self.moodle.post("core_course_get_recent_courses")
        return res

    def get_updates_since(self):
        res = self.moodle.post("core_course_get_updates_since")
        return res

    def get_user_administration_options(self):
        res = self.moodle.post("core_course_get_user_administration_options")
        return res

    def get_user_navigation_options(self):
        res = self.moodle.post("core_course_get_user_navigation_options")
        return res

    def import_course(self):
        res = self.moodle.post("core_course_import_course")
        return res

    def search_courses(self):
        res = self.moodle.post("core_course_search_courses")
        return res

    def set_favourite_courses(self):
        res = self.moodle.post("core_course_set_favourite_courses")
        return res

    def update_categories(self):
        res = self.moodle.post("core_course_update_categories")
        return res

    def update_courses(self):
        res = self.moodle.post("core_course_update_courses")
        return res

    def view_course(self):
        res = self.moodle.post("core_course_view_course")
        return res
