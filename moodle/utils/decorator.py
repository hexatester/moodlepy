import logging
from functools import wraps
from typing import Callable, Type
from moodle import MoodleObject


def meta(wsfunction: str, moodlewsrestformat: str) -> Callable:
    def decorator(cls: Type[MoodleObject]) -> Type[MoodleObject]:
        setattr(cls, 'wsfunction', wsfunction)
        setattr(cls, 'moodlewsrestformat', moodlewsrestformat)
        return cls

    return decorator


def deprecated(func: Callable):
    """Specify the method is deprecated

    Args:
        func (Callable): Wsfunction of moodlepy

    Returns:
        Callable: Decorated func
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        logging.warning(
            '** DEPRECATED ** Please do not call this function any more')
        return func(*args, **kwargs)

    return wrapper
