from __future__ import annotations
from typing import Type, TYPE_CHECKING
if TYPE_CHECKING:
    from moodle import Moodle


class MoodleObject(object):
    moodle: Moodle = None  # type: ignore
    wsfunction: str = ''
    moodlewsrestformat: str = 'json'

    def __hash__(self) -> int:
        if hasattr(self, 'id') and getattr(self, 'id') is not None:
            return hash((self.__class__, getattr(self, 'id')))
        return super().__hash__()

    @classmethod
    class property:
        "Emulate PyProperty_Type() in Objects/descrobject.c"

        def __init__(self,
                     cls: Type[MoodleObject],
                     fget=None,
                     fset=None,
                     fdel=None,
                     doc=None):
            self.cls = cls
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
            if doc is None and fget is not None:
                doc = fget.__doc__
            self.__doc__ = doc

        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            if self.fget is None:
                raise AttributeError("unreadable attribute")
            return self.fget(obj)

        def __set__(self, obj, value):
            if self.fset is None:
                raise AttributeError("can't set attribute")
            self.fset(obj, value)

        def __delete__(self, obj):
            if self.fdel is None:
                raise AttributeError("can't delete attribute")
            self.fdel(obj)

        def getter(self, fget):
            return type(self)(fget, self.fset, self.fdel, self.__doc__)

        def setter(self, fset):
            return type(self)(self.fget, fset, self.fdel, self.__doc__)

        def deleter(self, fdel):
            return type(self)(self.fget, self.fset, fdel, self.__doc__)
