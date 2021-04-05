from moodle import MoodleWarning
from typing import List
from moodle.attr import dataclass, field


@dataclass
class CalendarExportToken:
    """Auth token for exporting a calendar.
        token (str): The calendar permanent access token for calendar export.
        warnings (List[MoodleWarning]): list of MoodleWarning
    """
    token: str
    warnings: List[MoodleWarning] = field(factory=list)

    def __str__(self):
        return self.token
