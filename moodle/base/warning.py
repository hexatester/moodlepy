from dataclasses import dataclass


@dataclass
class Warning:
    item: str
    itemid: int
    warningcode: str
    message: str

    def __str__(self) -> str:
        return self.message
