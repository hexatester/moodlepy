from moodle import BaseMoodle
from moodle.utils.decorator import lazy
from . import BaseGuest, BaseManual, BaseSelf


class Enrol(BaseMoodle):
    @property  # type: ignore
    @lazy
    def guest(self) -> BaseGuest:
        return BaseGuest(self.moodle)

    @property  # type: ignore
    @lazy
    def manual(self) -> BaseManual:
        return BaseManual(self.moodle)

    @property  # type: ignore
    @lazy
    def self(self) -> BaseSelf:
        return BaseSelf(self.moodle)
