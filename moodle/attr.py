from attr import attrs, attrib, has, Attribute
from attr import asdict as asdict_attr
from datetime import datetime
from functools import partial
from typing import Any, Callable, List

COMMON: List = [str, int, datetime]


def serialize(inst=None,
              field: Attribute = None,
              value: Any = None,
              name: str = None) -> Any:
    if not value:
        return value
    if not name:
        name = getattr(field, 'name', '')
    if isinstance(value, list):
        out = {}
        for idx, val in enumerate(value):
            val = serialize(value=val)
            if isinstance(val, dict):
                for key, value in val.items():
                    out[f'{name}[{idx}][{key}]'] = val[key]
            else:
                out_key = name or ''
                # Check if data required name prefix
                if hasattr(value, 'name'):
                    out_key += f"[{getattr(value, 'name')}]"
                out_key += f'[{idx}]'
                out[out_key] = val
        return out
    elif isinstance(value, dict):
        out = {}
        for key, value in value.items():
            if isinstance(value, list):
                out.update(serialize(value=val, name=key))
            else:
                out[key] = value
        return out
    elif has(value):
        return asdict_attr(value, value_serializer=serialize)  # type: ignore
    elif isinstance(value, datetime):
        return datetime.timestamp(value)
    return value


asdict: Callable = partial(
    asdict_attr,
    value_serializer=serialize,
)
dataclass: Callable = partial(
    attrs,
    auto_attribs=True,
    slots=True,
)
field = attrib
