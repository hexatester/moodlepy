from typing import Callable, Type
from moodlepy import MoodleObject


def meta(wsfunction: str, moodlewsrestformat: str) -> Callable:
    def decorator(cls: Type[MoodleObject]) -> Type[MoodleObject]:
        cls.wsfunction = wsfunction
        cls.moodlewsrestformat = moodlewsrestformat
        return cls

    return decorator
