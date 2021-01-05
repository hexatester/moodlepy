from moodle.attr import dataclass, fields
from typing import List
from . import GeneralKeyMessage


@dataclass
class GeneralResultError:
    """GeneralResultError
    Args:
        result (int): True if the user's enrolment was successfully updated
        errors (List[GeneralKeyMessage]): List of validation errors
    """
    result: int
    errors: List[GeneralKeyMessage] = fields(GeneralKeyMessage)

    def __bool__(self) -> bool:
        if isinstance(self.result, int):
            return self.result == 1
        elif isinstance(self.result, str):
            return self.result == '1' or self.result == 'true'
        return bool(self.result)
