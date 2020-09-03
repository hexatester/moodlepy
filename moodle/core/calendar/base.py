from dacite import from_dict
from dataclasses import dataclass
from typing import List, Optional
from moodle import BaseMoodle, ActionEvent


@dataclass
class ResultActionEvents:
    events: List[ActionEvent]
    # TODO check id type of ActionEvent
    firstid: Optional[int]
    lastid: Optional[int]


class BaseCalendar(BaseMoodle):
    def get_action_events_by_timesort(self) -> ResultActionEvents:
        data = self.moodle.get('core_calendar_get_action_events_by_timesort')
        return from_dict(ResultActionEvents, data)
