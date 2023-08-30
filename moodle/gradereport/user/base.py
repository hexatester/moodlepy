from typing import Optional

from moodle import BaseMoodle
from moodle.gradereport.user.gradereport import GradeReport


class BaseGradeReportUser(BaseMoodle):
    def get_user_grades(
        self,
        course_id: int,
        user_id: Optional[int] = None,
        group_id: Optional[int] = None,
    ) -> GradeReport:
        """Get user grades for a course.

        Args:
            course_id (int): course id
            user_id (int, optional): user id. Defaults to None.
            group_id (int, optional): group id. Defaults to None.

        Returns:
            GradeReport: Returns the complete list of grade items for users
             in a course
        """
        data = self.moodle.post(
            "gradereport_user_get_grade_items",
            courseid=course_id,
            userid=user_id,
            groupid=group_id,
        )
        return self._tr(GradeReport, **data)
