from moodle import BaseMoodle
from moodle.utils.decorator import lazy_property
from . import (
    BaseAssign,
    BaseFolder,
    BaseForum,
    BaseLesson,
    BaseResource,
    BaseUrl,
)


class Mod(BaseMoodle):
    @lazy_property
    def assign(self) -> BaseAssign:
        return BaseAssign(self.moodle)

    @lazy_property
    def folder(self) -> BaseFolder:
        return BaseFolder(self.moodle)

    @lazy_property
    def forum(self) -> BaseForum:
        return BaseForum(self.moodle)

    @lazy_property
    def lesson(self) -> BaseLesson:
        return BaseLesson(self.moodle)

    @lazy_property
    def resource(self) -> BaseResource:
        return BaseResource(self.moodle)

    @lazy_property
    def url(self) -> BaseUrl:
        return BaseUrl(self.moodle)
