from dataclasses import dataclass


@dataclass
class EnrolledCourse:
    """
    id (int): Id of the course
    fullname (str): Fullname of the course
    shortname (str): Shortname of the course
    """
    id: int
    fullname: str
    shortname: str
