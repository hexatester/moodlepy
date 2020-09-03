from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from moodle import Moodle


class BaseMoodle(object):
    def __init__(self, moodle):
        self._moodle = moodle
        self.__post_init__(moodle)

    def __post_init__(self, moodle) -> None:
        pass

    @property
    def moodle(self) -> Moodle:
        return self._moodle
