from moodle import BaseMoodle
from moodle.utils.decorator import lazy_property
from . import BaseGuest, BaseManual, BaseSelf


class Enrol(BaseMoodle):
    @lazy_property
    def guest(self) -> BaseGuest:
        return BaseGuest(self.moodle)

    @lazy_property
    def manual(self) -> BaseManual:
        return BaseManual(self.moodle)

    @lazy_property
    def self(self) -> BaseSelf:
        return BaseSelf(self.moodle)
