from moodle.attr import dataclass


@dataclass
class GeneralIdName:
    """GeneralIdName

    Args:
        id (str): ...
        name (Any): ...
    """
    id: str
    name: str
