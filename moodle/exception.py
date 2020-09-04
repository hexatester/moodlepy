from dataclasses import dataclass
from typing import Optional


@dataclass
class MoodleException(Exception):
    errorcode: Optional[str] = ''
    exception: Optional[str] = ''
    message: Optional[str] = ''

    def __str__(self):
        return self.message or self.exception or self.errorcode
