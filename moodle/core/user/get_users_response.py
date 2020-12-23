from dataclasses import dataclass, field
from typing import List

from moodle import ResponsesFactory
from . import User


@dataclass
class GetUsersResponse(ResponsesFactory[User]):
    users: List[User] = field(default_factory=list)
    warnings: List[Warning] = field(default_factory=list)

    @property
    def items(self) -> List[User]:
        return self.users
