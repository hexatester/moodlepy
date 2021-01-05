from moodle.attr import dataclass


@dataclass
class GeneralNameValue:
    """General NameValue
    Args:
        name (str): Name
        value (str): Value
    """
    name: str
    value: str

    def __str__(self) -> str:
        return f"{self.name} : {self.value}"
