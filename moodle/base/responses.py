from operator import getitem
from typing import Generic, Iterator, List, TypeVar

T = TypeVar('T')


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

    def last(self) -> T:
        return getitem(self.items, -1)
