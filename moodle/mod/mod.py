from moodle import BaseMoodle
from . import (
    BaseAssign,
    BaseFolder,
    BaseForum,
    BaseLesson,
    BaseResource,
    BaseUrl,
)


class Mod(BaseMoodle):
    def __post_init__(self, moodle) -> None:
        self._assign = BaseAssign(moodle)
        self._folder = BaseFolder(moodle)
        self._forum = BaseForum(moodle)
        self._lesson = BaseLesson(moodle)
        self._resource = BaseResource(moodle)
        self._url = BaseUrl(moodle)

    @property
    def assign(self) -> BaseAssign:
        return self._assign

    @property
    def folder(self) -> BaseFolder:
        return self._folder

    @property
    def forum(self) -> BaseForum:
        return self._forum

    @property
    def lesson(self) -> BaseLesson:
        return self._lesson

    @property
    def resource(self) -> BaseResource:
        return self._resource

    @property
    def url(self) -> BaseUrl:
        return self._url
