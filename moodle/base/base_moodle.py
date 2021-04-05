import cattr
from typing import Any, Iterable, List, Type, TypeVar, TYPE_CHECKING
if TYPE_CHECKING:
    from moodle import Moodle

T = TypeVar('T')


class BaseMoodle(object):
    def __init__(self, moodle):
        self._moodle = moodle
        self.__post_init__(moodle)

    def __post_init__(self, moodle) -> None:
        pass

    @property
    def moodle(self) -> 'Moodle':
        return self._moodle

    @staticmethod
    def _tr(kls: Type[T], *args, **kwargs) -> T:
        return cattr.structure(kwargs, kls)  # type: ignore

    @staticmethod
    def _trs(kls: Type[T], datas: Iterable[Any]) -> List[T]:
        return [cattr.structure(datas, kls)
                for data in datas] if datas else []  # type: ignore
