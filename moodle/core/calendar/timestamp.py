from typing import List, Optional

from moodle import ResponsesFactory
from moodle.attr import dataclass, fields


@dataclass
class Timestamp:
    """Timestamp

    Args:
        key (str): Timestamp key
        timestamp (int): Unix timestamp
    """
    key: str
    timestamp: int


@dataclass
class Timestamps(ResponsesFactory[Timestamp]):
    """list of Timestamp
    """
    timestamps: List[Timestamp] = fields(Timestamp)

    @property
    def items(self) -> List[Timestamp]:
        return self.timestamps

    @dataclass
    class Create:
        """Arg for core_calendar_get_timestamps

        Args:
            key (Optional[str]): key
            year (int): year
            month (int): month
            day (int): day
            hour (Optional[int]): hour
            minute (Optional[int]): minute
        """
        key: Optional[str]
        year: int
        month: int
        day: int
        hour: Optional[int]
        minute: Optional[int]
