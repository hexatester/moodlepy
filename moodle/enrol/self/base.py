from moodle import BaseMoodle
from . import InstanceInfo
from .enrol_user_response import EnrolUserResponse


class BaseSelf(BaseMoodle):
    def enrol_user(self,
                   courseid: int,
                   password: str,
                   instanceid: int = 0) -> EnrolUserResponse:
        """Self enrol the current user in the given course.

        Args:
            courseid (int): Id of the course
            password (str): Enrolment key
            instanceid (int, optional): Instance id of self enrolment plugin. Defaults to 0.

        Returns:
            EnrolUserResponse: Response
        """
        data = self.moodle.post(
            'enrol_self_enrol_user',
            courseid=courseid,
            password=password,
            instanceid=instanceid,
        )
        return self._tr(EnrolUserResponse, **data)

    def get_instance_info(self, instanceid: int) -> InstanceInfo:
        """self enrolment instance information.

        Args:
            instanceid (int): instance id of self enrolment plugin.

        Returns:
            InstanceInfo: Instance info
        """
        data = self.moodle.post(
            'enrol_self_get_instance_info',
            instanceid=instanceid,
        )
        return self._tr(InstanceInfo, **data)
