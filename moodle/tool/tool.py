from moodle import BaseMoodle
from moodle.utils.decorator import lazy_property
from . import BaseMobile


class Tool(BaseMoodle):
    @lazy_property
    def mobile(self) -> BaseMobile:
        return BaseMobile(self.moodle)
