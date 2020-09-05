from dataclasses import dataclass
from typing import Optional


@dataclass
class MoodleException(Exception):
    errorcode: Optional[str] = ''
    exception: Optional[str] = ''
    message: Optional[str] = ''

    def __str__(self):
        return self.message or self.exception or self.errorcode


@dataclass
class BaseException(Exception):
    msg: str = ''

    def __post_init__(self) -> None:
        self.msg = self.msg.capitalize()

    def __str__(self) -> str:
        return self.msg


@dataclass
class InvalidCredentialException(Exception):
    msg: str = 'Wrong username or password!'
