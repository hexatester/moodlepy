from typing import Any

from moodle.mdl import Mdl

from moodle.auth import Auth
from moodle.block import Block
from moodle.core import Core
from moodle.enrol import Enrol
from moodle.gradereport import GradeReport
from moodle.mod import Mod
from moodle.tool import Tool

from moodle.utils.decorator import lazy


class Moodle(Mdl):
    def __init__(self, url: str, token: str):
        super(Moodle, self).__init__(url, token)

    def __call__(self, wsfunction: str, moodlewsrestformat="json", **kwargs) -> Any:
        return self.post(wsfunction, moodlewsrestformat, **kwargs)

    @property  # type: ignore
    @lazy
    def auth(self) -> Auth:
        return Auth(self)

    @property  # type: ignore
    @lazy
    def block(self) -> Block:
        return Block(self)

    @property  # type: ignore
    @lazy
    def core(self) -> Core:
        return Core(self)

    @property  # type: ignore
    @lazy
    def enrol(self) -> Enrol:
        return Enrol(self)

    @property  # type: ignore
    @lazy
    def grade_report(self) -> GradeReport:
        return GradeReport(self)

    @property  # type: ignore
    @lazy
    def mod(self) -> Mod:
        return Mod(self)

    @property  # type: ignore
    @lazy
    def tool(self) -> Tool:
        return Tool(self)
