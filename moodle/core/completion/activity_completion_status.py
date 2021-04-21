from typing import List, Optional

from moodle import MoodleWarning, ResponsesFactory
from moodle.attr import dataclass, field


@dataclass
class ActivityCompletion:
    """Activity Completion
    Args:
        cmid (int): comment ID
        modname (str): activity module name
        instance (int): instance ID
        state (int): completion state value: 0 means incomplete, 1 complete, 2 complete pass, 3 complete fail
        timecompleted (int): timestamp for completed activity
        tracking (int): type of tracking: 0 means none, 1 manual, 2 automatic
        overrideby (Optional[int]): The user id who has overriden the status, or null
        valueused (Optional[int]): Whether the completion status affects the availability of another activity.
    """

    cmid: int
    modname: str
    instance: int
    state: int
    timecompleted: int
    tracking: int
    overrideby: Optional[int]
    valueused: Optional[int]


@dataclass
class ActivityCompletionStatus(ResponsesFactory[ActivityCompletion]):
    """Activity Completion Statuses (List of activities completion status)
    Args:
        statuses (List[Activity]): List of activities completion status
        warnings (List[Warning]): list of warnings
    """

    statuses: List[ActivityCompletion] = field(factory=list)
    warnings: List[MoodleWarning] = field(factory=list)

    @property
    def items(self) -> List[ActivityCompletion]:
        return self.statuses
