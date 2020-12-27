from moodle import BaseMoodle
from moodle.utils.decorator import lazy_property
from . import (BaseAuth, BaseBadges, BaseBlock, BaseBlog, BaseCalendar,
               BaseCohort, BaseComment, BaseCompetency, BaseCompletion,
               BaseCourse, BaseEnrol, BaseMessage, BaseNotes, BaseUser,
               BaseWebservice)


class Core(BaseMoodle):
    @lazy_property
    def auth(self) -> BaseAuth:
        return BaseAuth(self.moodle)

    @lazy_property
    def bagdes(self) -> BaseBadges:
        return BaseBadges(self.moodle)

    @lazy_property
    def block(self) -> BaseBlock:
        return BaseBlock(self.moodle)

    @lazy_property
    def blog(self) -> BaseBlog:
        return BaseBlog(self.moodle)

    @lazy_property
    def calendar(self) -> BaseCalendar:
        return BaseCalendar(self.moodle)

    @lazy_property
    def cohort(self) -> BaseCohort:
        return BaseCohort(self.moodle)

    @lazy_property
    def comment(self) -> BaseComment:
        return BaseComment(self.moodle)

    @lazy_property
    def competency(self) -> BaseCompetency:
        return BaseCompetency(self.moodle)

    @lazy_property
    def completion(self) -> BaseCompletion:
        return BaseCompletion(self.moodle)

    @lazy_property
    def course(self) -> BaseCourse:
        return BaseCourse(self.moodle)

    @lazy_property
    def enrol(self) -> BaseEnrol:
        return BaseEnrol(self.moodle)

    @lazy_property
    def message(self) -> BaseMessage:
        return BaseMessage(self.moodle)

    @lazy_property
    def notes(self) -> BaseNotes:
        return BaseNotes(self.moodle)

    @lazy_property
    def user(self) -> BaseUser:
        return BaseUser(self.moodle)

    @lazy_property
    def webservice(self) -> BaseWebservice:
        return BaseWebservice(self.moodle)
