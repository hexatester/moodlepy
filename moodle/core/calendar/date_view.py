from dataclasses import dataclass


@dataclass
class DateView:
    """Date
    Constructor arguments:
    params: seconds (int): seconds
    params: minutes (int): minutes
    params: hours (int): hours
    params: mday (int): mday
    params: wday (int): wday
    params: mon (int): mon
    params: year (int): year
    params: yday (int): yday
    params: weekday (str): weekday
    params: month (str): month
    params: timestamp (int): timestamp
    """
    seconds: int
    minutes: int
    hours: int
    mday: int
    wday: int
    mon: int
    year: int
    yday: int
    weekday: str
    month: str
    timestamp: int
