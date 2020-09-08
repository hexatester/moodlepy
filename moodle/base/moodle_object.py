from __future__ import annotations
from typing import Optional, Type, TypeVar, TYPE_CHECKING
from moodle.utils.helper import from_dict
if TYPE_CHECKING:
    from moodle import Moodle

T = TypeVar('T')


class MoodleObject(object):
    def __post_init__(self):
        self._moodle: Optional[Moodle] = None

    @property
    def moodle(self) -> Optional[Moodle]:
        return self._moodle

    @classmethod
    def from_data(cls: Type[T], data: dict, moodle: Moodle) -> T:
        self = from_dict(cls, data)
        setattr(self, '_moodle', moodle)
        return self

    def __str__(self) -> str:
        return getattr(self, 'name', repr(self))
