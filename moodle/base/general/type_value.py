from moodle.attr import dataclass


@dataclass
class GeneralTypeValue:
    """GeneralTypeValue

    Args:
        type (str): ...
        value (str): ...
    """
    type: str
    value: str
