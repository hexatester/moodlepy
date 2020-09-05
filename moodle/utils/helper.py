from dacite import from_dict as dacite_from_dict
from dacite.data import Data
from typing import Type, TypeVar
from moodle.config import DACITE_CONFIG

T = TypeVar("T")


def make_params(wstoken: str,
                wsfunction: str,
                moodlewsrestformat: str = 'json') -> dict:
    return {
        'wstoken': wstoken,
        'wsfunction': wsfunction,
        'moodlewsrestformat': moodlewsrestformat
    }


def from_dict(data_class: Type[T], data: Data) -> T:
    return dacite_from_dict(data_class, data, config=DACITE_CONFIG)
