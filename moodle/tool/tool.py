from moodle import BaseMoodle
from moodle.utils.decorator import lazy
from . import BaseMobile


class Tool(BaseMoodle):
    @property  # type: ignore
    @lazy
    def mobile(self) -> BaseMobile:
        return BaseMobile(self.moodle)
