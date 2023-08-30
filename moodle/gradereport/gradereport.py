from moodle import BaseMoodle
from moodle.utils.decorator import lazy
from . import BaseGradeReportUser


class GradeReport(BaseMoodle):
    @property
    @lazy
    def user(self) -> BaseGradeReportUser:
        return BaseGradeReportUser(self.moodle)
