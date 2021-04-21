from moodle.attr import dataclass
from typing import Any, Optional
from requests.exceptions import RequestException


@dataclass
class MoodleException(Exception):
    errorcode: Optional[Any] = ""
    exception: Optional[Any] = ""
    message: Optional[str] = ""

    def __str__(self):
        return self.message or self.exception or self.errorcode


class BaseException(Exception):
    message: str = ""

    def __post_init__(self) -> None:
        self.message = self.message.capitalize()

    def __str__(self) -> str:
        return self.message


@dataclass
class EmptyResponseException(BaseException):
    message: str = "Empty response from server!"


@dataclass
class InvalidCredentialException(BaseException):
    message: str = "Wrong username or password!"


@dataclass
class NetworkMoodleException(BaseException):
    """Moodle wrapper for network related network error"""

    exception: Optional[RequestException] = None
    message: str = "A Network error occurred"
