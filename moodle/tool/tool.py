from moodle import BaseMoodle
from . import BaseMobile


class Tool(BaseMoodle):
    def __post_init__(self, moodle) -> None:
        self._mobile = BaseMobile(moodle)

    @property
    def mobile(self) -> BaseMobile:
        return self._mobile
