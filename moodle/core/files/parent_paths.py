from moodle.attr import dataclass
from typing import List

from moodle import MoodleWarning, ResponsesFactory


@dataclass
class ParentPaths(ResponsesFactory[str]):
    """Parent Paths

    Args
        parentpaths (List[str]): Path to parent directory of the deleted files.
        warnings (List[Warning]): list of warnings
    """
    parentpaths: List[str]
    warnings: List[MoodleWarning]

    @property
    def items(self) -> List[str]:
        return self.parentpaths
