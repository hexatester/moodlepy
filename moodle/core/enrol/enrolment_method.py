from dataclasses import dataclass
from typing import Optional


@dataclass
class EnrolmentMethod:
    """Enrolment Method

    Args:
        id (int): id of course enrolment instance
        courseid (int): id of course
        type (str): type of enrolment plugin
        name (str): name of enrolment plugin
        status (str): status of enrolment plugin
        wsfunction (Optional[str]): webservice function to get more information
    """
    id: int
    courseid: int
    type: str
    name: str
    status: str
    wsfunction: Optional[str]
