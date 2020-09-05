from dacite import from_dict as dacite_from_dict
from dacite.data import Data
from dataclasses import is_dataclass, asdict
from typing import Type, TypeVar, Any
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


def to_dict(data: Any) -> Any:
    if not data:
        return data
    if type(data) == list:
        return [to_dict(d) for d in data]
    if type(data) == dict:
        out = {}
        for key, value in data.items():
            out[key] = to_dict(value)
        return out
    if is_dataclass(data):
        return asdict(data)
    return data
