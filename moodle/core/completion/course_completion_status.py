from dataclasses import dataclass, field
from typing import List
from moodle import MoodleWarning


@dataclass
class CourseCompletionDetail:
    """Completion details
    Args:
        type (str): Type description
        criteria (str): Criteria description
        requirement (str): Requirement description
        status (str): Status description, can be anything
    """
    type: str
    criteria: str
    requirement: str
    status: str


@dataclass
class CourseCompletion:
    """Course Completion
    Args:
        type (int): Completion criteria type
        title (str): Completion criteria Title
        status (str): Completion status (Yes/No) a % or number
        complete (int): Completion status (true/false)
        timecompleted (int): Timestamp for criteria completetion
        details (CourseCompletionDetail): details
    """
    type: int
    title: str
    status: str
    complete: int
    timecompleted: int
    details: CourseCompletionDetail


@dataclass
class CompletionStatus:
    """Completion Status
    Args:
        completed (int): true if the course is complete, false otherwise
        aggregation (int): aggregation method 1 means all, 2 means any
        completions (List[CourseCompletion]): list of CourseCompletion
    """
    completed: int
    aggregation: int
    completions: List[CourseCompletion] = field(default_factory=list)


@dataclass
class CourseCompletionStatus:
    """Course Completion Status
    Args:
        completionstatus (CompletionStatus): Course status
        warnings (List[Warning]): list of warnings
    """
    completionstatus: CompletionStatus
    warnings: List[MoodleWarning]
