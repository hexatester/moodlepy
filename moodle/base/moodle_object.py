from __future__ import annotations
from typing import Type, TypeVar, TYPE_CHECKING
from moodle.utils.helper import from_dict
if TYPE_CHECKING:
    from moodle import Moodle

T = TypeVar('T')


class MoodleObject(object):
    @classmethod
    def from_data(cls: Type[T], data: dict, moodle: Moodle) -> T:
        self = from_dict(cls, data)
        return self
