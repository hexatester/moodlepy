from operator import getitem
from typing import Any, Generic, Iterator, List, Optional, TypeVar

T = TypeVar("T")


class ResponsesFactory(Generic[T]):
    @property
    def items(self) -> List[T]:
        return []

    def __bool__(self) -> bool:
        return bool(self.items)

    def __getitem__(self, index: int) -> T:
        return getitem(self.items, index)

    def __iter__(self) -> Iterator[T]:
        return iter(self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def first(self) -> T:
        return getitem(self.items, 0)

    def get(self, key: Any, name: str = "id", default: T = None) -> Optional[T]:
        for item in self.items:
            if not hasattr(item, name):
                continue
            if getattr(item, name) == key:
                return item
        return default

    def last(self) -> T:
        return getitem(self.items, -1)
