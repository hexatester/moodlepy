from moodle import BaseMoodle
from moodle.utils.decorator import lazy
from . import (
    BaseAssign,
    BaseBook,
    BaseChat,
    BaseData,
    BaseFolder,
    BaseForum,
    BaseLesson,
    BasePage,
    BaseResource,
    BaseUrl,
    BaseWorkshop,
)


class Mod(BaseMoodle):
    @property  # type: ignore
    @lazy
    def assign(self) -> BaseAssign:
        return BaseAssign(self.moodle)

    @property  # type: ignore
    @lazy
    def book(self) -> BaseBook:
        return BaseBook(self.moodle)

    @property  # type: ignore
    @lazy
    def chat(self) -> BaseChat:
        return BaseChat(self.moodle)

    @property  # type: ignore
    @lazy
    def data(self) -> BaseData:
        return BaseData(self.moodle)

    @property  # type: ignore
    @lazy
    def folder(self) -> BaseFolder:
        return BaseFolder(self.moodle)

    @property  # type: ignore
    @lazy
    def forum(self) -> BaseForum:
        return BaseForum(self.moodle)

    @property  # type: ignore
    @lazy
    def lesson(self) -> BaseLesson:
        return BaseLesson(self.moodle)

    @property  # type: ignore
    @lazy
    def page(self) -> BasePage:
        return BasePage(self.moodle)

    @property  # type: ignore
    @lazy
    def resource(self) -> BaseResource:
        return BaseResource(self.moodle)

    @property  # type: ignore
    @lazy
    def url(self) -> BaseUrl:
        return BaseUrl(self.moodle)

    @property  # type: ignore
    @lazy
    def workshop(self) -> BaseWorkshop:
        return BaseWorkshop(self.moodle)
