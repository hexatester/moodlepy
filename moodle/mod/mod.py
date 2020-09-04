from moodle import BaseMoodle
from . import BaseForum


class Mod(BaseMoodle):
    def __post_init__(self, moodle) -> None:
        self._forum = BaseForum(moodle)

    @property
    def forum(self) -> BaseForum:
        return self._forum
