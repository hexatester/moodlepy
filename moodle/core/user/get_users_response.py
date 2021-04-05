from typing import List

from moodle import ResponsesFactory
from moodle.attr import dataclass, field
from . import User


@dataclass
class GetUsersResponse(ResponsesFactory[User]):
    users: List[User] = field(factory=list)
    warnings: List[Warning] = field(factory=list)

    @property
    def items(self) -> List[User]:
        return self.users
