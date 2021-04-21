from typing import List, Optional
from moodle import BaseMoodle, Array
from . import (
    ActivityOverview,
    Course,
    CourseByField,
    SearchResult,
    CoursesBTC,
    CheckUpdate,
    Category,
    ContentOption,
    Section,
    CourseModule,
    NavigationOptions,
    ViewCourse,
)


class BaseCourse(BaseMoodle):
    def check_updates(
        self,
        courseid: int,
        tocheck: List[CheckUpdate.ToCheck],
        filter: Optional[List[str]] = None,
    ) -> CheckUpdate:
        """Check if there is updates affecting the user for the given course and contexts.

        Args:
            courseid (int): Course id to check
            tocheck (List[CourseToCheck]): Instances to check
            filter (List[str], optional): Check only for updates in these areas. Defaults to [].

        Returns:
            CheckUpdate: Update
        """
        res = self.moodle.post("core_course_check_updates")
        return self._tr(CheckUpdate, **res)

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

    def get_activities_overview(
        self,
        courseid: int,
        tocheck: List[Course.ToCheck],
        filter: Optional[List[str]] = None,
    ) -> ActivityOverview:
        res = self.moodle.post(
            "core_course_get_activities_overview",
            courseid=courseid,
            tocheck=tocheck,
            filter=filter or [],
        )
        return self._tr(ActivityOverview, **res)

    def get_categories(
        self, criteria: Optional[List[Category.Criteria]] = None
    ) -> List[Category]:
        res = self.moodle.post(
            "core_course_get_categories",
            criteria=criteria or [],
        )
        results = list()
        for data in res:
            results.append(Category(**data))  # type: ignore
        return results

    def get_contents(
        self, courseid: int, options: Optional[List[ContentOption]] = None
    ) -> List[Section]:
        """Get course contents

        Args:
            courseid (int): course id
            options (Optional[List[ContentOption]], optional): Options, used since Moodle 2.9. Defaults to None.

        Returns:
            List[Section]: list of section
        """
        res = self.moodle.post(
            "core_course_get_contents", courseid=courseid, options=options or []
        )
        return self._trs(Section, res)

    def get_course_module(self, cmid: int) -> CourseModule:
        """Return information about a course module

        Args:
            cmid (int): The course module id

        Returns:
            CourseModule: Course Module wrapper
        """
        res = self.moodle.post("core_course_get_course_module", cmid=cmid)
        return self._tr(CourseModule, **res)

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
        options = Array(ids if ids else [])
        options.name = "ids"
        res = self.moodle.post("core_course_get_courses", options=options)
        return self._trs(Course, res)

    def get_courses_by_field(self, field: str = "", value: str = "") -> CourseByField:
        """Get courses matching a specific field (id/s, shortname, idnumber, category)

        Args:
            field (str, optional): The field to search can be left empty for all courses or:
                                   id: course id
                                   ids: comma separated course ids
                                   shortname: course short name
                                   idnumber: course id number
                                   category: category id the course belongs to.
                                   Defaults to ''.
            value (str, optional): The value to match. Defaults to ''.

        Returns:
            CourseByField: List of Course
        """
        res = self.moodle.post(
            "core_course_get_courses_by_field", field=field, value=value
        )
        return self._tr(CourseByField, **res)

    def get_enrolled_courses_by_timeline_classification(
        self,
        classification: str,
        limit: int = 0,
        offset: int = 0,
        sort: Optional[str] = None,
    ) -> CoursesBTC:
        """List of enrolled courses for the given timeline classification (past, inprogress, or future).

        Args:
            classification (str): future, inprogress, or past
            limit (int, optional): Result set limit. Defaults to 0.
            offset (int, optional): Result set offset. Defaults to 0.
            sort (Optional[str], optional): Sort string. Defaults to None.

        Returns:
            CoursesBTC: List of enrolled courses
        """
        res = self.moodle.post(
            "core_course_get_enrolled_courses_by_timeline_classification",
            classification=classification,
            limit=limit,
            offset=offset,
            sort=sort,
        )
        return self._tr(CoursesBTC, **res)

    def get_recent_courses(
        self,
        userid: int = 0,
        limit: int = 0,
        offset: int = 0,
        sort: Optional[str] = None,
    ) -> List[Course]:
        res = self.moodle.post(
            "core_course_get_recent_courses",
            userid=userid,
            limit=limit,
            offset=offset,
            sort=sort,
        )
        return self._trs(Course, res)

    def get_enrolled_users_by_cmid(self):
        res = self.moodle.post("core_course_get_enrolled_users_by_cmid")
        return res

    def get_module(self):
        res = self.moodle.post("core_course_get_module")
        return res

    def get_updates_since(
        self, courseid: int, since: int, filter: Optional[List[str]] = None
    ) -> CheckUpdate:
        """Check if there are updates affecting the user for the given course since the given time stamp.

        Args:
            courseid (int): Course id to check
            since (int): Check updates since this time stamp
            filter (Optional[List[str]], optional): Check only for updates in these areas. Defaults to None.
                                                    Area name: configuration, fileareas, completion, ratings, comments, gradeitems, outcomes

        Returns:
            CheckUpdate: Update course detail
        """
        res = self.moodle.post(
            "core_course_get_updates_since",
            courseid=courseid,
            since=since,
            filter=filter,
        )
        return self._tr(CheckUpdate, **res)

    def get_user_administration_options(self):
        res = self.moodle.post("core_course_get_user_administration_options")
        return res

    def get_user_navigation_options(self, courseids: List[int]) -> NavigationOptions:
        """Return a list of navigation options in a set of courses that are avaialable or not for the current user.

        Args:
            courseids (List[int]): List of one or more course id

        Returns:
            NavigationOptions: Navigation options of courses
        """
        res = self.moodle.post(
            "core_course_get_user_navigation_options", courseids=courseids
        )
        return self._tr(NavigationOptions, **res)

    def import_course(self):
        res = self.moodle.post("core_course_import_course")
        return res

    def search_courses(
        self,
        criterianame: str,
        criteriavalue: str,
        page: int = 0,
        perpage: int = 0,
        requiredcapabilities: Optional[List[str]] = None,
        limittoenrolled: int = 0,
        onlywithcompletion: int = 0,
    ) -> SearchResult:
        """Search courses by (name, module, block, tag)

        Args:
            criterianame (str): criteria name (search, modulelist (only admins), blocklist (only admins), tagid)
            criteriavalue (str): criteria value
            page (int, optional): page number (0 based). Defaults to 0.
            perpage (int, optional): items per page. Defaults to 0.
            requiredcapabilities (Optional[List[str]], optional): Optional list of required capabilities (used to filter the list). Defaults to None.
            limittoenrolled (int, optional): limit to enrolled courses. Defaults to 0.
            onlywithcompletion (int, optional): limit to courses where completion is enabled. Defaults to 0.

        Returns:
            SearchResult: List of result courses
        """
        res = self.moodle.post(
            "core_course_search_courses",
            criterianame=criterianame,
            criteriavalue=criteriavalue,
            page=page,
            perpage=perpage,
            requiredcapabilities=requiredcapabilities,
            limittoenrolled=limittoenrolled,
            onlywithcompletion=onlywithcompletion,
        )
        return self._tr(SearchResult, **res)

    def set_favourite_courses(self):
        res = self.moodle.post("core_course_set_favourite_courses")
        return res

    def update_categories(self):
        res = self.moodle.post("core_course_update_categories")
        return res

    def update_courses(self):
        res = self.moodle.post("core_course_update_courses")
        return res

    def view_course(self, courseid: int, sectionnumber: int) -> ViewCourse:
        res = self.moodle.post("core_course_view_course")
        return self._tr(ViewCourse, **res)
