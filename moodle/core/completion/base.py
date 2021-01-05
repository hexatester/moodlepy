from moodle import BaseMoodle
from . import ActivityCompletionStatus, CourseCompletionStatus, StatusCompletion


class BaseCompletion(BaseMoodle):
    def get_activities_completion_status(
            self, courseid: int, userid: int) -> ActivityCompletionStatus:
        """Return the activities completion status for a user in a course.

        Args:
            courseid (int): Course ID
            userid (int): User ID

        Returns:
            CompletionStatus: Activities completion status for a user in a course.
        """
        res = self.moodle.post(
            'core_completion_get_activities_completion_status',
            courseid=courseid,
            userid=userid,
        )
        return self._tr(ActivityCompletionStatus, **res)

    def get_course_completion_status(self, courseid: int,
                                     userid: int) -> CourseCompletionStatus:
        """Returns course completion status.

        Args:
            courseid (int): Course ID
            userid (int): User ID

        Returns:
            CourseCompletionStatus: Course completion status.
        """
        res = self.moodle.post(
            'core_completion_get_course_completion_status',
            courseid=courseid,
            userid=userid,
        )
        return self._tr(CourseCompletionStatus, **res)

    def mark_course_self_completed(self, courseid: int) -> StatusCompletion:
        """Update the course completion status for the current user (if course self-completion is enabled).

        Args:
            courseid (int): Course ID

        Returns:
            SelfCompleted: Response
        """
        res = self.moodle.post('core_completion_mark_course_self_completed',
                               courseid=courseid)
        return self._tr(StatusCompletion, **res)

    def update_activity_completion_status_manually(
            self, cmid: int, completed: int) -> StatusCompletion:
        """Update completion status for the current user in an activity, only for activities with manual tracking.

        Args:
            cmid (int): course module id
            completed (int): activity completed or not

        Returns:
            StatusCompletion: Response
        """
        res = self.moodle.post(
            'core_completion_update_activity_completion_status_manually',
            cmid=cmid,
            completed=completed,
        )
        return self._tr(StatusCompletion, **res)
