from moodle import BaseMoodle
from . import BaseGuest


class Enrol(BaseMoodle):
    def __post_init__(self, moodle) -> None:
        self._guest = BaseGuest(moodle)

    @property
    def guest(self) -> BaseGuest:
        return self._guest
