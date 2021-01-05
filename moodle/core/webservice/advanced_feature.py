from moodle.attr import dataclass


@dataclass
class AdvancedFeatures:
    name: str
    value: int

    def __str__(self) -> str:
        return self.name
