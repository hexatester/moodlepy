from moodle import BaseMoodle
from . import (BaseBlog, BaseCalendar, BaseCohort, BaseComment, BaseCompetency,
               BaseCourse, BaseMessage, BaseUser, BaseWebservice)


class Core(BaseMoodle):
    def __post_init__(self, moodle) -> None:
        self._blog = BaseBlog(moodle)
        self._calendar = BaseCalendar(moodle)
        self._cohort = BaseCohort(moodle)
        self._comment = BaseComment(moodle)
        self._competency = BaseCompetency(moodle)
        self._course = BaseCourse(moodle)
        self._message = BaseMessage(moodle)
        self._user = BaseUser(moodle)
        self._webservice = BaseWebservice(moodle)

    @property
    def calendar(self) -> BaseCalendar:
        return self._calendar

    @property
    def cohort(self) -> BaseCohort:
        return self._cohort

    @property
    def comment(self) -> BaseComment:
        return self._comment

    @property
    def competency(self) -> BaseCompetency:
        return self._competency

    @property
    def course(self) -> BaseCourse:
        return self._course

    @property
    def blog(self) -> BaseBlog:
        return self._blog

    @property
    def message(self) -> BaseMessage:
        return self._message

    @property
    def user(self) -> BaseUser:
        return self._user

    @property
    def webservice(self) -> BaseWebservice:
        return self._webservice
