from moodle.attr import dataclass
from typing import Any


@dataclass
class GeneralKeyValue:
    """GeneralKeyValue

    Args:
        key (str): ...
        value (Any): ...
    """

    key: str
    value: Any
