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
        logging.warn(
            f'{func.__name__} **DEPRECATED** Please do not call this function any more',
            DeprecationWarning)
        return func(*args, **kwargs)

    return wrapper


def lazy(func):
    '''Decorator that makes a property lazy-evaluated.
    Source : https://stevenloria.com/lazy-properties/
    '''
    attr_name = '_lazy_' + func.__name__

    @wraps(func)
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self))
        return getattr(self, attr_name)

    return wrapper
