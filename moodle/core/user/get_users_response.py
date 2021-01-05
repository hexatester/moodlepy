from typing import List

from moodle import ResponsesFactory
from moodle.attr import dataclass, fields
from . import User


@dataclass
class GetUsersResponse(ResponsesFactory[User]):
    users: List[User] = fields(User)
    warnings: List[Warning] = fields(Warning)

    @property
    def items(self) -> List[User]:
        return self.users
