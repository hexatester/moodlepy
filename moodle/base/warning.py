from dataclasses import dataclass
from typing import Optional


@dataclass
class Warning:
    item: Optional[str]
    itemid: Optional[int]
    warningcode: str
    message: str

    def __str__(self) -> str:
        return self.message
