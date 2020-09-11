from moodle import BaseMoodle
from . import BaseAssign, BaseForum


class Mod(BaseMoodle):
    def __post_init__(self, moodle) -> None:
        self._assign = BaseAssign(moodle)
        self._forum = BaseForum(moodle)

    @property
    def assign(self) -> BaseAssign:
        return self._assign

    @property
    def forum(self) -> BaseForum:
        return self._forum
