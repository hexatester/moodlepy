from typing import List

from moodle import BaseMoodle
from . import Enrolment


class BaseManual(BaseMoodle):
    def enrol_users(self, enrolments: List[Enrolment]) -> None:
        """Manual enrol users

        Args:
            enrolments (List[Enrolment]): enrolments

        Returns:
            None: Nothing
        """
        data = self.moodle.post(
            "enrol_manual_enrol_users",
            enrolments=enrolments,
        )
        return data

    def unenrol_users(self, enrolments: List[Enrolment]) -> None:
        """Manual unenrol users

        Args:
            enrolments (List[Enrolment]): enrolments

        Returns:
            None: Nothing
        """
        data = self.moodle.post(
            "enrol_manual_unenrol_users",
            enrolments=enrolments,
        )
        return data
