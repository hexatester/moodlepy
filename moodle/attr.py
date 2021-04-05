from attr import attrs, attrib, has, Attribute
from attr import asdict as asdict_attr
from datetime import datetime
from functools import partial
from typing import Any, Callable, List, Optional

from moodle.base.moodle_object import MoodleObject  # NOQA

COMMON: List = [str, int, datetime]


def fromtimestamp(d: str):
    if not isinstance(d, str):
        return d
    elif not d.isdigit():
        return d
    return datetime.fromtimestamp(float(d))


def hooq(cls: type, fields: List[Attribute]) -> List[Attribute]:
    results: List[Attribute] = list()
    return results


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


def auto_convert(cls, fields):
    results = []
    for field in fields:
        if field.converter is not None:
            results.append(field)
            continue
        if field.type in {datetime, 'datetime'}:
            converter = fromtimestamp
        elif field.type == Optional[field.type]:

            def converter(d=None):
                return d
        else:
            converter = None
        results.append(field.evolve(converter=converter))
    return results


asdict: Callable = partial(
    asdict_attr,
    value_serializer=serialize,
)
dataclass: Callable = partial(
    attrs,
    auto_attribs=True,
    # field_transformer=auto_convert,
)
sdataclass: Callable = partial(
    attrs,
    auto_attribs=True,
    field_transformer=auto_convert,
    slots=True,
)
field = attrib


def fields(converter: Callable):
    def conv(d: List[dict]):
        results: List = list()
        if not isinstance(d, list):
            return results
        for result in results:
            results.append(converter(**result))
        return results

    return attrib(converter=conv, factory=list)
