from datetime import datetime
from typing import List, Optional, Union

from moodle import BaseMoodle
from . import Pages, Lessons, OneLesson, View


class BaseLesson(BaseMoodle):
    def finish_attempt(
        self,
        lessonid: int,
        password: str = "",
        outoftime: Optional[Union[datetime, int]] = None,
        review: Optional[int] = None,
    ):
        res = self.moodle.post(
            "mod_lesson_finish_attempt",
            lessonid=lessonid,
            password=password,
            outoftime=outoftime or "",
            review=review or "",
        )
        return res

    def get_attempts_overview(self, lessonid: int, groupid: int = 0):
        res = self.moodle.post(
            "mod_lesson_get_attempts_overview",
            lessonid=lessonid,
            groupid=groupid,
        )
        return res

    def get_content_pages_viewed(
        self, lessonid: int, lessonattempt: int, userid: Optional[int] = None
    ):
        res = self.moodle.post(
            "mod_lesson_get_content_pages_viewed",
            lessonid=lessonid,
            lessonattempt=lessonattempt,
            userid=userid,
        )
        return res

    def get_lesson(self, lessonid: int, password: str = "") -> OneLesson:
        """Return information of a given lesson.

        Args:
            lessonid (int): lesson instance id
            password (str, optional): lesson password. Defaults to ''.

        Returns:
            OneLesson: Object containing Lesson
        """
        res = self.moodle.post(
            "mod_lesson_get_lesson",
            lessonid=lessonid,
            password=password,
        )
        return self._tr(OneLesson, **res)

    def get_lesson_access_information(self, lessonid: int):
        res = self.moodle.post(
            "mod_lesson_get_lesson_access_information",
            lessonid=lessonid,
        )
        return res

    def get_lessons_by_courses(self, courseids: Optional[List[int]] = None) -> Lessons:
        """Returns a list of lessons in a provided list of courses, if no list is provided all lessons that the user can view will be returned.

        Args:
            courseids (Optional[List[int]], optional): Array of course ids. Defaults to [].

        Returns:
            Lessons: List of Lesson
        """
        res = self.moodle.post(
            "mod_lesson_get_lessons_by_courses",
            courseids=courseids or [],
        )
        return self._tr(Lessons, **res)

    def get_page_data(
        self,
        lessonid: int,
        pageid: int,
        password: str = "",
        review: str = "",
        returncontents: str = "",
    ):
        res = self.moodle.post(
            "mod_lesson_get_page_data",
            lessonid=lessonid,
            pageid=pageid,
            password=password,
            review=review,
            returncontents=returncontents,
        )
        return res

    def get_pages(self, lessonid: int, password: str = "") -> Pages:
        """Return the list of pages in a lesson (based on the user permissions).

        Args:
            lessonid (int): lesson instance id
            password (str, optional): optional password (the lesson may be protected). Defaults to ''.

        Returns:
            Pages: List of LessonPage
        """
        res = self.moodle.post(
            "mod_lesson_get_pages",
            lessonid=lessonid,
            password=password,
        )
        return self._tr(Pages, **res)

    def get_pages_possible_jumps(self, lessonid: int):
        res = self.moodle.post(
            "mod_lesson_get_pages_possible_jumps",
            lessonid=lessonid,
        )
        return res

    def get_questions_attempts(
        self,
        lessonid: int,
        attempt: int,
        correct: Optional[int] = None,
        pageid: Optional[int] = None,
        userid: Optional[int] = None,
    ):
        res = self.moodle.post(
            "mod_lesson_get_questions_attempts",
            lessonid=lessonid,
            attempt=attempt,
            correct=correct or "",
            pageid=pageid,
            userid=userid,
        )
        return res

    def get_user_attempt(self, lessonid: int, userid: int, lessonattempt: int):
        res = self.moodle.post(
            "mod_lesson_get_user_attempt",
            lessonid=lessonid,
            userid=userid,
            lessonattempt=lessonattempt,
        )
        return res

    def get_user_attempt_grade(
        self, lessonid: int, lessonattempt: int, userid: Optional[int] = None
    ):
        res = self.moodle.post(
            "mod_lesson_get_user_attempt_grade",
            lessonid=lessonid,
            lessonattempt=lessonattempt,
            userid=userid,
        )
        return res

    def get_user_grade(self, lessonid: int, userid: Optional[int] = None):
        res = self.moodle.post(
            "mod_lesson_get_user_grade",
            lessonid=lessonid,
            userid=userid,
        )
        return res

    def get_user_timers(self, lessonid: int, userid: Optional[int] = None):
        res = self.moodle.post(
            "mod_lesson_get_user_timers",
            lessonid=lessonid,
            userid=userid,
        )
        return res

    def launch_attempt(
        self,
        lessonid: int,
        password: str = "",
        pageid: int = 0,
        review: Optional[int] = None,
    ):
        res = self.moodle.post(
            "mod_lesson_launch_attempt",
            lessonid=lessonid,
            password=password,
            pageid=pageid,
            review=review,
        )
        return res

    def process_page(
        self,
        lessonid: int,
        pageid: int,
        data: List[dict],
        password: str = "",
        review: Optional[int] = None,
    ):
        res = self.moodle.post(
            "mod_lesson_process_page",
            lessonid=lessonid,
            pageid=pageid,
            data=data,
            password=password,
            review=review or "",
        )
        return res

    def view_lesson(self, lessonid: int, password: str = "") -> View:
        """Trigger the course module viewed event and update the module completion status.

        Args:
            lessonid (int): lesson instance id
            password (str, optional): lesson password. Defaults to ''.

        Returns:
            View: View lesson response
        """
        res = self.moodle.post(
            "mod_lesson_view_lesson",
            lessonid=lessonid,
            password=password,
        )
        return self._tr(View, **res)
