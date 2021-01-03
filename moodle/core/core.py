from moodle import BaseMoodle
from moodle.utils.decorator import lazy
from . import (
    BaseAuth,
    BaseBackup,
    BaseBadges,
    BaseBlock,
    BaseBlog,
    BaseCalendar,
    BaseCohort,
    BaseComment,
    BaseCompetency,
    BaseCompletion,
    BaseCourse,
    BaseCustomfield,
    BaseEnrol,
    BaseMessage,
    BaseNotes,
    BaseUser,
    BaseWebservice,
)


class Core(BaseMoodle):
    @property  # type: ignore
    @lazy
    def auth(self) -> BaseAuth:
        return BaseAuth(self.moodle)

    @property  # type: ignore
    @lazy
    def backup(self) -> BaseBackup:
        return BaseBackup(self.moodle)

    @property  # type: ignore
    @lazy
    def bagdes(self) -> BaseBadges:
        return BaseBadges(self.moodle)

    @property  # type: ignore
    @lazy
    def block(self) -> BaseBlock:
        return BaseBlock(self.moodle)

    @property  # type: ignore
    @lazy
    def blog(self) -> BaseBlog:
        return BaseBlog(self.moodle)

    @property  # type: ignore
    @lazy
    def calendar(self) -> BaseCalendar:
        return BaseCalendar(self.moodle)

    @property  # type: ignore
    @lazy
    def cohort(self) -> BaseCohort:
        return BaseCohort(self.moodle)

    @property  # type: ignore
    @lazy
    def comment(self) -> BaseComment:
        return BaseComment(self.moodle)

    @property  # type: ignore
    @lazy
    def competency(self) -> BaseCompetency:
        return BaseCompetency(self.moodle)

    @property  # type: ignore
    @lazy
    def completion(self) -> BaseCompletion:
        return BaseCompletion(self.moodle)

    @property  # type: ignore
    @lazy
    def course(self) -> BaseCourse:
        return BaseCourse(self.moodle)

    @property  # type: ignore
    @lazy
    def customfield(self) -> BaseCustomfield:
        return BaseCustomfield(self.moodle)

    @property  # type: ignore
    @lazy
    def enrol(self) -> BaseEnrol:
        return BaseEnrol(self.moodle)

    @property  # type: ignore
    @lazy
    def message(self) -> BaseMessage:
        return BaseMessage(self.moodle)

    @property  # type: ignore
    @lazy
    def notes(self) -> BaseNotes:
        return BaseNotes(self.moodle)

    @property  # type: ignore
    @lazy
    def user(self) -> BaseUser:
        return BaseUser(self.moodle)

    @property  # type: ignore
    @lazy
    def webservice(self) -> BaseWebservice:
        return BaseWebservice(self.moodle)
