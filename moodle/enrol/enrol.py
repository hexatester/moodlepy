from moodle import BaseMoodle
from . import BaseGuest, BaseManual, BaseSelf


class Enrol(BaseMoodle):
    def __post_init__(self, moodle) -> None:
        self._guest = BaseGuest(moodle)
        self._manual = BaseManual(moodle)
        self._self = BaseSelf(moodle)

    @property
    def guest(self) -> BaseGuest:
        return self._guest

    @property
    def manual(self) -> BaseManual:
        return self._manual

    @property
    def self(self) -> BaseSelf:
        return self._self
