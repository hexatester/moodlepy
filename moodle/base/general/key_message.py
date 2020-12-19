from dataclasses import dataclass


@dataclass
class GeneralKeyMessage:
    """GeneralKeyMessage

    Args:
        key (str): ...
        message (str): ...
    """
    key: str
    message: str
