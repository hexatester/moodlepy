from moodle import BaseMoodle
from moodle.utils.helper import from_dict
from . import InstanceInfoResponse


class BaseGuest(BaseMoodle):
    def get_instance_info(self, instanceid: int) -> InstanceInfoResponse:
        data = self.moodle.post(
            'enrol_guest_get_instance_info',
            instanceid=instanceid,
        )
        return from_dict(InstanceInfoResponse, data)
