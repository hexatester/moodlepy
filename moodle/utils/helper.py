from dacite import from_dict as dacite_from_dict
from dacite.data import Data
from dataclasses import is_dataclass, asdict
from datetime import datetime
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


def to_dict(data: Any, name: str = '') -> Any:
    if not data:
        return data
    if isinstance(data, list):
        out = {}
        for idx, val in enumerate(data):
            val = to_dict(val)
            if isinstance(val, dict):
                for key, value in val.items():
                    out[f'{name}[{idx}][{key}]'] = val
            else:
                out_key = name
                # Check if data required name prefix
                if hasattr(data, 'name'):
                    out_key += f"[{getattr(data, 'name')}]"
                out_key += f'[{idx}]'
                out[out_key] = val
        return out
    if isinstance(data, dict):
        out = {}
        for key, value in data.items():
            if isinstance(value, list):
                out.update(to_dict(value, key))
            else:
                out[key] = value
        return out
    if is_dataclass(data):
        return asdict(data)
    if isinstance(data, datetime):
        return datetime.timestamp(data)
    return data
