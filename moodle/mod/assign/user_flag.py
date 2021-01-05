from moodle.attr import dataclass
from typing import Optional


@dataclass
class UserFlag:
    """User Flag
    Args:
        userid (int): student id
        locked (Optional[int]): locked
        mailed (Optional[int]): mailed
        extensionduedate (Optional[int]): extension due date
        workflowstate (Optional[str]): marking workflow state
        allocatedmarker (Optional[int]): allocated marker
    """
    userid: int
    locked: Optional[int]
    mailed: Optional[int]
    extensionduedate: Optional[int]
    workflowstate: Optional[str]
    allocatedmarker: Optional[int]

    @dataclass
    class Result:
        """Result
        Args:
            id (int): id of record if successful, -1 for failure
            userid (int): userid of record
            errormessage (Optional[str]): Failure error message
        """
        id: int
        userid: int
        errormessage: Optional[str]
