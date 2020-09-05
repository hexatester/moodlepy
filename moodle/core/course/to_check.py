from dataclasses import dataclass


@dataclass
class CourseToCheck:
    contextlevel: str  # The context level for the file location. Only module supported right now.
    id: int  # Context instance id
    since: int  # Check updates since this time stamp
