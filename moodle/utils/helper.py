from attr import has
from datetime import datetime
from typing import TypeVar, Any

from moodle.attr import asdict as asdict_attr

T = TypeVar("T")


def make_params(wstoken: str,
                wsfunction: str,
                moodlewsrestformat: str = 'json') -> dict:
    return {
        'wstoken': wstoken,
        'wsfunction': wsfunction,
        'moodlewsrestformat': moodlewsrestformat
    }


def to_dict(data: Any, name: str = '') -> Any:
    if not data:
        return data
    if isinstance(data, list):
        out = {}
        for idx, val in enumerate(data):
            val = to_dict(val)
            if isinstance(val, dict):
                for key, value in val.items():
                    out[f'{name}[{idx}][{key}]'] = val[key]
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
    if has(data):
        return asdict_attr(data)
    if isinstance(data, datetime):
        return datetime.timestamp(data)
    return data


def fromtimestamp(d: str):
    if not isinstance(d, str):
        return d
    elif not d.isdigit():
        return d
    return datetime.fromtimestamp(float(d))
